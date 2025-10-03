from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import csv

# Setup Chrome options for headless browsing (optional)
def setup_driver(headless=False):
    """Setup Chrome WebDriver with options"""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scrape_top_ten_vulnerabilities():
  driver = setup_driver()

  try:
    driver.get("https://owasp.org/www-project-top-ten/")

    # Wait for list link to load
    wait = WebDriverWait(driver, 10)

    link_list = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "/html/body/main/div/div[1]/section[1]/ul[2]/li/a")))

    results = []

    for link in link_list:
      try:
          title = link.find_element(By.XPATH, ".//strong").text
          # title = link.find_element(By.XPATH, "//*/ul[2]/li/a/strong").text
          href_link = link.get_attribute("href")

          scraped_vulnerabilities = {
            "Title": title,
            "Href Link": href_link
          }
          results.append(scraped_vulnerabilities)

      except Exception as e:
        print(f"Error scraping vulnerabilities: {e}")
        continue

    return results

  finally:
    driver.quit()

print(scrape_top_ten_vulnerabilities())

#Task 6.4: Write out the Data
def scrape_and_export_to_csv():
    vulnerabilities = scrape_top_ten_vulnerabilities()

    with open('owasp_top_10.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Href Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for vulnerability in vulnerabilities:
            vulnerability_copy = vulnerability.copy()
            writer.writerow(vulnerability_copy)

    print(f"Exported {len(vulnerabilities)} vulnerabilities to owasp_top_10.csv")
scrape_and_export_to_csv()

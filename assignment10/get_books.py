from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import json
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

#Task 2: Understanding HTML and the DOM for the Durham Library Site
#Note the values for the class attribute of this entry:
#3 li: class="row cp-search-result-item" (I need to remove the row class later since that's a separate class)
#4 title: class="title-content"
#5 author: class="cp-author-link"
#6 format/year: class="display-info-primary"


#Task 3: Write a Program to Extract this Data
def scrape_search_list_results():
  driver = setup_driver()

  try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

    # Wait for list items to load
    wait = WebDriverWait(driver, 10)
    list_items = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.cp-search-result-item")))

    results = []

    for item in list_items:
      try:
          title = item.find_element(By.CSS_SELECTOR, ".title-content").text

          author_elements = item.find_elements(By.CSS_SELECTOR, ".cp-author-link")
          author = []
          for author_element in author_elements:
            author_text = author_element.text.strip()

          author.append(author_text)
          authors = "; ".join(author)

          format_year_element = item.find_element(By.CSS_SELECTOR, ".display-info-primary")
          format_year = format_year_element.text.strip()

          scraped_books = {
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
          }
          results.append(scraped_books)

      except Exception as e:
        print(f"Error scraping books: {e}")
        continue

    return results

  finally:
    driver.quit()

print(scrape_search_list_results())

results = scrape_search_list_results()

df = pd.DataFrame(results)
print(f"DataFrame created.")
print(df)


#To search through all the pages, we would have to keep track of what page we're on and then see if there's a next button to click on. If there is, we'd have to increase our page number tracker and run the function to scrape the data from the current page until there's no more pages found.In this example we might be looking at the class selector ".pagination__next-chevron".

#Task 4: Write out the Data
def scrape_and_export_to_csv():
    books = scrape_search_list_results()

    with open('get_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Author', 'Format-Year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for book in books:
            book_copy = book.copy()
            writer.writerow(book_copy)

    print(f"Exported {len(books)} books to books.csv")
scrape_and_export_to_csv()

def scrape_and_export_to_json():
    books = scrape_search_list_results()

    with open('get_books.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(books, jsonfile, indent=2, ensure_ascii=False)

    print(f"Exported {len(books)} books to get_books.json")
scrape_and_export_to_json()

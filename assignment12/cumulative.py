import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
  query = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
    FROM orders o JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id;
  """
  df = pd.read_sql_query(query, conn)
  print(df)

def cumulative(row):
  totals_above = df['total_price'][0:row.name+1]
  return totals_above.sum()

df['cumulative'] = df['total_price'].cumsum()
print(df)

categories = df["order_id"]
cumulative_revenue = df["cumulative"]
plt.plot(categories, cumulative_revenue, marker='o', linestyle='-', color='blue')
plt.title("Cumulative Revenue")
plt.xlabel("Order Id")
plt.ylabel("Revenue ($)")
plt.show()

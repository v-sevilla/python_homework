import pandas as pd
import sqlite3

#Task 1: Complex JOINs with Aggregation
with sqlite3.connect("../db/lesson.db") as conn:
  query = """
    SELECT o.order_id, ROUND(SUM(li.quantity * p.price),2)
    FROM orders AS o
    JOIN line_items AS li
    ON li.order_id = o.order_id
    JOIN products AS p
    ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;"""
  df = pd.read_sql_query(query, conn)
  print(df, '\n')

#Task 2: Understanding Subqueries
  query = """
    SELECT c.customer_name,
    ROUND(AVG(total_price), 2) AS average_total_price
    FROM customers AS c
    LEFT JOIN (
      SELECT o.order_id, o.customer_id AS customer_id_b, ROUND(SUM(li.quantity * p.price),2) AS total_price
      FROM orders AS o
      JOIN line_items AS li
      ON li.order_id = o.order_id
      JOIN products AS p
      ON li.product_id = p.product_id
      GROUP BY o.customer_id, o.order_id
    ) ON c.customer_id = customer_id_b
    GROUP BY c.customer_id
    ORDER BY c.customer_id
    """
  df = pd.read_sql_query(query, conn)
  print(df, '\n')

#Task 4:Aggregation with HAVING
  query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT (o.order_id) AS order_count
    FROM employees AS e
    JOIN orders AS o
    ON o.employee_id = e.employee_id
    GROUP BY e.employee_id, e.first_name, e.last_name
    HAVING COUNT(o.order_id) > 5
    """

df = pd.read_sql_query(query, conn)
print(df, '\n')


#Task 3: An Insert Transaction Based on Data

conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

def add_order_id(cursor, customer_id, employee_id, date):
  try:
      cursor.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?,?,?) RETURNING order_id", (customer_id, employee_id, date))
  except Exception as e:
    conn.rollback()
    print("Error:", e)

def add_order(cursor, order_id, product_id, quantity):
  try:
      cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?,?,?)", (order_id, product_id, quantity))
  except Exception as e:
    conn.rollback()
    print("Error:", e)

add_order_id(cursor, 16, 7, '2025-09-09')
add_order(cursor, 250, 23, 10)
add_order(cursor, 251, 18, 10)
add_order(cursor, 252, 43, 10)
add_order(cursor, 253, 9, 10)
add_order(cursor, 254, 44, 10)

conn.commit()

query = """
  SELECT li.line_item_id, p.product_name, li.quantity
  FROM line_items AS li
  JOIN products AS p
  ON p.product_id = li.product_id
  WHERE li.order_id = (
    SELECT o.order_id
    FROM orders o
    JOIN customers c
    ON c.customer_id = o.customer_id
    JOIN employees e
    ON e.employee_id = o.employee_id
    WHERE c.customer_name = 'Perez and Sons'
  )
  ORDER BY li.line_item_id;
"""
df = pd.read_sql_query(query, conn)
print(df)

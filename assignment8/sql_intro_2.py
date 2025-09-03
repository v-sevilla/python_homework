import pandas as pd
import sqlite3
import csv

#Task 5:Read Data into a DataFrame
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
    SELECT line_items.line_item_id, line_items.quantity, products.product_id, products.product_name, products.price
    FROM line_items JOIN products ON line_items.product_id = products.product_id"""
    df = pd.read_sql_query(sql_statement, conn)

#Print the first 5 lines of the resulting DataFrame.
print(df.head(5), '\n')

#Add a column to the DataFrame called "total".
df['total'] = df['quantity'] * df['price']
print(df.head(5), '\n')

#Add groupby() code to group by the product_id. 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'.
df = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'})
print(df.head(5), '\n')

#Sort the DataFrame by the product_name column
df.sort_values(by='product_name')
print(df.head(5))

#write this DataFrame to a file order_summary.csv
df.to_csv('order_summary.csv', index=False)

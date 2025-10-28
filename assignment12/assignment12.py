import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.data as pldata

#Task 1: Plotting with Pandas
with sqlite3.connect("../db/lesson.db") as conn:
  query = """
    SELECT last_name, SUM(price * quantity) AS revenue
    FROM employees e JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id;
  """
  employee_results = pd.read_sql_query(query, conn)

ax = employee_results.plot.bar(x='last_name', y='revenue', color='green')

plt.xlabel('Employee Last Name')
plt.ylabel('Revenue')
plt.show()

#Task 3: Interactive Visualizations with Plotly
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

df['strength'] = df['strength'].str.replace('6+', '6-6')
min_range = df['strength'].str.split('-').str[0].astype(float)
max_range = df['strength'].str.split('-').str[1].astype(float)
df['strength'] = (min_range + max_range) / 2
print(df.head(10))
print(df.tail(10))

fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Data, Strength vs. Frequency")
fig.write_html("wind.html", auto_open=True)

import sqlite3
import json
from sqlite3.dbapi2 import Cursor, connect

print('Plz enter drug name')
drugName = input('Brand Name: ')
query = f"Select * From Brands WHERE Brandname LIKE '%{drugName}%' "
print(type(drugName))
con = sqlite3.connect('drugPrice.db')
cursor = con.cursor()
cursor.execute(query)
rows = cursor.fetchall()

# Get the column names from the cursor description
column_names = [description[0] for description in cursor.description]

# Convert the results to a list of dictionaries
result_list = [dict(zip(column_names, row)) for row in rows]

for item in result_list:
    print(item['Brandname'],item['Price'])


# for item in data:
    # print(item['Brandname'],item['Price'],item['Company'])

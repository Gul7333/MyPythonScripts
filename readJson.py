import time
import sqlite3
import json
# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('./drugPrice.db')
cursor = conn.cursor()

# Create a table named 'example_table'
cursor.execute('''
    CREATE TABLE IF NOt Exists Brands (
        id INTEGER PRIMARY KEY,
        Brandname TEXT,
        Price INTEGER,
        Formulation TEXT,
        Company TEXT,
        Packsize TEXT
    )
''')

with open('./_result_2024-02-06_22-02-56.json','r') as file:
    jsondata = json.load(file)
    for item in jsondata['value']:
        print(item['BrandName'])
        cursor.execute('''
        INSERT INTO Brands (Brandname, Price, Formulation, Company, Packsize ) VALUES (?, ?, ?, ?, ?)
        ''',(item['BrandName'],item['MRP'],item['Formulation'],item['CompanyName'],item['PackSize']))
# Commit changes and close connection
conn.commit()
conn.close()


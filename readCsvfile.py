import csv

# Specify the path to your CSV file
csv_file_path = './Free_Proxy_List.csv'

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Each row is a list representing the columns in that row
        print(row.index(,0,2))

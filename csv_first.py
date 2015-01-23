import csv
 
filename = "example.csv"
 
with open(filename) as csv_file:
    processed_csv = csv.reader(csv_file)
 
    for csv_row in processed_csv:
        for column in csv_row:
            print(column)

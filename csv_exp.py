import csv
 
filename = "example.csv"
 
with open(filename) as csv_file:
    processed_csv = list(csv.reader(csv_file))
    print(processed_csv[0])

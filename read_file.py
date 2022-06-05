import csv


file = open('./test_coordinate/target_coordinate.csv', 'r')
print('csv file opened')
csvreader = csv.reader(file)
print('csv file read')
rows = []
for row in csvreader:
    rows.append(row)
print('coordinate data appended')
print(rows)
file.close()
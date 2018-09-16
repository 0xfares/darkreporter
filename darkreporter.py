import csv

with open('nessus.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Plugin'],'----', row['Plugin Name'])

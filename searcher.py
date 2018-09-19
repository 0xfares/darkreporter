import csv
import sys

#input number you want to search
number = input('Enter number to find\n')


with open('nessus.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if number == row['Plugin']:
			print(row['IP Address'],'\n\n\n')

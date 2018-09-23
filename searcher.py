import csv
import sys

AllData = []
AllData = list()

#input number you want to search
number = input('Enter number to find\n')


with open('nessus.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if number == row['Plugin']:
			IPAddressesRow = row['IP Address']
			AllData.append(IPAddressesRow)
print(AllData)
RemovingDublicates = list(set(AllData))
RemovingDublicates.sort()
print(RemovingDublicates)

import csv
AllData = []
AllData = list()
with open('nessus.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		PluginRow = row['Plugin']
		AllData.append(PluginRow)
#print(len(AllData))
#print(AllData[0])
print(AllData)
AllData.sort()
print(AllData)
RemovingDublicates = list(set(AllData))
RemovingDublicates.sort()
print(RemovingDublicates)
                #PluginRow = row['Plugin']
                #AllData.append(PluginRow)
	#print(x)
		#print('Plugin ---> ', row['Plugin'])
		#print('Plugin Name ---> ', row['Plugin Name'])
		#print('Family ---> ', row['Family'])
		#print('Severity ---> ', row['Severity'])
		#print('IP Address ---> ', row['IP Address'])
		#print('Protocol ---> ', row['Protocol'])
		#print('Port ---> ', row['Port'])
		#print('Exploit? ---> ', row['Exploit?'])
		#print('Repository ---> ', row['Repository'])
		#print('MAC Address ---> ', row['MAC Address'])
		#print('DNS Name ---> ', row['DNS Name'])
		#print('NetBIOS Name ---> ', row['NetBIOS Name'])
		#print('Plugin Text ---> ', row['Plugin Text'])
		#print('First Discovered ---> ', row['First Discovered'])
		#print('Last Observed ---> ', row['Last Observed'])
		#print('Exploit Frameworks ---> ', row['Exploit Frameworks'])
		#print('Synopsis ---> ', row['Synopsis'])
		#print('Description ---> ', row['Description'])
		#print('Solution ---> ', row['Solution'])
		#print('See Also ---> ', row['See Also'])
		#print('CVE ---> ', row['CVE'])
		#print('Vulnerablity Publication Date ---> ', row['Vuln Publication Date'])
		#print('Exploit Ease ---> ', row['Exploit Ease'])
		#print('\n\n')
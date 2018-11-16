import csv
import sys


#Defining list of variables hold the actual data.
#IP Addresses Varible
RowOfDataIPAddress = []
RowOfDataIPAddress = list()
#Plugin Name Varible
RowOfDataPluginName = []
RowOfDataPluginName = list()
#Family Varibale
RowOfDataFamily = []
RowOfDataFamily = list()
#Severity Varible
RowOfDataSeverity = []
RowOfDataSeverity = list()
#IP Address Varible
RowOfDataIPAddress = []
RowOfDataIPAddress = list()
#Protocol Varible
RowOfDataProtocol = []
RowOfDataProtocol = list()
#Port Varibale
RowOfDataPort = []
RowOfDataPort = list()
#Exploit? Varible
RowOfDataIsExploitable = []
RowOfDataIsExploitable = list()
#Repository Varible
RowOfDataRepository = []
RowOfDataRepository = list()
#MAC Address Variable
RowOfDataMACAddress = []
RowOfDataMACAddress = list()
#DNS Name Varibale
RowOfDataDNSName = []
RowOfDataDNSName = list()
#NetBIOS Name Variable
RowOfDataNetBIOSName = []
RowOfDataNetBIOSName = list()
#Plugin Text Variable
RowOfDataPluginText = []
RowOfDataPluginText = list()
#First Discovered Variable
RowOfDataFirstDiscovered = []
RowOfDataFirstDiscovered = list()
#Last Observed Varibale
RowOfDataLastObserved = []
RowOfDataLastObserved = list()
#Exploit Frameworks Varibale
RowOfDataExploitFrameworks = []
RowOfDataExploitFrameworks = list()
#Synopsis Varibale
RowOfDataSynopsis = []
RowOfDataSynopsis = list()
#Description Varibale
RowOfDataDescription = []
RowOfDataDescription = list()
#Solution Varibale
RowOfDataSolution = []
RowOfDataSolution = list()
#See Also Varibale
RowOfDataSeeAlso = []
RowOfDataSeeAlso = list()
#CVE Variable
RowOfDataCVE = []
RowOfDataCVE = list()
#Vulnerablity Publication Date Variable
RowOfDataVulnerablityPublicationDate = []
RowOfDataVulnerablityPublicationDate = list()
#Exploit Ease Variable
RowOfDataExploitEase = []
RowOfDataExploitEase = list()

#All Data In One Place
SingleRow = []
SingleRow = list()

#All Data In One Place
FullData = []
FullData = list()


with open('nessus.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		PluginRow = row['Plugin']
		SingleRow.append(PluginRow)
#print(len(AllData))
#print(AllData[0])


print("\n")
print("********************************************************************************************************")
print("						Printing the whole data...				       ")
print("********************************************************************************************************")
print(SingleRow)
print("========================================================================================================")
print("\n")
print("********************************************************************************************************")
print("						Sorting the data...					       ")
print("********************************************************************************************************")
SingleRow.sort()
print(SingleRow)
print("========================================================================================================")
print("\n")
print("********************************************************************************************************")
print("						Removing the dublicates...				       ")
print("********************************************************************************************************")
RemovingDublicates1 = list(set(SingleRow))
RemovingDublicates1.sort()
print(RemovingDublicates1)
print("========================================================================================================")
print("\n")
i = 0
while i < len(RemovingDublicates1):
	with open('nessus.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
				if RemovingDublicates1[i] == row['Plugin']:
					#fetching the data as rows
					PluginNameRow = row['Plugin Name']
		
					#Appending the results in the lists
					RowOfDataPluginName.append(PluginNameRow)

		
					AllData= list(set(RowOfDataPluginName))
	#AllData.append({'Plugin Name':RemovingDuplicatesFromPluginName})
		i += 1	
	#print(RemovingDublicates[i])
print(AllData)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
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

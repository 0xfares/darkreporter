import csv
import sys
from collections import defaultdict

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
RowOfDataHostName = []
RowOfDataHostName = list()
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
		PluginRow = row['Plugin ID']
		SingleRow.append(PluginRow)
#print(len(AllData))
#print(AllData[0])


#print("\n")
#print("********************************************************************************************************")
#print("						Printing the whole data...				       ")
#print("********************************************************************************************************")
#print(SingleRow)
#print("========================================================================================================")
#print("\n")
#print("********************************************************************************************************")
#print("						Sorting the data...					       ")
#print("********************************************************************************************************")
SingleRow.sort()
#print(SingleRow)
#print("========================================================================================================")
#print("\n")
#print("********************************************************************************************************")
#print("						Removing the dublicates...				       ")
#print("********************************************************************************************************")
RemovingDublicates1 = list(set(SingleRow))
RemovingDublicates1.sort()
#print(RemovingDublicates1)
#print("========================================================================================================")
#print("\n")
i = 0
while i < len(RemovingDublicates1):
	with open('nessus.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
				if RemovingDublicates1[i] == row['Plugin ID']:
					#fetching the data as rows
					PluginNameRow = row['Name']
					HostNameRow = row['Host']
					ProtocolRow = row['Protocol']
					PortRow = row['Port']

					#Appending the results in the lists
					RowOfDataPluginName.append(PluginNameRow)
					RowOfDataHostName.append(HostNameRow)
					RowOfDataProtocol.append(ProtocolRow)
					RowOfDataPort.append(PortRow)
		
					#RowOfDataPluginName.sort()
					#RowOfDataHostName.sort()

					AllData = list(RowOfDataPluginName)
					AllData1 = list(RowOfDataHostName)
					AllData2 = list(RowOfDataProtocol)
					AllData3 = list(RowOfDataPort)
		i += 1	
#print(AllData)
#print(len(AllData))
#print(len(AllData1))
AllDataMeans = []
AllDataMeans = list()
for j in range(len(AllData)):
	print(AllData[j])
	matches = [index for index, value in enumerate(AllData) if value == AllData[j]]
	#display the data based on matches list hostnames,an more
	for xx in range(len(matches)): 
		print(AllData1[xx],AllData2[xx],AllData3[xx])
	print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
	AllDataMeans.append(({AllData[j]:[AllData1[j],AllData2[j],AllData3[j]]}))
matches = [index for index, value in enumerate(AllData) if value == "SSL Certificate Signed Using Weak Hashing Algorithm (Known CA)" ]
print(matches)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#res = defaultdict(list)
#for vulName,vulHost in AllDataMeans: 
#	res[vulName].append(vulHost)
#print([{'vulnerablity':vulName, 'host':vulHost} for vulName,vulHost in res.items()])
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

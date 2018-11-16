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
AllData = []
AllData = list()

with open('nessus.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		PluginRow = row['Plugin']
		AllData.append(PluginRow)
#print(len(AllData))
#print(AllData[0])


print("\n")
print("********************************************************************************************************")
print("						Printing the whole data...				       ")
print("********************************************************************************************************")
print(AllData)
print("========================================================================================================")
print("\n")
print("********************************************************************************************************")
print("						Sorting the data...					       ")
print("********************************************************************************************************")
AllData.sort()
print(AllData)
print("========================================================================================================")
print("\n")
print("********************************************************************************************************")
print("						Removing the dublicates...				       ")
print("********************************************************************************************************")
RemovingDublicates = list(set(AllData))
RemovingDublicates.sort()
print(RemovingDublicates)
print("========================================================================================================")
print("\n")
i = 0
while i < len(RemovingDublicates):
	with open('nessus.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
				if RemovingDublicates[i] == row['Plugin']:
					#fetching the data as rows
					PluginNameRow = row['Plugin Name']
					FamilyRow = row['Family']
					SeverityRow = row['Severity']
					IPAddressRow = row['IP Address']
					ProtocolRow = row['Protocol']
					PortRow = row['Port']
					ExploitRow = row['Exploit?']
					RepositoryRow = row['Repository']
					MACAddressRow = row['MAC Address']
					DNSNameRow = row['DNS Name']
					NetBIOSNameRow = row['NetBIOS Name']
					PluginTextRow = row['Plugin Text']
					FirstDiscoveredRow = row['First Discovered']
					LastObservedRow = row['Last Observed']
					ExploitFrameworksRow = row['Exploit Frameworks']
					SynopsisRow = row['Synopsis']
					DescriptionRow = row['Description']
					SolutionRow = row['Solution']
					SeeAlsoRow = row['See Also']
					CVERow = row['CVE']
					VulnerablityPublicationDateRow = row['Vuln Publication Date']
					ExploitEaseRow = row['Exploit Ease']
		
					#Appending the results in the lists
					RowOfDataPluginName.append(PluginNameRow)
					RowOfDataFamily.append(FamilyRow)
					RowOfDataSeverity.append(SeverityRow)		
					RowOfDataIPAddress.append(IPAddressRow)
					RowOfDataProtocol.append(ProtocolRow)
					RowOfDataPort.append(PortRow)
					RowOfDataIsExploitable.append(ExploitRow)
					RowOfDataRepository.append(RepositoryRow)
					RowOfDataMACAddress.append(MACAddressRow)
					RowOfDataDNSName.append(DNSNameRow)
					RowOfDataNetBIOSName.append(NetBIOSNameRow)
					RowOfDataPluginText.append(PluginTextRow)
					RowOfDataFirstDiscovered.append(FirstDiscoveredRow)
					RowOfDataLastObserved.append(LastObservedRow)
					RowOfDataExploitFrameworks.append(ExploitFrameworksRow)
					RowOfDataSynopsis.append(SynopsisRow)
					RowOfDataDescription.append(DescriptionRow)
					RowOfDataSolution.append(SolutionRow)
					RowOfDataSeeAlso.append(SeeAlsoRow)
					RowOfDataCVE.append(CVERow)
					RowOfDataVulnerablityPublicationDate.append(VulnerablityPublicationDateRow)
					RowOfDataExploitEase.append(ExploitEaseRow)
					
					#Removing the Duplicates Values
					RemovingDuplicatesFromPluginName = list(set(RowOfDataPluginName))
					RemovingDuplicatesFromFamily = list(set(RowOfDataFamily))
					RemovingDuplicatesFromSeverity = list(set(RowOfDataSeverity))
					RemovingDuplicatesFromIPAddress = list(set(RowOfDataIPAddress))
					RemovingDuplicatesFromProtocol = list(set(RowOfDataProtocol))
					RemovingDuplicatesFromPort = list(set(RowOfDataPort))
					RemovingDuplicatesFromExploitable = list(set(RowOfDataIsExploitable))
					RemovingDuplicatesFromRepository = list(set(RowOfDataRepository))
					RemovingDuplicatesFromMACAddress = list(set(RowOfDataMACAddress))
					RemovingDuplicatesFromDNSName = list(set(RowOfDataDNSName))
					RemovingDuplicatesFromNetBIOSName = list(set(RowOfDataNetBIOSName))
					RemovingDuplicatesFromPluginText = list(set(RowOfDataPluginText))
					RemovingDuplicatesFromFirstDiscovered = list(set(RowOfDataFirstDiscovered))
					RemovingDuplicatesFromLastObserved = list(set(RowOfDataLastObserved))
					RemovingDuplicatesFromExploitFrameworks = list(set(RowOfDataExploitFrameworks))
					RemovingDuplicatesFromSynopsis = list(set(RowOfDataSynopsis))
					RemovingDuplicatesFromDescription = list(set(RowOfDataDescription))
					RemovingDuplicatesFromSolution = list(set(RowOfDataSolution))
					RemovingDuplicatesFromSeeAlso = list(set(RowOfDataSeeAlso))
					RemovingDuplicatesFromCVE = list(set(RowOfDataCVE))
					RemovingDuplicatesFromVulnerablityPublicationDate = list(set(RowOfDataVulnerablityPublicationDate))
					RemovingDuplicatesFromExploitEase = list(set(RowOfDataExploitEase))
					
					#Sorting the Data			
					RemovingDuplicatesFromPluginName.sort()
					RemovingDuplicatesFromFamily.sort()
					RemovingDuplicatesFromSeverity.sort()
					RemovingDuplicatesFromIPAddress.sort()
					RemovingDuplicatesFromProtocol.sort()
					RemovingDuplicatesFromPort.sort()
					RemovingDuplicatesFromExploitable.sort()
					RemovingDuplicatesFromRepository.sort()
					RemovingDuplicatesFromMACAddress.sort()
					RemovingDuplicatesFromDNSName.sort()
					RemovingDuplicatesFromNetBIOSName.sort()
					RemovingDuplicatesFromPluginText.sort()
					RemovingDuplicatesFromFirstDiscovered.sort()
					RemovingDuplicatesFromLastObserved.sort()
					RemovingDuplicatesFromExploitFrameworks.sort()
					RemovingDuplicatesFromSynopsis.sort()
					RemovingDuplicatesFromDescription.sort()
					RemovingDuplicatesFromSolution.sort()
					RemovingDuplicatesFromSeeAlso.sort()
					RemovingDuplicatesFromCVE.sort()
					RemovingDuplicatesFromVulnerablityPublicationDate.sort()
					RemovingDuplicatesFromExploitEase.sort()
			
					AllData.append({'Plugin Name':RemovingDuplicatesFromPluginName,'Family':RemovingDuplicatesFromFamily,'Severity':RemovingDuplicatesFromSeverity,'IP Address':RemovingDuplicatesFromIPAddress,'Protocol':RemovingDuplicatesFromProtocol,'Port':RemovingDuplicatesFromPort,'Exploitable':RemovingDuplicatesFromExploitable,'Repository':RemovingDuplicatesFromRepository,'MACAddress':RemovingDuplicatesFromMACAddress,'DNSName':RemovingDuplicatesFromDNSName,'NetBIOSName':RemovingDuplicatesFromNetBIOSName,'PluginText':RemovingDuplicatesFromPluginText,'FirstDiscovered':RemovingDuplicatesFromFirstDiscovered,'LastObserved':RemovingDuplicatesFromLastObserved,'ExploitFrameworks':RemovingDuplicatesFromExploitFrameworks,'Synopsis':RemovingDuplicatesFromSynopsis,'Description':RemovingDuplicatesFromDescription,'Solution':RemovingDuplicatesFromSolution,'SeeAlso':RemovingDuplicatesFromSeeAlso,'CVE':RemovingDuplicatesFromCVE,'VulnerabilityPublicationDate':RemovingDuplicatesFromVulnerablityPublicationDate,'ExploitEase':RemovingDuplicatesFromExploitEase})
					print(AllData)
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("*************************************************************************************************************************************************")
	print("*************************************************************************************************************************************************")

	#print(RemovingDublicates[i])
	i += 1

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

import csv
import sys
from collections import defaultdict

#Defining list of variables hold the actual data.
#IP Addresses Varible
RowOfDataIPAddress = []
RowOfDataIPAddress = list()
#Plugin ID Varible
RowOfDataPluginID = []
RowOfDataPluginID = list()
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
PluginsIndexList = []
PluginsIndexList = list()

with open('nessus.csv') as MainCSVFile:
	FirstRoundReader = csv.DictReader(MainCSVFile)
	for IndexPluginRows in FirstRoundReader:
		PluginListIndexer = IndexPluginRows['Plugin ID']
		PluginsIndexList.append(PluginListIndexer)

PluginsIndexList.sort()
RemovingDublicatesFromIndexList = list(set(PluginsIndexList))
RemovingDublicatesFromIndexList.sort()
print(RemovingDublicatesFromIndexList)

IndexCounter = 0
while IndexCounter < len(RemovingDublicatesFromIndexList):
	with open('nessus.csv') as SecondMainFileLoading:
		SecondRoundReader = csv.DictReader(SecondMainFileLoading)
		for IndexAllDataRows in SecondRoundReader:
				if RemovingDublicatesFromIndexList[IndexCounter] == IndexAllDataRows['Plugin ID']:
					#fetching the data as rows
					PluginIDRows = IndexAllDataRows['Plugin ID']
					PluginNameRows = IndexAllDataRows['Name']
					HostNameRows = IndexAllDataRows['Host']
					ProtocolRows = IndexAllDataRows['Protocol']
					PortRows = IndexAllDataRows['Port']

					#Appending the results in the lists
					RowOfDataPluginID.append(PluginIDRows)
					RowOfDataPluginName.append(PluginNameRows)
					RowOfDataHostName.append(HostNameRows)
					RowOfDataProtocol.append(ProtocolRows)
					RowOfDataPort.append(PortRows)
		
					#RowOfDataPluginName.sort()
					#RowOfDataHostName.sort()
					AllDataPluginIDs = list(RowOfDataPluginID)
					AllDataPluginNames = list(RowOfDataPluginName)
					AllDataPluginNames2 = list(set(RowOfDataPluginName))
					AllDataHostNames = list(RowOfDataHostName)
					AllDataHostNames2 = list(set(RowOfDataHostName))
					AllDataProtocols = list(RowOfDataProtocol)
					AllDataPorts = list(RowOfDataPort)
		IndexCounter += 1	

AllData = []
AllData = list()
for j in range(len(AllDataPluginNames2)):
	print(j,AllDataPluginNames2[j])
	matches = [index for index, value in enumerate(AllDataPluginNames) if value == AllDataPluginNames2[j]]
	print("*************************************************************************************")
	print(matches)
	print("*************************************************************************************")
	#display the data based on matches list hostnames,an more
	for xx in range(len(matches)): 
		#print(AllDataPluginNames[xx])
		print(xx,AllDataHostNames[matches[xx]])
		#print()
	print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
	#AllData.append(({AllDataPluginNames[j]:[AllDataHostNames[j],AllDataProtocols[j],AllDataPorts[j]]}))

import csv
import sys
from collections import defaultdict
import re

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

def contentCleaner(str):
    regex = r"(?<=^)(.*?)(?<=\))"

    test_str = str

    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        print(match.group())

with open('nessus1.csv') as MainCSVFile:
	FirstRoundReader = csv.DictReader(MainCSVFile)
	for IndexPluginRows in FirstRoundReader:
		PluginListIndexer = IndexPluginRows['IP Address']
		PluginsIndexList.append(PluginListIndexer)

PluginsIndexList.sort()
RemovingDublicatesFromIndexList = list(set(PluginsIndexList))
RemovingDublicatesFromIndexList.sort()
print(RemovingDublicatesFromIndexList)

IndexCounter = 0
while IndexCounter < len(RemovingDublicatesFromIndexList):
	with open('nessus1.csv') as SecondMainFileLoading:
		SecondRoundReader = csv.DictReader(SecondMainFileLoading)
		for IndexAllDataRows in SecondRoundReader:
				if RemovingDublicatesFromIndexList[IndexCounter] == IndexAllDataRows['IP Address']:
					#fetching the data as rows
					PluginIDRows = IndexAllDataRows['IP Address']
					PluginNameRows = IndexAllDataRows['NetBIOS Name']
					HostNameRows = IndexAllDataRows['Plugin Text']


					#Appending the results in the lists
					RowOfDataPluginID.append(PluginIDRows)
					RowOfDataPluginName.append(PluginNameRows)
					RowOfDataHostName.append(HostNameRows)

		
					#RowOfDataPluginName.sort()
					#RowOfDataHostName.sort()
					AllDataPluginIDs = list(set(RowOfDataPluginID))
					AllDataPluginNames = list(RowOfDataPluginName)
					AllDataHostNames = list(RowOfDataHostName)

		IndexCounter += 1	

AllData = []
AllData = list()
for j in range(len(AllDataPluginIDs)):
	matches = [index for index, value in enumerate(AllDataPluginIDs) if value == AllDataPluginIDs[j]]
	#display the data based on matches list hostnames,an more
	for xx in range(len(matches)): 
		#print(AllDataPluginNames[xx])
		print(AllDataPluginIDs[matches[xx]],AllDataPluginNames[matches[xx]],contentCleaner(AllDataHostNames[matches[xx]]))
		#print()
	print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
	#AllData.append(({AllDataPluginNames[j]:[AllDataHostNames[j],AllDataProtocols[j],AllDataPorts[j]]}))

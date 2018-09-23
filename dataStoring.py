import mysql.connector as mysql

class DarkStoringData:
	def dark_db_config(self, DB_USERNAME, DB_PASSWORD, DB_HOST_OR_IP, DB_NAME):
		configuration = {
				'darkdbusername': DB_USERNAME,
				'darkdbpassword': DB_PASSWORD,
				'darkdbhostname': DB_HOST_OR_IP,
				'darkdbname': DB_NAME
		}
		return configuration

	def dark_db_connector(self, CONFIGURATION_INFO):
		initConnection = mysql.connect(CONFIGURATION_INFO)
		cursor = initConnection.cursor()

dsd = DarkStoringData()
config = dsd.dark_db_config('root','toor','localhost','darkcoders')
print(config)
#connect = dsd.dark_db_connector(**config)
#db_name = 'YOUR_DB_NAME'
#try:
	#cursor.execute("CREATE DATABASE {}".format(db_name))
	#cursor.execute("CREATE TABLE TenableNessusVAScanner (
    #ID int NOT NULL AUTO_INCREMENT,
    #Plugin INT NOT NULL,
    #PluginName TEXT NOT NULL,
    #Family TEXT NOT NULL,
    #Severity VARCHAR(255) NOT NULL,
    #IPAddress VARCHAR(17) NOT NULL,
    #Protocol VARCHAR(6) NOT NULL,
    #Port VARCHAR(5) NOT NULL,
    #Exploit VARCHAR(255) NOT NULL,
    #Repository TEXT NOT NULL,
    #MACAddress VARCHAR(20) NOT NULL,
    #DNSName VARCHAR(255) NOT NULL,
    #NetBIOSName VARCHAR(255) NOT NULL,
    #PluginText LONGTEXT NOT NULL,
    #FirstDiscovered VARCHAR(255) NOT NULL,
    #LastObserved VARCHAR(255) NOT NULL,
    #ExploitFrameworks TEXT NOT NULL,
    #Synopsis TEXT NOT NULL,
    #Description LONGTEXT NOT NULL,
    #Solution LONGTEXT NOT NULL,
    #SeeAlso LONGTEXT NOT NULL,
    #CVE VARCHAR(255) NOT NULL,
    #VulnerabilityPublicationDate VARCHAR(255) NOT NULL,
    #ExploitEase TEXT NOT NULL,
    #PRIMARY KEY (ID)
#);")
#except mysql.Error as err:
#	print("Failed to create DB:{}".format(err))

#cursor.execute("SHOW DATABASES")
#print(cursor.fetchall())
#conn.close

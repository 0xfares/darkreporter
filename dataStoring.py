
import mysql.connector as mysql

class StoringData:
	def db_config(self, DB_USERNAME, DB_PASSWORD, DB_HOST_OR_IP, DB_NAME):
		configuration = {
				"user": DB_USERNAME,
				"password": DB_PASSWORD,
				"host": DB_HOST_OR_IP,
				"database": DB_NAME
		}
		return configuration

	def db_connector(self, CONFIGURATION_INFO):
		initalConnection = mysql.connect(**CONFIGURATION_INFO)
		cursor = initalConnection.cursor()
		

dsd = StoringData()
config = dsd.db_config('user','password','localhost','mysql')
connect = dsd.db_connector(config)
#connect = dsd.dark_db_connector(config)
#print(connect)
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

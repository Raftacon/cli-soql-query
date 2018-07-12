import os, sys, yaml, beatbox

env_list = ["main", "backup"]

msg = ("____________________________________________________________________________________________________"
	"\r\n\r\n"
	"Configure a config.yml in the same directory as this script, where eligible Salesforce buckets are\r\n"
	"configured under their appropriate lowercase environment headers (i.e. \'main\', \'backup\', etc.)\r\n"
	"and each has three key-value pairs to pull from: \'username\', \'password\', & \'token\'.\r\n"
	"\r\n"
	"To use, call the script with an environment followed by a quote-escaped SOQL query as the arg.\r\n"
	"\tExample: main \"SELECT id FROM Contact__c WHERE EmployeeId__c=1234567890\"\r\n"
	"\tResponse: [{\'type\': \'Contact__c\', \'Id\': \'a6o1f123456ZF3kBBG\'}]\r\n"
	"\r\n"
	"Alternatively, echo the contents out to file by piping the output using \'> \{filename\}\'.\r\n"
	"____________________________________________________________________________________________________")

if os.path.exists("config.yml"):
	with open("config.yml", 'r') as ymlconfig:
		cfg = yaml.load(ymlconfig)

	if len(sys.argv) > 1:
		if sys.argv[1] == "help":
			print msg
		elif len(sys.argv) == 3:
			env = sys.argv[1].lower()

			if env in env_list:
				username = cfg[env]['username']
				password = cfg[env]['password']
				token = cfg[env]['token']

				svc = beatbox.PythonClient()

				if env != "main":
					svc.serverUrl = 'https://test.salesforce.com/services/Soap/u/20.0'

				svc.login(username, password + token)

				print svc.query(sys.argv[2])
			else:
				print "Invalid environment provided, aborting."
				print "If you need further help, provide 'help' as a command-line argument for the script."
		else:
			print "No SOQL query specified, aborting."
			print "If you need further help, provide 'help' as a command-line argument for the script."
	else:
		print "No SOQL query specified, aborting."
		print "If you need further help, provide 'help' as a command-line argument for the script."
else:
	print "No config file could be found, aborting."
	print "If you need further help, provide 'help' as a command-line argument for the script."
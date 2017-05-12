#Before anything, I am still a beginner in programming. Any bad practices should be pointed out and constructive criticism is very much appreciated.

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("URL", help="The FULL URL for the wordpress 'root' without subdomain. Usually the URL of the website domain")
parser.add_argument("startID", help="Starting Admin ID to scan", type=int)
parser.add_argument("endID", help="Last Admin ID to scan", type=int)
args = parser.parse_args()

URL = args.URL
startID = args.startID
endID = args.endID

print("""
_ _ _ ___  ____ ___  _  _ _ _  _ 
| | | |__] |__| |  \ |\/| | |\ | by Marc owen
|_|_| |    |  | |__/ |  | | | \| https://github.com/marcowen20

[*] Use --help' for additional information""")
print("[*] URL: {0}\n[*]startID: {1}\n[*]endID: {2}\n".format(URL, startID, endID))
print("[*] ^C anytime to stop scanning")
admins = [] #To store found admin
for x in range(startID, endID + 1): #Range of ID to scan
	try:
		#Fix the URL  format to http://domain.com/?author=x or http://www.domain.com?author=x
		newURL = URL + "/?author={0}".format(x) 
		newURL2 = URL + "?author={0}".format(x) #If user already put / at the end of the URL

		r = requests.get(newURL)
		if r.url == newURL or r.url == newURL2: #Check if the request URL is the same as newURL. If they are the same, it indicates no redirection to author page. Author with ID X does not exist
			print("[*] Current scan ID: {0}\r".format(x)) #Do not print r.url on failure
			continue
		else: #The request URL is not the same as newURL. Redirection happens. Proceed to print the URL
			print("[+] Current scan ID: {0}    \t{1}".format(x, r.url)) #Print current URL
			admins.append("{0}\t: {1}".format(x, r.url)) #Save ID and URL of the admin page to be printed
	except KeyboardInterrupt:
		break #If process is interrupted, stop scanning
print("\n[+] Found admins:\nID\t: Admin URL")
for admin in admins:
	print("{0}".format(admin)) #Print all collected admin URLs
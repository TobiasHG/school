#import de relevante moduler.
import random
import sys
from ftplib import FTP

#liste med filer som bliver brugt.
coreFiles = ["acts.txt", "adjectives.txt", "jobs.txt", "things.txt"]

#funktion som kan download en fil fra ftp connection.
#return true når det lykkeds og false på fejl
def handleDownload(block, file):
	try:
		file.write(block)
		file.close()
	except:
		print("failed to write file!")

def downloadFile(fileName):
	try: 
		ftp.retrbinary('RETR '+fileName, lambda text: handleDownload(text, open(fileName, "wb")) ) #sender en kommando til serveren om at hente 'fileName' skriv/gem den som callback function
		return True
	except:
		print("failed to download file!")
		return False

def downloadCoreFiles():
	global ftp

	try:
		ftp = FTP('127.0.0.1') 
	except:
		print("connection failed to server!")
		return False

	try:
		ftp.login("geek")
	except:
		print("failed to login!")
		return False

	success = 0

	for fileName in coreFiles:
		if downloadFile(fileName):
			success=success+1

	try:
		ftp.quit()
	except:
		print("failed to quit ftp connection!")
		return False

	print("downloaded "+str(success)+"/"+str(len(coreFiles))+" files.")

def importList(file):
	try:
		filen = open(file, "r")
		output = filen.read().split()
		filen.close()
		return output
	except:
		return [""]

def getRandom(list):
	try:
		return list[random.randint(0, len(list)-1)]
	except:
		print("failed to get random from list")
		return [""]

def makeInsult():
	return "I don't want to talk to you no more you\n"+getRandom(adjectives)+" "+getRandom(jobs)+"!... I "+getRandom(acts)+" in your\ngeneral direction!\nYour "+getRandom(family)+" was a "+getRandom(jobs)+" and your\n"+getRandom(family)+" smelt of "+getRandom(things)+"!\n"

acts = importList("acts.txt")
adjectives = importList("adjectives.txt")
family = importList("family.txt")
jobs = importList("jobs.txt")
things = importList("things.txt")

while True:
	print("""
╔╗──╔═╗───╔╗─────────╔╗╔╗
╠╬═╦╣═╬╦╦╗║╚╗╔══╦═╗╔═╣╚╬╬═╦╦═╗
║║║║╠═║║║╚╣╔╣║║║║╬╚╣═╣║║║║║║╩╣
╚╩╩═╩═╩═╩═╩═╝╚╩╩╩══╩═╩╩╩╩╩═╩═╝

please choose an number!

1. random insult
2. download/update the core files
3. Exit
----------------------------------
""")

	selection = input()

	if selection == "1":
		print("you choosed to make an insult.\n")
		print(makeInsult())
	elif selection == "2":
		print("You choosed to download core files.\n")
		downloadCoreFiles()
	elif selection == "3":
		print("Exiting the program.\n")
		break
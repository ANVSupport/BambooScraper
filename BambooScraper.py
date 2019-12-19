
import sys
import os
from bs4 import BeautifulSoup
from datetime import datetime
import errno
import shutil
from pyfiglet import figlet_format
from termcolor import cprint
import re

def main():
	ChangedCounter = 0
	unChangedCounter = 0
	TimeStamp = datetime.now().strftime("%H-%M-%S")

	newFolderName = os.getcwd()+"/Renamed_Images_"+TimeStamp
	files_folder_name = "/"+str(sys.argv[1]).replace(".html" , "")
	oldSourceFolder = os.getcwd()+files_folder_name+"_files/"
	try:
		os.mkdir(newFolderName)
		print "\n===================================================================================================================="
		print "\t\t"+newFolderName+"Created"
		print "====================================================================================================================\n"
	except:
		print(printRed+"An Error has Occured Creating a new folder.. please try again"+printWhite)
		exit(1)

	try:
		copy_Folder(oldSourceFolder, newFolderName)
		print "\n===================================================================================================================="
		print "\t\t"+"Copied files..."
		print "====================================================================================================================\n"
	except:
		print(colors.printRed+"An Eror has Occured Copying the folder, Exiting..."+printWhite)
		exit(1)

	htmlFile = open(sys.argv[1], "r")
	soup = BeautifulSoup(htmlFile, "html.parser")
	cards = soup.find_all("div", {"class" : "EmployeeCardContainer__card"})
	for Employees in cards:
		cardSoup = BeautifulSoup(Employees.text, "html.parser") #
		name = clean_string(Employees.find_all("div", {"class" : "JobInfo__name"}))
		image = clean_string(Employees.find("img", {"class" : "ImgContainer__image"})['src'])
		old_path = os.path.join(newFolderName, str(image))
		new_path = os.path.join(newFolderName, str(name))
		new_path = new_path+".jpg"		
		try:
			os.rename(old_path,new_path)
			printString = str(old_path)+" Changed to "+str(new_path)
			print (colors.printGreen+printString+colors.printWhite)
			ChangedCounter=ChangedCounter+1
		except:
			printString = str(old_path)+" Not found, Skipping"
			print(colors.printRed+printString+colors.printWhite)
			unChangedCounter=unChangedCounter+1
	print(figlet_format('DONE!'))
	print("Files Created: "+colors.printGreen+str(ChangedCounter)+colors.printWhite)
	print("Files Unchanged: "+colors.printRed+str(unChangedCounter)+colors.printWhite)

def copy_Folder(src, dest):
	src_files = os.listdir(src)
	for file_name in src_files:
	    full_file_name = os.path.join(src, file_name)
	    if os.path.isfile(full_file_name):
	        shutil.copy(full_file_name, dest)
class colors():
	printRed = '\033[91m'
	printWhite = '\033[0m'
	printGreen = '\033[32m'

def clean_string(str):
	str = str(str)
	str = str.replace("Employees_files/", "")
	str = str.replace("[<div class=\"JobInfo__name\">","")
	str = str.replace("</div>]", "")
	return str

if __name__ == '__main__':
	main()

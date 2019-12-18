import sys
import os
from bs4 import BeautifulSoup
from datetime import datetime
import errno
import shutil

def main():
	TimeStamp = datetime.now().strftime("%H-%M-%S")
	newFolderName = os.getcwd()+"/Renamed_Images_"+TimeStamp
	files_folder_name = "/"+str(sys.argv[1]).replace(".*" , "")
	oldSourceFolder = os.getcwd()+files_folder_name+"_files/"
	os.mkdir(newFolderName)
	print "\n\n\n===================================================================================================================="
	print "\t\t"+newFolderName+"Created"
	print "====================================================================================================================\n\n\n"
	copy_Folder(oldSourceFolder, newFolderName)
	print "\n\n\n===================================================================================================================="
	print "\t\t"+"Copied files..."
	print "====================================================================================================================\n\n\n"
	htmlFile = open(sys.argv[1], "r")
	soup = BeautifulSoup(htmlFile, "lxml")
	cards = soup.find_all("div", {"class" : "EmployeeCardContainer__card"})
	for Employees in cards:
		cardSoup = BeautifulSoup(Employees.text, "lxml")
		name = str(Employees.find_all("div", {"class" : "JobInfo__name"}))
		image = str(Employees.find("img", {"class" : "ImgContainer__image"})['src'])
		name = clean_string(name)
		image = clean_string(image)
		old_path = os.path.join(newFolderName, str(image))
		new_path = os.path.join(newFolderName, str(name))
		new_path = new_path+".jpg"
		#print str(old_path)+" changed to "+str(new_path)
		# try:
		# 	os.rename(old_path,new_path)
		# except:
		# 	print str(old_path)+" Not found, Skipping"

def copy_Folder(src, dest):
	src_files = os.listdir(src)
	for file_name in src_files:
	    full_file_name = os.path.join(src, file_name)
	    if os.path.isfile(full_file_name):
	        shutil.copy(full_file_name, dest)


def clean_string(str):
	str = str.replace("Employees_files/", "")
	str = str.replace("[<div class=\"JobInfo__name\">","")
	str = str.replace("</div>]", "")
	return str


if __name__ == '__main__':
	main()
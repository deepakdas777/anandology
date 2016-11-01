"""Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments."""

from zipfile import *
import sys
def zip(x,y):
	f=ZipFile(x,'w')
	for n in y:
		f.write(n)
zip(sys.argv[1],sys.argv[2:])

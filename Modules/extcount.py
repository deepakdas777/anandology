"""Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension. """


import sys
import os
def extcount(x):
	ls=os.listdir(x)
	i=0
	d={}
	while i<len(ls):
		ls[i]=ls[i].split('.')
		if(len(ls[i])>1):
			d[ls[i][1]]=d.get(ls[i][1],0)+1
		i=i+1
	for keys,values in d.items():
		print keys,values
extcount(sys.argv[1])

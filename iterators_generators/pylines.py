"""Write a function to compute the total number of lines of code in all python files in the specified directory recursively."""

import os
import sys
rootdir=sys.argv[1]
def numlines(x):
	l=0
	for path,y,z in os.walk(rootdir):
		for i in z:
			if x in i:
				print os.path.join(path,i)," :- ",len(open(i).readlines())
				l+=len(open(i).readlines())
	#print "Total:- ",l
numlines(".py")

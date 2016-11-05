""" Write a function to compute the number of python files (.py extension) in a specified directory recursively."""
import os
import sys
rootdir = sys.argv[1]
def pyfiles(x):
	l=[]
        for path,dirn,filen in os.walk(rootdir):
                for i in filen:
			if x in i:
				l.append(os.path.join(path,i))
	print len(l)
pyfiles(".py")


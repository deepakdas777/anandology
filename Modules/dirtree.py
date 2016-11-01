"""Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree."""

import os
import sys
def tree(x,i=0):
	ls=os.listdir(x)
	k=0
	print ' '*i,x
	while k<len(ls):
		if '.' in ls[k]:
			print ' '*i,'|', '_'*2,ls[k]
		else:
			tree(x+'/'+ls[k],i+2)
		k=k+1
tree(sys.argv[1])

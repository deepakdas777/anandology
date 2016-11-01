"""Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html."""

import os
import urllib
import sys
def wget(x):
	r=urllib.urlopen(x)
	cont=r.read()
	name=x.split('/')
	n=name[-1]
	if n=='':
		n='index.html'
	f=open(n,'w')
	print "saving %s as %s" %(x,n)
	f.write(cont)
wget(sys.argv[1])

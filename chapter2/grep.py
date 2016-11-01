# Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string


import sys
def grep(x,s):
    i=0
    f=open(x).readlines()
    l=len(f)
    while i<l:
        p=s in f[i]
	if(p==True):
         f[i]= f[i].strip('\n')
	 print f[i]
	i=i+1
grep(sys.argv[1],sys.argv[2])

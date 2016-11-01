#Write a program to print each line of a file in reverse order.

import sys
def revline(x):
    i=0
    z=len(open(x).readlines())
    rev=[None]*z
    f=open(x)
    while(i<z):
         rev[i]=f.readline()
         rev[i]=rev[i].strip()
         print rev[i][::-1]
         i=i+1
    print '\n'	
z=sys.argv[1]
revline(z)

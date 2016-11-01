"""Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module."""

import sys
from inspect import *
def mypydoc(x):
        p=__import__(x)
        print 'DESCRIPTION:\n----------\n',p.__doc__,'\nFUNCTIONS\n---------\n'
        for y in dir(p):
                 print y
mypydoc(sys.argv[1])

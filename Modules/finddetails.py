"""Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs."""

import sys
import os
import time
def filedetail(x):
        ls=os.listdir(x)
        i=0
        d={}
        while i<len(ls):
                p=os.stat(os.getcwd()+'/'+ls[i])
		print ls[i],'\t'*2,time.ctime(p.st_mtime),'\t',p.st_size
                i=i+1
filedetail(os.getcwd())

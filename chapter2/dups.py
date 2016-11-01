
def dups(x):
    i=0
    y=[]
    l=[]	
    while(i<len(x)):
         f=x[i] in y
         if(f==False):
           y.append(x[i])
	 else:
	   l.append(x[i])
	 i+=1		
    return l
print dups([1, 2, 1, 3, 2, 5])


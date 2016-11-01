
def unique(x):
    i=0
    y=[]
    while(i<len(x)):
         f=x[i] in y
         if(f==False):
           y.append(x[i])
         i=i+1
    return y
print unique([1, 2, 1, 3, 2, 5])



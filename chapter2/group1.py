def group(x,l):
    i=0
    j=0
    p=0
    y=[[None]*l]*(len(x)/l)
    ys=[None]*l
    z=len(x)/l
    while(j<z):
          while(i<l):
	       print j,i,p
               ys.append.pop()
           #    y[j][i]=x[p]
               i=i+1
               p=p+1
          y[j]=ys
          i=0
          j=j+1
    return y
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

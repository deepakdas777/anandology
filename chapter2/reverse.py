def reverse(l):
	n=len(l)
	i=n-1
	x=[]
	while i>=0:
		x.append(l[i])
		i-=1
	return x
print 'reverse=',reverse([1,2,3,4])

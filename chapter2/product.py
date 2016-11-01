def product(l):
	product=1
	for i in l:
		product=product*i
	return product
print 'product=' ,product([1,2,3])

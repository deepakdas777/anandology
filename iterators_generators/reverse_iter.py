""" Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. """

class reverse_iter(object):
	def __init__(self,n):
		self.i=len(n)-1
		self.n=n
	def __iter__(self):
		return self
	def next(self):
		if self.i>=0:
			i=self.i
			self.i-=1
			return self.n[i]
		else:
			raise StopIteration()
r=reverse_iter([1,2,3,4,5])
while True:
	print r.next()


def lensort(a):
     a.sort(key=lambda x:len(x))
     return a
print lensort(["q","qwqwqw","qw"])
print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])


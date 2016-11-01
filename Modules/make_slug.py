"""Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end of the slug."""

import string
def make_slug(x):
	s=''
	flag=0
	for y in x:
		if y in string.ascii_letters:
			s=s+y
			flag=1
		elif y in string.punctuation+' ' and flag==1:
			s=s+'-'
			flag=0
	if s[len(s)-1] in string.punctuation+' ':
		s=s.strip(s[len(s)-1])
	print s
make_slug("  -   --hello- +    world--   +")

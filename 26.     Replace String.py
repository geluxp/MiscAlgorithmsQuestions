# 26.     Replace String
# Froma given string, replace all instances of 
# 'a' with 'one' and 'A' with 'ONE'.
# Example Input: " A boy is playing in a garden"
# Example Output: " ONE boy is playing in onegarden"
# -- Not that 'A' and 'a' 
# are to be replaced only when theyare single characters, not as part of another word.

def replaced(s):
	ss=s.split()
	print ss
	for i in range(len(ss)):
		
		if ss[i]=='a':
			
			ss[i]='one'
		elif ss[i]=='A':
			ss[i]='ONE'

	return ' '.join(ss)


s='A boy is playing in a garden'
print replaced(s)

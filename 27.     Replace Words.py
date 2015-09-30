#27.     Replace Words
#Given a string.
#Replace the words whose length>=4and is even,
#with a space between the two equal halves 
#of the word. Consideronly alphabets for
#finding the evenness of the word 
#I/P "A person can't walk in this street" .
#From 1point 3acres bbs
#O/P "A per son ca n't wa lk in th is str eet"


def replace(s):
    ss=s.split(' ')
    result=[]
    
    for i in range(len(ss)):
        if len(ss[i])>=4 and len(filter(str.isalpha, ss[i]))%2==0:
        	temp=list(ss[i])
        	print temp
        	temp.insert(len(temp)/2, ' ')
        	print temp
        	ss[i]=''.join(temp)
        	print ss[i]
    return ' '.join(ss)
    
    

    
s="A person can't walk in this street"
print replace(s)

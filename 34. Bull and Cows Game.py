#34.     Bull and Cows Game
#There’s a word guessing game. One personthink a word,
#and the other one guess a word, both words have the
#same length.The person should return the number
#of bulls and cows for the guessing.
#Bullsrepresent the number of same characters in 
#the same spots, whereas cowsrepresent the number 
#of characters guessed right but in the wrong spots. 
#Writea program with two input strings, return the
#number of bulls and cows.


def bullcowsgame(think,guess):
    #intputs are two strings.
    think=list(think)
    guess=list(guess)
    if len(think)!=len(guess):
        return 
    bulls=0
    totals=0
    i=0
    j=0
    while i<len(think):
        if think[i]==guess[i]:
            bulls +=1
        i+=1
    
    dict={}
    
    for i in range(len(think)):
        if think[i] not in dict:
            dict[think[i]]=1
        else:
            dict[think[i]] +=1
    
    
    for j in range(len(guess)):
        if guess[j] in dict and dict[guess[j]]>0:
            dict[guess[j]] -=1
            totals +=1
         
    cows=totals-bulls
    print "totals=" +str(totals)
    print "cows=" +str(cows)
    print "bulls=" +str(bulls)

think='applelala'
guess='bananlale'

bullcowsgame(think,guess)

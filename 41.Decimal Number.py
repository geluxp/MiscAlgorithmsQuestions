#41.    Decimal Number
#Let the user enter a decimal number. 
#Therange allowed is 0.0001 to 0.9999. 
#Only four decimal places are allowed. 
#Theoutput should be an irreducible fract
#E.g.: If the user enters 0.35,the irreducible fraction will be 7/20.



a=0.35
b=0.38
def decimalNumber(a):
    base=1000
    a=a*base
    
    number_2=0
    number_5=0
    
    while True:
        if a%5==0:
            a /= 5
            number_5 +=1
        elif a%2==0:
            a /= 2
            number_2 +=1
           
        else:
            break
    
    deminator=a
    denominator=1000/((5**number_5)*(2**number_2))
    
    
    print str(int(deminator))+'/'+ str(int(denominator))
    
decimalNumber(a)
decimalNumber(b)

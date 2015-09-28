#48.     Octal and Decimal Palindrome
#
#The decimal and octal values of 
#some numbersare both palindromes sometimes. 
#Find such numbers within a given range.



def octdemipalindrome(a): ##a is a decimal int
    
    b=oct(a)
    decimal_number=list(str(a))
    oct_number=list(str(b))
    
    if decimal_number==decimal_number[::-1] and oct_number==oct_number[::-1]:
        return True

    
def main(froma,to):
    for i in range(froma,to+1):
        if octdemipalindrome(i):
            print i
     
    

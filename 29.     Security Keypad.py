#29.     Security Keypad
#There is a security keypad at the entrance of
#a building. It has 9 numbers 1 - 9 in a 3x3 matrix format. 
#
#1 2 3 
#4 5 6 
#7 8 9 
#The security has decided to allow one digit 
#error for a person but that digitshould be
#horizontal or vertical. Example: 
#for 5 the user is allowed to enter2, 4, 6, 8 
#or for 4 the user is allowed to enter 1, 5, 7. 
#IF the security codeto enter is 1478
#and if the user enters 1178 he should be allowed. 
#Write afunction to take security code from the
#user and print out if he should beallowed or not.
def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1 

def sucuritykeypad(realcode,userinput):
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    realcode=list(str(realcode))
    userinput=list(str(userinput))
    
    while len(userinput)>1:
        a=userinput.pop()
        b=realcode.pop()
        if a==b:
            continue
        else:
            break
    print type(a), a
    print type(b),b
    index_a=list(find(matrix,int(a)))
    index_b=list(find(matrix,int(b)))
    print index_a
    print index_b
    
    if (abs(index_a[0]-index_b[0])==1 and index_a[1]==index_b[1] )or ( index_a[0]==index_b[0] and abs(index_a[1]-index_b[1])==1):
        return True
    else:
        return False
realcode=1634
userinput=1234
print sucuritykeypad(realcode,userinput)        
    
    

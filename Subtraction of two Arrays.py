#37.     Subtraction of two Arrays
#Suppose you want to do the subtraction of twonumbers. Each digit of the numbers is divided and put in an array.
#Like A=[1,2, 3, 4, 5], B=[4, 5, 3, 5].
#You should output an array C=[7, 8, 1, 0].Remember that your machine can’t hand numbers larger than 20.


A=[1,2, 3, 4, 5,5]
B=[9,4, 5, 3, 5]

C=[]

length=max(len(A),len(B))

while len(A)>len(B):
    B.insert(0,0)



for i in range(length):
    C.append(A[i]+B[i])

for i in range(length)[::-1]:

    if C[i]>=10:
        C[i]=C[i]-10
        if i!=0:
            C[i-1] += 1
        else:
            C.insert(0,1)


print C
         

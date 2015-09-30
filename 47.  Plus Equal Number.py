#47.     Plus Equal Number
#Given a number find whether the digits 
#in thenumber can be used to form an equation with + and '='.
#That is if the number is123, we can have a equation of 1+2=3. 
#But even the number 17512 also forms theequation 12+5=17.

def check(num1,num2,num3):
	count=0
	n1=int(num1)
	n2=int(num2)
	n3=int(num3)

	if (n1+n2==n3):
		return 1
	elif (n2+n3==n1):
		return 2
	elif (n1+n3==n2):
		return 3
	else:
		return 0

def main(number):
	str_num=str(number)
	n=len(str_num)-2
	print str_num
	print n
	for i in range(n):
		for j in range(i+1,n+1):# 1 2 3 4 5
			num1=str_num[0:i+1]
			num2=str_num[i+1:j+1]
			num3=str_num[j+1:len(str_num)]
			temp=check(num1,num2,num3)
			if temp==0:
				continue
			else:
				print "we have a solution"+num1+" and "+num2+ " and "+num3





a=17512
b=542826
main(a)
main(b)
c=54504
main(c)

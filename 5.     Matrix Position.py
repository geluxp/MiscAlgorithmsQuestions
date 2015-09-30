# 25.     Matrix Position
# Given an NxN matrix with unique integers :Find \
# and print positions of all numbers such that it is the biggest in 
# its row andalso the smallest in its column . e.g. : In 3 x 3 with elements 
# 1 2 3 
# 4 5 6 
# 7 8 9 
# the number is 3 and position (1,3)

def matrixposition(matrix):
	semi_result1=[]
	semi_result2=[]
	for i in range(len(matrix)):
		max=matrix[i][0]
		for j in range(len(matrix[0])):
			if matrix[i][j]>=max:
				max=matrix[i][j]
				semi_result1.append((i,j))

	for i in range(len(matrix[0])):
		min=matrix[0][i]
		for i in range(len(matrix)):
			if matrix[i][j]<=min:
				min=matrix[i][j]
				semi_result2.append((i,j))

	result=set(semi_result1) & set(semi_result2)
	print result
	result=list(result)
	result= [(x+1,y+1) for (x,y) in result]
	return result

	


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print matrixposition(matrix)

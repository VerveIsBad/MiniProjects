a = [[1,3,7],
	[0,8,3],
	[5,2,0]]

b = [[3,5,1],
	[2,6,0],
	[1,4,2]]

def multiply_matrix(matrix_a, matrix_b):
	result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]  
	# iterate through rows of matrix_a  
	for i in range(len(matrix_a)):  
	   for j in range(len(matrix_b[0])):  
	       for k in range(len(matrix_b)):  
	           result[i][j] += matrix_a[i][k] * matrix_b[k][j]  
	
	for line in result:  
	   print(' '.join(map(str, line)))  

multiply_matrix(a,b)
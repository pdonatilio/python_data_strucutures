#Vector and Matrices in Python
#Vector: a unidimensional matrix
#Matrix: Vector of Vectors (multidimensional)

#example of matrix
matrix = [[10,20,30,40],
		  [50,60,70,80],
		  [90,100,110,120],]

print(matrix[1][2])

#example of vector
vector = [10,20,30,40,50]

#printing the last and the first vector itens in this order
print(str(vector[-1])," - ",str(vector[0]))

#matrix to imput the notes of students
matrix = [['Paulo',8,7,6],
		  ['Laerson',4.5,9,10],
		  ['Alexandre',6,6,8],]

print(matrix)

for row in matrix:
	for col in row:
		print(str(col) + '\t', end = ' ') 
	print('')
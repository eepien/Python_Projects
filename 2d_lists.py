#matrices are very useful in data science.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   # this is a 2d list or matrice: each element in the list is another list
print (matrix[0])                            # Returns [1, 2, 3], first row elements
print(matrix[0][0])                          # Returns 1
print(matrix[0][1])                          # Returns 2

matrix[0][1] = 20                            # modifies first row, second element from 2 --> 20
print(matrix[0][1])                          # now returns 20

for row in matrix:                           # Iterates all 3 rows [1, 2, 3], [4, 5, 6], [7, 8, 9]
    for item in row:                         # Iterates through each row
        print(item)                          #Prints item in each row.

#VD 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("MatranGoc:")
for row in matrix:
    print(row)
print("Matranhoanvi:")
for row in transposed:
   print(row)

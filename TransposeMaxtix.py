#VD 1
def TrasposeMatrix(matrix):
    #if not matrix or not matrix[0]:
        #return []
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transposed_matrix = TrasposeMatrix(matrix)
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("Transposed Matrix:")
    for row in transposed_matrix:
        print(row)

#VD2
def TransposeMatrix2(matrix2):
    if not matrix2 or not matrix2[0]:
      return []
    trapspose2 = [[matrix2[j][i] for j in range(len(matrix2))] for i in range(len(matrix2[0]))]
    return trapspose2
if __name__ == "__main__":
    matrix2 = [
        [1 , 2 , 3],
        [4 , 5 , 6]
    ]
    transpose2 = TransposeMatrix2(matrix2)
    print("Old: ")
    for row in matrix2:
      print(row)
    print("New: ")
    for row in transpose2:
      print(row)

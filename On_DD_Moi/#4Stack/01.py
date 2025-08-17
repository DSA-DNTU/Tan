def find_celebrity(matrix):
    n = len(matrix)
    indegree = [0] * n
    outdegree = [0] * n

    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1:
                outdegree[i] += 1
                indegree[j] += 1

    for i in range(n):
        if indegree[i] == n -1 and outdegree [i] == 0:
            return i
    return -1

print(find_celebrity([[1, 1, 0], [0, 1, 0], [0, 1, 1]]))
print(find_celebrity([[1, 1], [1, 1]]))
print(find_celebrity([[1]]))

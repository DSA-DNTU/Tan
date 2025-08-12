matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m, n = len(matrix), len(matrix[0])
pos = int(input("Nhap k: "))
flat = [x for row in matrix for x in row]
flat = flat[-pos:] + flat[:-pos]
result = [flat[i * n : (i + 1) * n] for i in range(m)]
for row in result:
  print(row)

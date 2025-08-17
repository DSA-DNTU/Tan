def delete_node_n(array, k):
  count = 1
  result = []
  for num in array:
    if count % k != 0:
      result.append(num)
    count += 1
  return result

print(delete_node_n([1, 2, 3, 4, 5], 2))
print(delete_node_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

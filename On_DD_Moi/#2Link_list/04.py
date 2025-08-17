def sum_sort_list(array0, array1, array2):
  result = array0 + array1 + array2
  result.sort()
  return result

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3 = [0, 9, 10, 11]
print(sum_sort_list(arr1, arr2, arr3))

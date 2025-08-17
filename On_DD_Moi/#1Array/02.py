def find_missing_ranges(arr, lower, upper):
  res = []
  prev = lower - 1
  for num in arr + [upper + 1]:
    if num - prev > 1:
      res.append([prev + 1, num - 1])
    prev = num
  return res

print(find_missing_ranges([14, 15, 20, 30, 31, 45], 10, 50))


#print(find_missing_ranges([-48, -10, -6, -4, 0, 4, 17], -54, 17))

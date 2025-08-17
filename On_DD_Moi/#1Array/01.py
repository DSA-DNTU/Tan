def seccond_largest(array):
  first = seccond = -1
  for num in array:
    if num > first:
      seccond = first
      first = num
    elif num > seccond and num != first:
      seccond = num
    return seccond

#TH1
print(seccond_largest([20, 10, 30, 40, 50]))

#TH2
print(seccond_largest([20, 10, 10]))

def test_string_binary(string):
  for char in string:
    if char not in ('0', '1'):
      return False
  return True

str = "0110100"
print(test_string_binary(str))

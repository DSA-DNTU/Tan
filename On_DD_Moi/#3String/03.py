def check_char_double(string):
    str = set()
    for char in string:
        if char in str:
            return char
        str.add(char)
    return -1

print(check_char_double("geeksforgeeks"))
print(check_char_double("hello geeks"))
print(check_char_double("abc"))


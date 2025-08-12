def linearSearch(a, t):
    for i in range(len(a)):
        if t == a[i]:
            return i
    return -1

a1 = [5, 2, 9, 1, 7]
t1 = 9
n = linearSearch(a1, t1)
print(n)
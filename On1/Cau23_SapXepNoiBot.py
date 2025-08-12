def bubbleSort(a):
    n = len(a)
    for i in range(n):
        sw = False
        for j in range(0, n - i -1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                sw = True
        if not sw:
            break

a = [4, 2, 7, 1, 3]
print(a)
bubbleSort(a)
print(a)
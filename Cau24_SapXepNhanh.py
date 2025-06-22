def quickSort(a):
    def sort(l , r):
        if l >= r:
            return
        p = a[r]
        i = l
        for j in range(l, r):
            if a[j] < p:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[r] = a[r], a[i]
        sort(l, i - 1) 
        sort(i + 1, r)
    sort(0, len(a) - 1)

n = int(input("Nhap so phan tu: "))
a = []
for i in range(n):
    x = int(input("Nhap phan tu thu {}: ".format(i + 1)))
    a.append(x)
rs = quickSort(a)
print("Mang da sap xep: ", a)
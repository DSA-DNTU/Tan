def insert (a, l, p, x): # a la array, l la length, p la pos vi tri chen, x la so can chen
    m = len(a)
    #if l >= m or p < 0 or p > l:
        #return l
    for i in range (l, p, -1):
        a[i] = a[i - 1]
    a[p] = x
    return l + 1

a = [1, 2, 3, 0, 0]
print(a, "Số phần tử hiện tại: ", 3)
l = 3
vt = 4 #int(input("Nhập vị trí cần chèn: "))
gt = 9 #int(input("Nhập giá trị cần chèn: "))
l = insert(a, l, vt, gt)
print(a , l)

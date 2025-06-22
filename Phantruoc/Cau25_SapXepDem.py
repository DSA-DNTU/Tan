def countingSort(a, k):
    c = [0] * (k + 1)
    for n in a:
        c[n] += 1
    idx = 0
    for i in range(k + 1):
        while c[i] > 0:
            a[idx] = i
            idx += 1
            c[i] -= 1


n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)
    if x > n:
        print("Phần tử vượt quá k, vui lòng nhập lại.")
        break
k = max(a)
if n == k:
    countingSort(a, k)
    print("Mảng đã sắp xếp:", a)
else:
    print()

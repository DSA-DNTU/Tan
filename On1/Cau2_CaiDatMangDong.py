class DynamicArray:
    def __init__(s): #s = self, c la` capacity, l la` length, d la` data, e la` element
        s.c = 2 
        s.l = 0
        s.d = [0] * s.c

    def add(s, e):
        if s.l == s.c:
            s.resize()
        s.d[s.l] = e
        s.l += 1

    def resize(s): #nc la` new capacity, nd la` new data
        nc = s.c * 2
        nd = [0] * nc
        for i in range(s.l):
            nd[i] = s.d[i]
        s.d = nd
        s.c = nc

    def get_array(s):
        return s.d[:s.l]
    
    def get_capacity(s):
        return s.c
    
    
arr = DynamicArray() #ip = input
while True:
    ip = int(input("Nhập giá trị: ")) 
    arr.add(ip)
    print("Mảng hiện tại:", arr.get_array())         
    print("Dung lượng bên trong:", arr.get_capacity())
    if ip == "-1":
        break
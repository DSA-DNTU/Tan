class Node:
    def __init__(s, d): # s self, d data
        s.d = d
        s.next = None

def addTail(h, d): #ham yeu ca`u cua de. h head, d data, n_n new_node, c = current
    n_n = Node(d)
    if h is None:
        h = n_n
        return h
    c = h
    while c.next is not None:
        c = c.next
    c.next = n_n
    return h

def print_list(h):
    c = h
    e = []
    while c:
        e.append(str(c.d))
        c = c.next
    e.append("null")
    print(" -> ".join(e))

n = int(input("Nhập số lượng phần tử trong danh sách: "))
i = 0
head1 = None
temp = None
while i < n: 
    c = Node(int(input("Nhập phần tử mẫu: ")))
    if head1 is None:
        head1 = c
        temp = c
    else:
        temp.next = c
        temp = c
    i += 1
    
print("Danh sách ban đầu:", end=" ")
print_list(head1)
data_to_add1 = int(input("Nhập dữ liệu cần thêm vào cuối danh sách: "))
head1 = addTail(head1, data_to_add1)
print("Danh sách mới:", end=" ")
print_list(head1)
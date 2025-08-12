class Node:
    def __init__(s, d): # s self, d data
        s.d = d
        s.next = None
        s.pre = None

def insertAfter(n_p, d): #ham yeu ca`u cua de. h head, d data, n_n new_node, c = current
    if n_p is None:
        return n_p
    n_n = Node(d)
    n_n.next = n_p.next
    n_n.pre = n_p
    n_p.next = n_n
    if n_n.next is not None:
        n_n.next.pre = n_n

def link_nodes(v):
    if not v: 
        return None
    h = Node(v[0])
    c = h
    for va in v[1:]:
        n = Node(va)
        c.next, n.pre = n, c
        c = n 
    return h

def find_node(h , v):
    c = h
    while c and c.d != v:
        c = c.next
    return c

def print_list(h):
    e = []
    c = h
    while c:
        e.append(str(c.d))
        c = c.next
    print("Danh sách: " + " <-> ".join(e))

node_bf = link_nodes([1, 2, 4])
print_list(node_bf)
vt = int(input("Nhập vị trí cần chèn: "))
node_aft = find_node(node_bf, vt)
gt = int(input("Nhập giá trị cần chèn: "))
node_ins = gt
insertAfter(node_aft, node_ins)
print_list(node_bf)
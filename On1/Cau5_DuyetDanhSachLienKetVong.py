class Node:  #rs = result
    def __init__(s, d):
        s.d = d
        s.next = None
def traverseCircularList(h):
    if not h:
        return []
    rs = []
    c = h 
    while True:
        rs.append(c.d)
        c = c.next
        if c == h:
            break
    return rs

mot = int(input("Nhập số đầu tiên: "))
hai = int(input("Nhập số thứ hai: "))  
ba = int(input("Nhập số thứ ba: "))
if __name__ == "__main__":
    node1 = Node(mot)
    node2 = Node(hai)
    node3 = Node(ba)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    output_node1 = traverseCircularList(node1)
    print(*output_node1)
    output_node2 = traverseCircularList(node2)
    print(*output_node2)
    output_node3 = traverseCircularList(node3)
    print(*output_node3)
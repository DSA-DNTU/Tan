class Queue:
    def __init__(s):
        s.it = []
    def enqueue(s, it):
        s.it.append(it)
    def dequeue(s):
        if s.isEmpty():
            raise IndexError("Queue empty")
        return s.it.pop(0)
    def peek(s):
        if s.isEmpty():
            raise IndexError("Queue empty")
        return s.it[0]
    def isEmpty(s):
        return len(s.it) == 0
    def __str__(s):
        return str(s.it)

sl = int(input("Nhập số lượng Item: "))
q = Queue()
for i in range(sl):
    n = int(input("Nhập giá trị Item: "))
    q.enqueue(n)
first_item = q.dequeue()
next_item = q.peek()

print("Item đầu tiên:", first_item)
print("Item tiếp theo:", next_item)
print("Danh sách Item:", q)

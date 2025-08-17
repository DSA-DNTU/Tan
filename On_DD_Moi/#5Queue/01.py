from collections import deque

q1 = deque()
q2 = deque()

def push(x):
    q2.append(x)
    while q1:
        q2.append(q1.popleft())
    while q2:
        q1.append(q2.popleft())

def pop():
    if q1:
        return q1.popleft()
    return None

push(1)
push(2)
push(3)
print(pop())
print(pop())
push(4)
print(pop())

stack = []

def push(x):
  if not stack:
    min_now = x
  else:
    min_now = min(x, stack[-1][1])
  stack.append((x, min_now))

def pop():
    if stack:
        return stack.pop()[0]

def top():
    if stack:
        return stack[-1][0]

def getMin():
    if stack:
        return stack[-1][1]
print(stack)
push(3)
print(stack)
push(5)
print(stack)
push(2)
print(stack)
print(getMin())
print(stack)
pop()
print(stack)
print(getMin())
print(stack)

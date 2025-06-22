def evaluate_postfix(ex):
    stack = []
    for token in ex.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
    return stack.pop()

expr = input("Nhập biểu thức: ")
rs = evaluate_postfix(expr)
print("Kết quả:", rs)
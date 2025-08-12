def factorial_stack(n):
    if n == 0 or n == 1:
        return 1
    st = [] #st = stack
    for i in range(2, n + 1):
        st.append(i)
    result = 1
    while st:
        result *= st.pop()
    return result

n = int(input("Nhập n: "))
rs = factorial_stack(n)
print("Kết quả: ", rs)
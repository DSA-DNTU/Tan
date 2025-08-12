def LIFO(ex):
    s = []
    t = {"(":")","[":"]","{":"}"}
    m = set(["(","[","{"])
    d = set([")","]","}"])
    for c in ex:
        if c in m:
            s.append(c)
        elif c in d:
            if not s:
                return "Invalid"
            e = s.pop()
            if t[e] != c:
                return "Invalid"
    if not s:
        return "Valid"
    else:
        return "Invalid"
    
print("input expression: ")
c = LIFO(input())
print(c)
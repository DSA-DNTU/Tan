from collections import deque

def connectLevels(root):
    if not root:
        return

    q = deque()
    q.append(root)

    while q:
        size = len(q)
        prev = None

        for i in range(size):
            node = q.popleft()

            if prev:
                prev["nextRight"] = node
            prev = node

            if node["left"]:
                q.append(node["left"])
            if node["right"]:
                q.append(node["right"])

        # Nút ngoài cùng bên phải
        node["nextRight"] = None

# Ví dụ
root = {
    "data": 1,
    "left": {
        "data": 2,
        "left": {"data": 4, "left": None, "right": None},
        "right": {"data": 5, "left": None, "right": None}
    },
    "right": {
        "data": 3,
        "left": None,
        "right": {"data": 6, "left": None, "right": None}
    }
}

connectLevels(root)
print("nextRight của nút 2:", root["left"]["nextRight"]["data"])  # Kết quả: 3

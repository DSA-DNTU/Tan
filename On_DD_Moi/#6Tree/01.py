def inorder(root):
    if root is None:
        return
    inorder(root["left"])
    print(root["data"], end=" ")
    inorder(root["right"])

# Ví dụ
root = {
    "data": 1,
    "left": {"data": 2, "left": None, "right": None},
    "right": {"data": 3, "left": None, "right": None}
}

print("Inorder traversal:", end=" ")
inorder(root)  # Kết quả: 2 1 3

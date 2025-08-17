def maxDepth(root):
    if root is None:
        return -1   # hoặc 0 nếu tính theo số nút
    left = maxDepth(root["left"])
    right = maxDepth(root["right"])
    return max(left, right) + 1

# Ví dụ
root = {
    "data": 12,
    "left": {
        "data": 8,
        "left": {"data": 5, "left": None, "right": None},
        "right": None
    },
    "right": None
}

print("Độ sâu tối đa:", maxDepth(root))  # Kết quả: 2

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        arr.sort()
        return arr
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr

# Ví dụ sử dụng:
print(next_permutation([2, 4, 1, 7, 5, 0]))  # Output: [2, 4, 5, 0, 1, 7]
print(next_permutation([3, 2, 1]))           # Output: [1, 2, 3]
print(next_permutation([1, 3, 5, 4, 2]))     # Output: [1, 4, 2, 3, 5]

def trap_rain_water(arr):
    n = len(arr)
    if n == 0:
        return 0
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i])
    right_max[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])
    water = 0
    for i in range(n):
        water += max(0, min(left_max[i], right_max[i]) - arr[i])
    return water

# Ví dụ sử dụng:
print(trap_rain_water([3, 0, 1, 0, 4, 0, 2]))  # Output: 10
print(trap_rain_water([3, 0, 2, 0, 4]))        # Output: 7
print(trap_rain_water([1, 2, 3, 4]))           # Output: 0

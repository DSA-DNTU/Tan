def reverse_couple_arr(array):
    result = []
    n = len(array)
    count = 0
    while count < n:
        if count + 1 < n:
            result.append(array[count + 1])
            result.append(array[count])
            count += 2
        else:
            result.append(array[count])
            count += 1
    return result


# arr = [1, 2, 3, 4, 5, 6]
arr = [1, 2, 3, 4, 5]
print(reverse_couple_arr(arr))

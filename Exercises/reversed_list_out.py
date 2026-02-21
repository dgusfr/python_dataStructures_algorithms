array = [1, 2, 3, 4, 5]


def reverse_list_out(arr):
    n = len(arr)
    new_array = []

    for i in range(n - 1, -1, -1):
        new_array.append(arr[i])
    return new_array


print(reverse_list_out(array))

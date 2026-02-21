array = [1, 2, 3, 4, 5]


def reverse_list(arr):
    n = len(arr)
    limit = n // 2
    for i in range(limit):
        aux = arr[i]
        arr[i] = arr[n - 1 - i]
        arr[n - 1 - i] = aux
    return arr


print(reverse_list(array))

array = [1, 2, 8, 4, 5, 6, 7, 8, 9, 10]


def duplicated_itens(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


print(duplicated_itens(array))

array = [64, 34, 25, 12, 22, 11, 90, 5]


def insertion_sort(arr):
    n = len(array)

    for i in range(1, n):
        insert_index = array[i]
        j = i - 1

        for j in range(j, -1, -1):
            if array[j] > insert_index:
                array[j + 1] = array[j]
                j -= 1

        array[j + 1] = insert_index

    return array


print(insertion_sort(array))

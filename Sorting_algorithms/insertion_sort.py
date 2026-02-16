my_array = [64, 34, 25, 12, 22, 11, 90, 5]


def insertion_sort(arr):
    n = len(my_array)

    for i in range(1, n):
        insert_index = arr[i]
        j = i - 1

        for j in range(i - 1, -1, -1):
            if my_array[j] > insert_index:
                my_array[j + 1] = my_array[j]
            else:
                break
        my_array[j + 1] = insert_index

    print("Sorted array:", my_array)

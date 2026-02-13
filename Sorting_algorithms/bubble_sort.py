lista = [7, 12, 9, 11, 3]


def bubble_sort(lista):
    n = len(lista)

    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista


print(bubble_sort(lista))

def linear_search(lista: list, target):
    for element in lista:
        if element==target:
            return lista.index(element)
    return -1

lista = [2, 33, 47, 59, 62, 79, 80, 93, 100]
index = linear_search(lista, 79)
print(index)
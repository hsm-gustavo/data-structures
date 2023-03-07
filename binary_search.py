def binary_search(lista: list, target):
    left = 0
    right = len(lista)-1

    while left <= right:
        mid = (left + right)//2

        if lista[mid] == target:
            return mid
        elif lista[mid]<target:
            left=mid+1
        elif lista[mid]>target:
            right=mid-1
        else:
            left-=1
            right+=1
    return -1

lista = [2, 33, 47, 59, 62, 79, 80, 93, 100]
index = binary_search(lista, 100)
print(index)
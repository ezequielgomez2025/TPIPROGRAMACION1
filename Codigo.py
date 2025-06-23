ids = [34, 7, 23, 32, 5, 62]   # lista desordenada de IDs

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:              # compara pares adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # los intercambia
    return arr

bubble_sort(ids)
print("IDs ordenados:", ids)      #  [5, 7, 23, 32, 34, 62]

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:          # encontrado
            return mid
        if arr[mid] < target:           # buscar en la mitad derecha
            low = mid + 1
        else:                           # buscar en la mitad izquierda
            high = mid - 1
    return -1                           # no encontrado

target = 23
pos = binary_search(ids, target)
print("Posición encontrada:", pos)   #  2

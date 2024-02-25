def convertir_a_binario(arr, x, inicio=0, fin=None):
    if fin is None:
        fin = len(arr) - 1

    while inicio <= fin:
        mid = (inicio + fin) // 2
        if arr[mid] == x:
            print("Número Encontrado")
            return mid
        elif arr[mid] < x:
            inicio = mid + 1
        else:
            fin = mid - 1

    print("Número no encontrado")
    return -1  
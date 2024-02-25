def calcular_raiz_cuadrada(n,dato=1):
    if dato * dato ==n:
        return dato
    elif dato * dato < n:
        return calcular_raiz_cuadrada(n,dato +1)
    else:
        residuo = n - (dato -  1)**2
        return dato-1,residuo
 
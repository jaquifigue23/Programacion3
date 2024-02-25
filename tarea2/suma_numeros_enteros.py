def suma_numeros_enteros(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_numeros_enteros(numero - 1)


numero_entero = 5
resultado = suma_numeros_enteros(numero_entero)
print(f"La suma de todos los números enteros desde 0 hasta {numero_entero} es: {resultado}")

def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

numero = 12345
print("El número de dígitos en", numero, "es:", contar_digitos(numero))

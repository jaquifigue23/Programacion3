def convertir_a_decimal(romano):
    if not romano:
        return 0

    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    primer_valor = valores[romano[0]]

    if len(romano) == 1:
        return primer_valor

    segundo_valor = valores[romano[1]]

    if segundo_valor > primer_valor:
        return segundo_valor - primer_valor + convertir_a_decimal(romano[2:])

    else:
        return primer_valor + convertir_a_decimal(romano[1:])


numero_romano = "XXIV"
print(f"El número romano {numero_romano} es equivalente a {convertir_a_decimal(numero_romano)} en decimal.")

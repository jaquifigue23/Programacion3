def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

def menu():
    print("Menú:")
    print("1. Convertir a Binario")
    print("2. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            numero_decimal = int(input("Ingrese un número decimal: "))
            binario = decimal_a_binario(numero_decimal)
            print(f"El número decimal {numero_decimal} en binario es: {binario}")
        elif opcion == "2":
            print("¡Salio del Programa!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

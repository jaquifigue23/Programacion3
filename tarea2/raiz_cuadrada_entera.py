import calcular_raiz_cuadrada 
    
def raiz_cuadrada_entera(numero):
    if numero < 0:
         raise ValueError("No se puede calcular la rapiz cuadrada entera de un numero negativo.")
    elif numero == 0:
        return 0
    else: 
        return calcular_raiz_cuadrada.calcular_raiz_cuadrada(numero)
    
numero = int(input("ingrese un numero: "))
raiz_entera,residuo = raiz_cuadrada_entera(numero)
print(f"la raiz cuadrada entera de {numero} es:{raiz_entera} con un residuo de {residuo}")            
    
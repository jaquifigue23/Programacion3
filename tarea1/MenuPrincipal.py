import NodoDoblementeEnlazada
import ListaDoblementeEnlazada

def print_menu():
    print("1. Insertar al Principio")
    print("2. Insertar al Final")
    print("3. Eliminar por Valor")
    print("4. Mostar Lista")
    print("5. Salir")

def main():
    nuevaLista = ListaDoblementeEnlazada.ListaDoblementeEnlazada()
    while True:
        print_menu()
        choice = input("Ingresar opcion (1-5): ")
        
        if choice == "1":
            nombre = input("Ingrese Nombre: ")
            apellido = input("Ingrese Apellido: ")
            carnet = input("Ingrese Carnet: ")
            nuevoNodo = NodoDoblementeEnlazada.NodoDoblementeEnlazada(nombre, apellido, carnet)
            nuevaLista.insertar_al_inicio(nuevoNodo)
            print("Nodo Agregado")
        elif choice == "2":
            nombre = input("Ingrese Nombre: ")
            apellido = input("Ingrese Apellido: ")
            carnet = input("Ingrese Carnet: ")
            nuevoNodo = NodoDoblementeEnlazada.NodoDoblementeEnlazada(nombre, apellido, carnet)
            nuevaLista.insertar_al_final(nuevoNodo)
        elif choice == "3":
            carnet = input("Ingrese Carnet: ")
            nuevaLista.eliminar_por_valor(carnet)
        elif choice == "4":
            nuevaLista.imprimirLista()
            
        elif choice == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion Invalida, ingrese valor de 1-5")
main()
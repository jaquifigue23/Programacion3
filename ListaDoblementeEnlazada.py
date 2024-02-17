import NodoDoblementeEnlazada

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar_al_final(Self, nuevoNodo):
        if (Self.cabeza == None):
            Self.cabeza = nuevoNodo
        else:
            tmp = Self.cabeza
            while(tmp == Self.cabeza or tmp.siguiente != None):
                nuevoNodo.anterior = tmp
                tmp.siguiente = nuevoNodo
                tmp = tmp.siguiente                
                

    def imprimirLista(Self):
            tmp = Self.cabeza
            
            while(tmp != None):
                print(tmp.nombre + tmp.apellido + tmp.carnet)
                tmp = tmp.siguiente
               
nuevaLista = ListaDoblementeEnlazada()

nuevoNodo1 = NodoDoblementeEnlazada.NodoDoblementeEnlazada("oscar", "lopez", "123")
nuevoNodo2 = NodoDoblementeEnlazada.NodoDoblementeEnlazada("jaqui", "lopez", "123")


nuevaLista.insertar_al_final(nuevoNodo1)
nuevaLista.insertar_al_final(nuevoNodo2)

nuevaLista.imprimirLista()
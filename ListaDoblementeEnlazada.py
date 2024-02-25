import NodoDoblementeEnlazada

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar_al_inicio(Self, nuevoNodo):
        if (Self.cabeza == None):
            Self.cabeza = nuevoNodo
        else:
            Self.cabeza.anterior=nuevoNodo
            nuevoNodo.siguiente = Self.cabeza
            Self.cabeza = nuevoNodo
            
             
    def insertar_al_final(Self, nuevoNodo):
        if (Self.cabeza == None):
            Self.cabeza = nuevoNodo
        else:
            tmp = Self.cabeza
            if(tmp.siguiente == None):
                tmp.siguiente = nuevoNodo
                nuevoNodo.anterior = tmp
            else: 
                while( tmp.siguiente != None):
                    tmp = tmp.siguiente
                tmp.siguiente = nuevoNodo
                nuevoNodo.anterior = tmp
             
    def eliminar_por_valor(self,carnet):
        if(self.cabeza == None):
            print("No existe Registro")
        else:
            if(self.cabeza.siguiente == None and self.cabeza.carnet == carnet):                          
               self.cabeza = None
            else:
                tmp=self.cabeza
                while(tmp != None):
                    if(tmp.carnet == carnet):
                        #eliminar tmp
                        if(tmp.anterior == None):
                            tmp= tmp.siguiente
                            self.cabeza =tmp
                            tmp.anterior.siguiente = None
                            tmp.anterior = None
                        elif(tmp.siguiente == None):
                            tmp=tmp.anterior
                            tmp.siguiente.anterior=None
                            tmp.siguiente =None
                        else:
                            tmp.anterior.siguiente = tmp.siguiente
                            tmp.siguiente.anterior =tmp.anterior
                            tmp.anterior = None
                            tmp.siguiente = None
                    tmp = tmp.siguiente
                            
    def imprimirLista(Self):

            tmp = Self.cabeza
            
            while(tmp != None):
                print(tmp.nombre + tmp.apellido + tmp.carnet)
                tmp = tmp.siguiente
               

        tmp=Self.cabeza
        while(tmp != None):
            if(tmp.anterior == None):
                if(tmp.siguiente == None):
                    print("<-" + tmp.carnet + "->", end="")
                else:
                    print("<-" + tmp.carnet, end="")
            elif(tmp.siguiente == None):
                if(tmp.anterior == Self.cabeza):
                    print("<->" + tmp.carnet + "->", end="")
                else:    
                    print(tmp.carnet + "->", end="")
            else:
                print("<->" + tmp.carnet + "<->", end="")
            tmp = tmp.siguiente
        print("")    
            
 main
""" nuevaLista = ListaDoblementeEnlazada()

nuevoNodo1 = NodoDoblementeEnlazada.NodoDoblementeEnlazada("oscar", "lopez", "456")
nuevoNodo2 = NodoDoblementeEnlazada.NodoDoblementeEnlazada("jaqui", "lopez", "123")
nuevoNodo3 = NodoDoblementeEnlazada.NodoDoblementeEnlazada("pedro", "lopez", "789")
nuevoNodo4 = NodoDoblementeEnlazada.NodoDoblementeEnlazada("juan", "lopez", "741")


nuevaLista.insertar_al_final(nuevoNodo1)
nuevaLista.insertar_al_final(nuevoNodo2)
nuevaLista.insertar_al_final(nuevoNodo3)
nuevaLista.insertar_al_final(nuevoNodo4)

nuevaLista.eliminar_por_valor("741")
nuevaLista.eliminar_por_valor("456")
nuevaLista.imprimirLista() """



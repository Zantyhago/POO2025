from classNodo import Nodo

class Lista:
    __comienzo: Nodo
    __tope: int
    __indice: int
    __actual: Nodo

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregaProfesor(self, profesor):
        nodo = Nodo(profesor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def listarDatosProfesores(self):
        aux = self.__comienzo
        while aux!= None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def eliminarPorDNI(self, xdni):
        aux = self.__comienzo
        encontrado = False
        if aux.getDato().getDNI() == xdni:
            encontrado = True
            print(f"Encontrado y deleteado: {self.__comienzo.getDato()}")
            self.__comienzo = aux.getSiguiente()
            self.__tope -= 1
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            while aux != None and not encontrado:
                if aux.getDato().getDNI() == xdni:
                    encontrado = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            if encontrado:
                print(f"Encontrado y deleteado: {aux.getDato()}")
                ant.setSiguiente(aux.getSiguiente())
                self.__tope -= 1
                del aux
            else:
                print(f"No se encontró el DNI {xdni} en la lista.")
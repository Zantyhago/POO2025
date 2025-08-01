class Nodo:
    __dato: None
    __siguiente: None
    
    def __init__(self, unPaciente):
        self.__dato = unPaciente
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__dato
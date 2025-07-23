class Nodo:
    __dato: None
    __siguiente: None

    def __init__(self, xmedio):
        self.__dato = xmedio
        self.__siguiente = None

    def getDato(self):
        return self.__dato
    
    def setSiguiente(self, xsig):
        self.__siguiente = xsig

    def getSiguiente(self):
        return self.__siguiente
class Cancha:
    __id: str
    __piso: str
    __importe: float

    def __init__(self, xid, xpiso, ximp):
        self.__id = xid
        self.__piso = xpiso
        self.__importe = ximp

    def getID(self):
        return self.__id
    
    def getPiso(self):
        return self.__piso
    
    def getImporteHora(self):
        return self.__importe
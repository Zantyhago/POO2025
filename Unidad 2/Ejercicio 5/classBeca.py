class Beca:
    __idBeca: int
    __tipo: str
    __importe: float

    def __init__(self, xid, xtipo, ximp):
        self.__idBeca = xid
        self.__tipo = xtipo
        self.__importe = ximp

    def getID(self):
        return self.__idBeca
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe
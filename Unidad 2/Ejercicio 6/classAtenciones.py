class Atenciones:
    __Dni: int
    __fecha: str
    __importe: float

    def __init__(self, xdni, xfecha, ximp):
        self.__Dni = xdni
        self.__fecha = xfecha
        self.__importe = ximp

    def getDNIat(self):
        return self.__Dni
    
    def getFecha(self):
        return self.__fecha
    
    def getImporte(self):
        return self.__importe
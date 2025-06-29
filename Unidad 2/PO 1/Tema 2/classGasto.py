class Gasto:
    __patente: str
    __fecha: str
    __importe_gasto: float
    __descripcion: str

    def __init__(self, xpat, xfecha, ximpGas, xdescr):
        self.__patente = xpat
        self.__fecha = xfecha
        self.__importe_gasto = ximpGas
        self.__descripcion = xdescr

    def getPatente(self):
        return self.__patente
    
    def getFecha(self):
        return self.__fecha
    
    def getImpGasto(self):
        return self.__importe_gasto
    
    def getDescripcion(self):
        return self.__descripcion
    
    def __lt__(self, otro):
        resultado = None
        if self.getFecha() == otro.getFecha():
            resultado = self.getPatente() < otro.getPatente()
        else:
            self.getFecha() < otro.getFecha()
        return resultado
class Bateria:
    __patente: str
    __marca = "CATL"
    __Capacidad_kwh: float
    __CargaActual_kwh: float
    
    def __init__(self, xpat, xcapac, xcarga):
        self.__patente = xpat
        self.__Capacidad_kwh = xcapac
        self.__CargaActual_kwh = xcarga
    
    def getPatenteBat(self):
        return self.__patente
    
    @classmethod
    def getMarca(cls):
        return cls.__marca
    
    def getCapacidadKWH(self):
        return self.__Capacidad_kwh
    
    def getCargaActual(self):
        return self.__CargaActual_kwh
    
    def getEnergiaDisponible(self):
        return (self.getCapacidadKWH() - self.getCargaActual()) / 10
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    __Patente: str
    __CapacidadPasajeros: int
    __KmARecorrer: float
    
    def __init__(self, xpat, xcap, xkm):
        self.__Patente = xpat
        self.__CapacidadPasajeros = xcap
        self.__KmARecorrer = xkm
        
    def getPatente(self):
        return self.__Patente
    
    def getCapacidadPas(self):
        return self.__CapacidadPasajeros
    
    def getKMaRecorr(self):
        return self.__KmARecorrer
    
    @abstractmethod
    def getConsumo(self):
        pass
    
    def __str__(self):
        return f"{self.getPatente()}\n - Capacidad: {self.getCapacidadPas()}\n - KM a recorrer: {self.getKMaRecorr()}\n - Consumo: {self.getConsumo()}"
    
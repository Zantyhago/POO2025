from abc  import ABC, abstractmethod

class Vehículo(ABC):
    __matricula: str
    __modelo: str
    __costroKM: float
    __cantDias: int

    def __init__(self, xmatr, xmod, xcost, xcant):
        self.__matricula = xmatr
        self.__modelo = xmod
        self.__costroKM = xcost
        self.__cantDias = xcant

    def getMatricula(self):
        return self.__matricula
    
    def getModelo(self):
        return self.__modelo
    
    def getCostoKM(self):
        return self.__costroKM
    
    def getCantDias(self):
        return self.__cantDias
    
    @abstractmethod
    def getImporte(self):
        pass
    
    def __str__(self):
        return f"{self.getMatricula()}\n - {self.getModelo()}\n - {self.getCostoKM()}\n - {self.getCantDias}"
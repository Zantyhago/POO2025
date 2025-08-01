from classVehiculo import Vehículo
from classRuta import Ruta

class Camión(Vehículo):
    __capMaxima: float
    __cantTransportada: float
    __rutas: list

    def __init__(self, xmatr, xmod, xcost, xcant, xcapM, xcantT):
        super().__init__(xmatr, xmod, xcost, xcant)
        self.__capMaxima = xcapM
        self.__cantTransportada = xcantT
        self.__rutas = []

    def agregaRutas(self, unaRuta):
        if isinstance(unaRuta, Ruta):
            self.__rutas.append(unaRuta)
        else:
            raise TypeError("Se esperaba una ruta.")
        
    def getCapMaxima(self):
        return self.__capMaxima
    
    def getCantTrans(self):
        return self.__cantTransportada
    
    def __str__(self):
        return f"{super().__str__()}\n - {self.getCapMaxima()}\n - {self.getCantTrans(())}\n"
    
    def getImporte(self):
        if self.getCantTrans() > 4500:
            retorno = (self.getCantDias() * self.getCostoKM()) + (self.getCostoKM * 0.05)
        elif self.getCantTrans() <= 4500:
            retorno = (self.getCantDias() * self.getCostoKM()) + (self.getCostoKM * 0.02)
        return
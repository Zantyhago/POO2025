from classVehiculo import Vehículo

class Aut(Vehículo):
    __pasajerosMax: int
    __cantPasajerosReal: int

    def __init__(self, xmatr, xmod, xcost, xcant, xcapM, xcantP):
        super().__init__(xmatr, xmod, xcost, xcant)
        self.__pasajerosMax = xcapM
        self.__cantPasajerosReal = xcantP

    def getCapMaxPas(self):
        return self.__pasajerosMax
    
    def getCantPasajeros(self):
        return self.__cantPasajerosReal
    
    def getImporte(self):
        
        return 
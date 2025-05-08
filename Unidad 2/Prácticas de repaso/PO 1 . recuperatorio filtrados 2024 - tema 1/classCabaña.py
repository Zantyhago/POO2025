class Cabaña:
    __numero: int 
    __cantidadHabitaciones: int
    __camasGrandes: int
    __camasChicas: int
    __importe: float

    def __init__(self, xnum, xcantHab, xcamasG, xcamasC, ximp):
        self.__numero = xnum
        self.__cantidadHabitaciones = xcantHab
        self.__camasGrandes = xcamasG
        self.__camasChicas = xcamasC
        self.__importe = ximp

    def getNumeroC(self):
        return self.__numero

    def getCantH(self):
        return self.__cantidadHabitaciones
    
    def getCantC(self):
        return self.__camasGrandes
    
    def getCantG(self):
        return self.__camasChicas
    
    def getImporte(self):
        return self.__importe
    
    def getCapacidad(self):
        return self.getCantG()*2 + self.getCantC()

    def __ge__(self, cantidad):
        return self.getCapacidad() >= cantidad
    
    def __eq__(self, value):
        return self.getNumeroC() == value
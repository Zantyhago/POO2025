from classMedio import Medio

class PrensaEscrita(Medio):
    __tipo_publicacion: set
    __periodicidad: str

    def __init__(self, xnomb, xaud, xtipo, xperiod):
        super().__init__(xnomb, xaud)
        self.__tipo_publicacion = xtipo
        self.__periodicidad = xperiod

    def getTipo(self):
        return self.__tipo_publicacion
    
    def getPeriodicidad(self):
        return self.__periodicidad
    
    def  __str__(self):
        return f"{super().__str__()} Tipo: {self.getTipo()}. Periodicidad: {self.getPeriodicidad()}"
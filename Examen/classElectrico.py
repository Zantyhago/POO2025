from classVehiculo import Vehiculo
from classBateria import Bateria

class Electrico(Vehiculo):
    __autonomiaKm: int
    __eficiencia_kwh_por_km: float
    __baterias: list
    
    def __init__(self, xpat, xcap, xkm, xauton, xefic):
        super().__init__(xpat, xcap, xkm)
        self.__autonomiaKm = xauton
        self.__eficiencia_kwh_por_km = xefic
        self.__baterias = []
        
    def agregaBaterias(self, unaBat):
        if isinstance(unaBat, Bateria):
            self.__baterias.append(unaBat)
        else:
            raise TypeError("Se esperaba una bateria.")
    
    def buscaCapacidad(self):
        cargasDisponibles = 0
        for bateria in self.__baterias:
            cargasDisponibles += bateria.getEnergiaDisponible()
        return cargasDisponibles - self.getConsumo()

    def getAutonomia(self):
        return self.__autonomiaKm
    
    def getEficienciaKWH(self):
        return self.__eficiencia_kwh_por_km
    
    def getConsumo(self):
        return super().getKMaRecorr() * self.getEficienciaKWH()
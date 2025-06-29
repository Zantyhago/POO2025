class Tramo:
    __origen: str
    __destino: str
    __distancia_km: float
    __patente: str

    def __init__(self, xorig, xdest, xdist, xpat):
        self.__origen = xorig
        self.__destino = xdest
        self.__distancia_km = xdist
        self.__patente = xpat

    def getOrigen(self):
        return self.__origen
    
    def getDestino(self):
        return self.__destino
    
    def getDistanciaKM(self):
        return self.__distancia_km
    
    def getPatente(self):
        return self.__patente
    
    def __gt__(self, value):
        return self.getDistanciaKM() > value
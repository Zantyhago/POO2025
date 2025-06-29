class Colectivo:
    __patente: str
    __marca: str
    __modelo: int
    __capacidad: int
    __dni_chofer: str
    __consumo = 35

    def __init__(self, xpat, xmarca, xmod, xcapc, xdni):
        self.__patente = xpat
        self.__marca = xmarca
        self.__modelo = xmod
        self.__capacidad = xcapc
        self.__dni_chofer = xdni

    def getPatente(self):
        return self.__patente
    
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
    
    @classmethod
    def getConsumo(cls):
        return cls.__consumo

    def getCapacidad(self):
        return self.__capacidad

    def getDNI(self):
        return self.__dni_chofer
class Movilidad:
    __patente: str
    __tipo: str
    __capacidad_carga: int
    __importe_patente: float
    __marca: str
    __modelo: str

    def __init__(self, xpat, xtipo, xcapac, ximpPat, xmarca, xmodelo):
        self.__patente = xpat
        self.__tipo = xtipo
        self.__capacidad_carga = xcapac
        self.__importe_patente = ximpPat
        self.__marca = xmarca
        self.__modelo = xmodelo

    def getPatente(self):
        return self.__patente
    
    def getTipo(self):
        return self.__tipo
    
    def getCapacidadTrans(self):
        return self.__capacidad_carga
    
    def getImportePat(self):
        return self.__importe_patente
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def __str__(self):
        return f"{self.getPatente()} - {self.getMarca()} - ${self.getImportePat()}"
    #patente, marca, modelo y total a pagar

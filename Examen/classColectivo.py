from classVehiculo import Vehiculo

class Colectivo(Vehiculo):
    __empresa: str
    __capCombustible: float
    __tipoCombustible: str
    
    def __init__(self, xpat, xcap, xkm, xemp, xcapC, xtipo):
        super().__init__(xpat, xcap, xkm)
        self.__empresa = xemp
        self.__capCombustible = xcapC
        self.__tipoCombustible = xtipo
        
    def getEmpresa(self):
        return self.__empresa
    
    def getCapCombustible(self):
        return self.__capCombustible
    
    def getTipoCombustible(self):
        return self.__tipoCombustible
    
    def getConsumo(self):
        consumo = None
        if self.getTipoCombustible() == 'gasoil':
            consumo = self.getKMaRecorr() * 0.02
        elif self.getTipoCombustible() == 'gnc':
            consumo = self.getKMaRecorr() * 0.15
        return consumo
    
    def __str__(self):
        return f"{super().__str__()}\n - Empresa: {self.getEmpresa()}\n - Cap. Combustible: {self.getCapCombustible()}\n - Tipo de Comb.: {self.getTipoCombustible()}"
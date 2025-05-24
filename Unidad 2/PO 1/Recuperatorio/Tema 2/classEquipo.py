class Equipo:
    __idEquipo: str
    __denominacion: str
    __presidente: str
    __puntos: int
    __golesAfavor: int
    __golesEncontra: int
    __diferenciaGoles: int

    def __init__(self, xid, xdeno, xpresi, xpuntos, xfavor, xcontra, xdif):
        self.__idEquipo = xid
        self.__denominacion = xdeno
        self.__presidente = xpresi
        self.__puntos = xpuntos
        self.__golesAfavor = xfavor
        self.__golesEncontra = xcontra
        self.__diferenciaGoles = xdif

    def getID(self):
        return self.__idEquipo
    
    def getDenominacion(self):
        return self.__denominacion

    def getPresidente(self):
        return self.__presidente
    
    def setPuntos(self, xpuntos):
        self.__puntos += xpuntos

    def getPuntos(self):
        return self.__puntos
    
    def setgetGolesAFavor(self, goles):
        self.__golesAfavor += goles

    def getGolesAFavor(self):
        return self.__golesAfavor
    
    def setgetGolesContra(self, goles):
        self.__golesEncontra += goles

    def getGolesContra(self):
        return self.__golesEncontra
    
    def setDiferencia(self, dif):
        self.__diferenciaGoles += dif

    def getDiferencia(self):
        return self.__diferenciaGoles
    
    def __gt__(self, otro):
        return self.getPuntos() > otro.getPuntos()
    
    def __str__(self):
        return f"{self.getDenominacion()}              {self.getPuntos()}   {self.getGolesAFavor()}   {self.getGolesContra()}   {self.getDiferencia()}"
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
        if xpuntos != -1:
            self.__puntos += xpuntos
        else:
            self.__puntos = 0
    def getPuntos(self):
        return self.__puntos
    
    def setgetGolesAFavor(self, goles):
        if goles != -1:
            self.__golesAfavor += goles
        else:
            self.__golesAfavor = 0
    def getGolesAFavor(self):
        return self.__golesAfavor
    
    def setgetGolesContra(self, goles):
        if goles != -1:
            self.__golesEncontra += goles
        else:
            self.__golesEncontra = 0
    def getGolesContra(self):
        return self.__golesEncontra
    
    def setDiferencia(self):
        self.__diferenciaGoles = 0
    def getDiferencia(self):
        self.__diferenciaGoles = self.__golesAfavor - self.__golesEncontra
        return self.__diferenciaGoles
    
    def __gt__(self, otro):
        retorno = None
        if self.getPuntos() != otro.getPuntos():
            retorno = self.getPuntos() > otro.getPuntos()
        else:
            retorno = self.getDiferencia() > otro.getDiferencia()
        return retorno
    
    def __str__(self):
        return f"{'':<1}{self.getDenominacion():<26}{self.getPuntos():^6}   {self.getGolesAFavor():^13}   {self.getGolesContra():^15}   {self.getDiferencia():^19}"
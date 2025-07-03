class Curso:
    __identificacion: int
    __denominacion: str
    __cant_horas: int
    __cant_dias: int
    __cupo: int
    
    def __init__(self, xid, xden, xcantH, xcantD, xcupo):
        self.__identificacion = xid
        self.__denominacion = xden
        self.__cant_horas = xcantH
        self.__cant_dias = xcantD
        self.__cupo = xcupo
        
    def getID(self):
        return self.__identificacion
    def getDenominacion(self):
        return self.__denominacion
    def getCantH(self):
        return self.__cant_horas
    def getCantD(self):
        return self.__cant_dias
    def getCupo(self):
        return self.__cupo
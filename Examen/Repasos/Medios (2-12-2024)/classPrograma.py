import datetime
class Programa:
    __nombre: str
    __hora_inicio: datetime
    __hora_final: datetime

    def __init__(self, xnom, xhi, xhf):
        self.__nombre = xnom
        self.__hora_inicio = xhi
        self.__hora_final = xhf

    def getNombreP(self):
        return self.__nombre
    
    def getHoraInicio(self):
        return self.__hora_inicio
    
    def getHoraFinal(self):
        return self.__hora_final
    
    def __str__(self):
        return f"Nombre del programa: {self.getNombreP()}.\n  - H. inicio: {self.getHoraInicio()}\n  - H. finalización: {self.getHoraFinal()}"
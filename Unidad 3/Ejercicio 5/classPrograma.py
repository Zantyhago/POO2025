class Programa:
    __nombre: str
    __hora_inicio: str
    __hora_fin: str

    def __init__(self, xnomb, xhi, xhf):
        self.__nombre = xnomb
        self.__hora_inicio = xhi
        self.__hora_fin = xhf

    def getNombProg(self):
        return self.__nombre
    
    def getHInicio(self):
        return self.__hora_inicio
    
    def getHFin(self):
        return self.__hora_fin
    
    def __str__(self):
        return f"{self.getNombProg()} - De {self.getHInicio()} a {self.getHFin()}"
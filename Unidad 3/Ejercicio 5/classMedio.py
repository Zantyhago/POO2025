class Medio:
    __Nombre: str
    __Audiencia: int

    def __init__(self, xnomb, xaud):
        self.__Nombre = xnomb
        self.__Audiencia = xaud

    def getNombre(self):
        return self.__Nombre
    
    def getAudiencia(self):
        return self.__Audiencia
    
    def __str__(self):
        return f"{self.getNombre()}. Audiencia: {self.getAudiencia()}."
from abc import ABC, abstractmethod

class Medio(ABC):
    __nombre: str
    __audiencia_estimada: int

    def __init__(self, xnomb, xaud):
        self.__nombre = xnomb
        self.__audiencia_estimada = xaud

    def getNombre(self):
        return self.__nombre
    
    def getCantAudiencia(self):
        return self.__audiencia_estimada
    
    @abstractmethod
    def getIndiceAudiencia(self):
        pass

    def __str__(self):
        return f"Nombre: {self.getNombre()}.\n - Audiencia estimada:{self.getCantAudiencia()}\n - Índice de audiencia: {self.getIndiceAudiencia()}"
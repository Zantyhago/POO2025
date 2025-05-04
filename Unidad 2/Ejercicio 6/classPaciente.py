class Paciente:
    __dni: int
    __Nombre: str
    __Unidad: str

    def __init__(self, xdni, xnom, xunidad):
        self.__dni = xdni
        self.__Nombre = xnom
        self.__Unidad = xunidad

    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__Nombre
    
    def getUnidad(self):
        return self.__Unidad

    def __lt__(self, otro):
        return (self.getUnidad(), self.getNombre()) < (otro.getUnidad(), otro.getNombre())
    
    def __str__(self):
        return f"{self.getNombre()} - {self.getDNI()} - {self.getUnidad()}"
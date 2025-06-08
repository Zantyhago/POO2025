class ProgramaCapacitacion:
    __nombre: str
    __codigo: str
    __duracion: int

    def __init__(self, xnomb, xcod, xdur):
        self.__nombre = xnomb
        self.__codigo = xcod
        self.__duracion = xdur

    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo
    
    def getDuracion(self):
        return self.__duracion
    
    def __str__(self):
        return self.getNombre()
class Resultado:
    __Fecha: str
    __idEquipoLocal: str
    __golesLocal: int
    __idEquipoVisitante: str
    __golesVisitante: int
    __inscripcion = 45000

    def __init__(self, xfecha, xidlocal, xgollocal, xidvisit, xgolvisit):
        self.__Fecha = xfecha
        self.__idEquipoLocal = xidlocal
        self.__golesLocal = xgollocal
        self.__idEquipoVisitante = xidvisit
        self.__golesVisitante = xgolvisit

    def getFecha(self):
        return self.__Fecha
    
    def getIDlocal(self):
        return self.__idEquipoLocal
    
    def getGolsLocal(self):
        return self.__golesLocal
    
    def getIDvisitante(self):
        return self.__idEquipoVisitante
    
    def getGolsVisitante(self):
        return self.__golesVisitante
    
    @classmethod
    def getInscripcion(cls):
        return cls.__inscripcion
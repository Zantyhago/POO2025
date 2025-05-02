class Carrera:
    __codigoCarrera: int
    __nombreCarrera: str
    __titulo: str
    __duracion: str
    __nivel: str
    __codigoFacuDic: int

    def __init__(self, xcod, xnomb, xtit, xdura, xniv, xcodFac):
        self.__codigoCarrera = xcod
        self.__nombreCarrera = xnomb
        self.__titulo = xtit
        self.__duracion = xdura
        self.__nivel = xniv
        self.__codigoFacuDic = xcodFac

    def getCodCarrera(self):
        return self.__codigoCarrera
    
    def getNombreCarrera(self):
        return self.__nombreCarrera
    
    def getDuracion(self):
        return self.__duracion
        
    def getCodFacuDic(self):
        return self.__codigoFacuDic
    
    def __lt__(self, otro):
        return self.getNombreCarrera() < otro.getNombreCarrera()
    
    def __str__(self):
        return f'''Nombre de la carrera: {self.getNombreCarrera()}
            Duracion: {self.getDuracion()}
'''

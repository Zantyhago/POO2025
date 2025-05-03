class Beneficiario:
    __dni: int
    __nombre: str 
    __apellido: str
    __carrera: str
    __facultad: str
    __anioCursa: int
    __promedio: float
    __idBecaAsignada: int

    def __init__(self, xdni, xnom, xape, xcarr, xcufa, xanio, xprom, xid):
        self.__dni = xdni
        self.__nombre = xnom
        self. __apellido = xape
        self.__carrera = xcarr
        self.__facultad = xcufa
        self.__anioCursa = xanio
        self.__promedio = xprom
        self.__idBecaAsignada = xid
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido
    
    def getCarrera(self):
        return self.__carrera
    
    def getFacultad(self):
        return self.__facultad
    
    def getAnio(self):
        return self.__anioCursa
    
    def getPromedio(self):
        return self.__promedio
    
    def getIDasign(self):
        return self.__idBecaAsignada
    
    def __gt__(self, otro):
        return self.getFacultad() > otro.getFacultad()
    
    def __str__(self):
        return f"{self.getNombre()} {self.getApellido()}            {self.getDNI()}           {self.getCarrera()}           {self.getAnio()}          {self.getPromedio()}          {self.getFacultad()}"
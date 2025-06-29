class Medico:
    __DNI: str
    __Nombre: str
    __Especialidad: str
    __Matrícula: str
    __Zona: str
    __Precio = 14500

    def __init__(self, xdni, xnom, xesp, xmat, xz):
        self.__DNI = xdni
        self.__Nombre = xnom
        self.__Especialidad = xesp
        self.__Matrícula = xmat
        self.__Zona = xz

    def getDNI(self):
        return self.__DNI
    
    def getNombre(self):
        return self.__Nombre
    
    def getEspecialidad(self):
        return self.__Especialidad
    
    def getMatricula(self):
        return self.__Matrícula
    
    def getZona(self):
        return self.__Zona
    
    @classmethod
    def getPrecio(cls):
        return cls.__Precio
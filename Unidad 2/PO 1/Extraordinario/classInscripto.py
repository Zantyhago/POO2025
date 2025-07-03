class Inscripto:
    __dni: str
    __apellido_nombre: str
    __id_curso: str
    __cant_dias_asistio: int
    __nota_final: float
    
    def __init__(self, xdni, xnya, xidC, xcantD = 0, xnota = 0):
        self.__dni = xdni
        self.__apellido_nombre = xnya
        self.__id_curso = xidC
        self.__cant_dias_asistio = xcantD
        self.__nota_final = xnota
        
    def getDNI(self):
        return self.__dni
    
    def getAyN(self):
        return self.__apellido_nombre
    
    def getIDc(self):
        return self.__id_curso
    
    def setDiaAsistio(self, cant):
        self.__cant_dias_asistio += cant
    
    def getcantDa(self):
        return self.__cant_dias_asistio
    
    def setNotaF(self, xnota):
        self.__nota_final = xnota
    
    def getNotaF(self):
        return self.__nota_final
    
    def __lt__(self, otro):
        return self.getAyN() < otro.getAyN()
    
    def __str__(self):
        return f"{self.getDNI()} - {self.getAyN()} - {self.getcantDa()} - {self.getNotaF()}"
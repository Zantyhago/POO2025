class Empleado:
    __NyA: str
    __idEmpleado: int
    __puesto: str

    def __init__(self, xnya, xid, xpues):
        self.__NyA = xnya
        self.__idEmpleado = xid
        self.__puesto = xpues

    def getNyA(self):
        return self.__NyA
    
    def getIDemleado(self):
        return self.__idEmpleado
    
    def getPuesto(self):
        return self.__puesto
    
    def __str__(self):
        return f"{self.getNyA()} - ID:  {self.getIDemleado()} - Puesto: {self.getPuesto()}"
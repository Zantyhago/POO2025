from classEmpleado import Empleado
from classPrograma import ProgramaCapacitacion

class Matricula:
    __fecha: str
    __empleado: object
    __programa: object

    def __init__(self, xfecha, xemp, xprog):
        self.__fecha = xfecha
        self.__empleado = xemp
        self.__programa = xprog

    def getFecha(self):
        return self.__fecha
    
    def getEmpleado(self):
        return self.__empleado
    
    def getPrograma(self):
        return self.__programa
    
    def __str__(self):
        return self.getFecha()
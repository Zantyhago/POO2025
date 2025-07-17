from classCuentaCampus import CuentaCampus
class Profesor:
    __dni: str
    __apellido: str
    __nombre: str
    __cargo: str
    __cuenta: CuentaCampus

    def __init__(self, xdni, xap, xnom):
        self.__dni = xdni
        self.__apellido = xap
        self.__nombre = xnom
        self.__cuenta = CuentaCampus((self.__apellido+self.__nombre).lower(), self.__dni)

    def getDNI(self):
        return self.__dni
    
    def __str__(self):
        return f"Apellido y nombre: {self.__apellido} {self.__nombre}\n{self.__cuenta}"
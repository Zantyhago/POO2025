import abc
class Plan(abc.ABC):
    __compania: str
    __duracion: int
    __cobertura: str
    __precio: float

    def __init__(self, xnom, xdur, xcob, xprec):
        self.__compania = xnom
        self.__duracion = xdur
        self.__cobertura = xcob
        self.__precio = xprec

    def getCompañia(self):
        return self.__compania
    
    def getDuracion(self):
        return self.__duracion
    
    def getCobertura(self):
        return self.__cobertura
    
    def getPracioBase(self):
        return self.__precio

    @abc.abstractmethod
    def getPrecio(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__:<15}{self.getCompañia():<19}{self.getDuracion():<11}{self.getCobertura():<27}{self.getPrecio():.2f}"
        # self.__class__.__name__ devuelve el nombre de la clase

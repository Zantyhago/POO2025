import abc
class Plan:
    __compania: str
    __duracion: int
    __cobertura: str
    __precio: float

    def __init__(self, xnom, xdur, xcob, xprec):
        self.__compania = xnom
        self.__duracion = xdur
        self.__cobertura = xcob
        self.__precio = xprec

    @abc.abstractmethod
    def getTipo(self):
        pass

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
        return f"{self.getTipo():<15}{self.getCompañia():<19}{self.getDuracion():<11}{self.getCobertura():<27}{self.getPrecio():.2f}"
        # en vez de hacer getTipo(), se podría un type(self) directamente. No avivo mas

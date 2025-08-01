class Paciente:
    __nombre: str
    __apellido: str
    __mail: str
    __telefono: str
    __valor_consulta = 15000

    def __init__(self, xnom, xap, xmail, xnum):
        self.__nombre = xnom
        self.__apellido = xap
        self.__mail = xmail
        self.__telefono = xnum

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getNyA(self):
        return f"{self.getNombre()} {self.getApellido()}"
    
    def getMail(self):
        return self.__mail
    
    def getTelefono(self):
        return self.__telefono
    
    @classmethod
    def getValorCons(cls):
        return cls.__valor_consulta
    
    @classmethod
    def setValorCons(cls, xvalor):
        cls.__valor_consulta = xvalor

    def getImporte():
        pass

    def __str__(self):
        return f"{self.getNyA()} {self.getMail()} {self.getTelefono()}"
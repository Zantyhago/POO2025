class Reserva:
    __numeroReserva: int
    __cliente: str
    __cabana: int
    __fechaInicio: str
    __cantHuespedes: int
    __cantDias: int
    __sena: float

    def __init__(self, xnum, xclis, xcabana, fechaInit, xcantHues, xcantDias, xsena):
        self.__numeroReserva = xnum
        self.__cliente = xclis
        self.__cabana = xcabana
        self.__fechaInicio = fechaInit
        self.__cantHuespedes = xcantHues
        self.__cantDias = xcantDias
        self.__sena = xsena

    def getNumReserva(self):
        return self.__numeroReserva

    def getCliente(self):
        return self.__cliente
    
    def getCabana(self):
        return self.__cabana
    
    def getFechaInit(self):
        return self.__fechaInicio
    
    def getCantHuespedes(self):
        return self.__cantHuespedes
    
    def getCantDias(self):
        return self.__cantDias
    
    def getSena(self):
        return self.__sena
    
    def __eq__(self, value):
        return self.getFechaInit() == value
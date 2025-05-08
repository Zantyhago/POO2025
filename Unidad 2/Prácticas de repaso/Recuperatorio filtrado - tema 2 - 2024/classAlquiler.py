class Alquiler:
    __cliente: str
    __cancha: str
    __hora: int
    __minutos: int
    __duracion: int

    def __init__(self, xcli, xcancha, xhora, xmin, xdur):
        self.__cliente = xcli
        self.__cancha = xcancha
        self.__hora = xhora
        self.__minutos = xmin
        self.__duracion = xdur

    def getCliente(self):
        return self.__cliente
    
    def getCancha(self):
        return self.__cancha
    
    def getHora(self):
        return self.__hora
    
    def getMinuto(self):
        return self.__minutos
    
    def getDuracion(self):
        return self.__duracion
    
    def __gt__(self, otro):
        result = None
        if self.getHora() == otro.getHora():
            result = self.getMinuto() > otro.getMinuto()
        else:
            result = self.getHora() > otro.getHora()
        return result
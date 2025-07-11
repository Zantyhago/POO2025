from classPlan import Plan

class Telefonia (Plan):
    __tipollama: str
    __minutos: int

    def __init__(self, xnom, xdur, xcob, xprec, xtipo, xmins):
        self.__tipollama = xtipo
        self.__minutos = xmins
        Plan.__init__(self, xnom, xdur, xcob, xprec)

    def getTipo(self):
        return "Telefonia"

    def getTipoLL(self):
        return self.__tipollama
    
    def getMinutosLL(self):
        return self.__minutos
    
    def getPrecio(self):
        if self.getTipoLL() == 'internacional':
            retorno = self.getPracioBase() * 1.20
        elif self.getTipoLL() == 'locales':
            retorno = (self.getPracioBase() * 7.5) / 100
        else:
            retorno = self.getPracioBase()
        return retorno
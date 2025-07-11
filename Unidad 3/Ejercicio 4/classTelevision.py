from classPlan import Plan

class Television (Plan):
    __nacional: int
    __internacional: int

    def __init__(self, xnom, xdur, xcob, xprec, xnac, xint):
        self.__nacional = xnac
        self.__internacional = xint
        Plan.__init__(self, xnom, xdur, xcob, xprec)

    def getTipo(self):
        return "Television"

    def getCantNac(self):
        return self.__nacional
    
    def getCanInt(self):
        return self.__internacional
    
    def getPrecio(self):
        if self.getCantNac() > 10:
            retorno = self.getPracioBase() * 1.15
        else:
            retorno = self.getPracioBase()
        return retorno
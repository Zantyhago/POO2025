from classPaciente import Paciente

class PacObraSocial(Paciente):
    __historial: str
    __alergias: str
    __obraSocial: str

    def __init__(self, xnom, xap, xmail, xnum, xhis, xalerg, xobra):
        super().__init__(xnom, xap, xmail, xnum)
        self.__historial = xhis
        self.__alergias = xalerg
        self.__obraSocial = xobra

    def getHistorial(self):
        return self.__historial
    
    def getAlergias(self):
        return self.__alergias
    
    def getObraSoc(self):
        return self.__obraSocial
    
    def getImporte(self):
        if self.getObraSoc() == 'Provincia':
            importe = self.getValorCons() - 15000 + 5000
        elif self.getObraSoc() == 'OSDE':
            importe = self.getValorCons() - 15000 + 2000
        else:
            importe = self.getValorCons() - 15000 + 10000
        return importe
    
    def __str__(self):
        return f"{super().__str__()} {self.getHistorial()} {self.getAlergias()} {self.getObraSoc()} { self.getImporte()}"
from classPaciente import Paciente

class PacHospitalizado(Paciente):
    __numHab: str
    __fechaIngreso: str
    __diagnostico: str
    __cantDias: str
    __importeDescart: float
    
    def __init__(self, xnom, xap, xmail, xnum, xnumHab, xfecha, xdiag, xcantD, ximpDes):
        super().__init__(xnom, xap, xmail, xnum)
        self.__numHab = xnumHab
        self.__fechaIngreso = xfecha
        self.__diagnostico = xdiag
        self.__cantDias = xcantD
        self.__importeDescart = ximpDes

    def getNumHab(self):
        return self.__numHab
    
    def getFechaIng(self):
        return self.__fechaIngreso
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getCantDias(self):
        return self.__cantDias
    
    def getImpDescart(self):
        return self.__importeDescart
    
    def getImporte(self):
        return self.getValorCons() * self.getCantDias() + self.getImpDescart()
    
    def __str__(self):
        return f"{super().__str__()} {self.getNumHab()} {self.getFechaIng()} {self.getDiagnostico()}"
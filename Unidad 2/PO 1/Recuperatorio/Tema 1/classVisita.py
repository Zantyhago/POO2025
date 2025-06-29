class Visita:
    __Fecha: str
    __DNI_Paciente: str
    __Zona: str
    __DNI_Medico: str
    ___Diagnostico: str

    def __init__(self, xfe, xdnip, xzona, xdnim, xdiag):
        self.__Fecha = xfe
        self.__DNI_Paciente = xdnip
        self.__Zona = xzona
        self.__DNI_Medico = xdnim
        self.___Diagnostico = xdiag

    def getFecha(self):
        return self.__Fecha
    def getDNIp(self):
        return self.__DNI_Paciente
    def getZona(self):
        return self.__Zona
    def getDNIm(self):
        return self.__DNI_Medico
    def getDiagnostico(self):
        return self.___Diagnostico
    def __eq__(self, value):
        return self.getZona().lower() == value.lower()
    def __str__(self):
        return f"{self.getFecha()} - DNI del paciente: {self.getDNIp()} - Diagnostico: {self.getDiagnostico()}"
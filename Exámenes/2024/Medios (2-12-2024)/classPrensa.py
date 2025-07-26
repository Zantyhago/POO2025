from classMedio import Medio

class PrensaEScrita(Medio):
    __periodicidad: str
    __cant_secciones: int

    def __init__(self, xnomb, xaud, xperiod, xcant):
        super().__init__(xnomb, xaud)
        self.__periodicidad = xperiod
        self.__cant_secciones = xcant

    def getPeriodicidad(self):
        return self.__periodicidad
    
    def getCantSecciones(self):
        return self.__cant_secciones
    
    def getIndiceAudiencia(self):
        retorno = None
        if self.getPeriodicidad().lower() == 'mensual':
            retorno = self.getCantAudiencia() / self.getCantSecciones()
        elif self.getPeriodicidad().lower() == 'semanal':
            retorno = self.getCantAudiencia() / (self.getCantSecciones() * 4)
        return int(retorno)
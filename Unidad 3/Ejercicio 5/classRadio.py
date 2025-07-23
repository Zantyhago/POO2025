from classMedio import Medio
from classPrograma import Programa

class Radio(Medio):
    __nombre_emisora: str
    __frecuencia: str
    __programas: list

    def __init__(self, xnomb, xaud, xnombEmis, xfrecu):
        super().__init__(xnomb, xaud)
        self.__nombre_emisora = xnombEmis
        self.__frecuencia = xfrecu
        self.__programas = []

    def getNombreEmisora(self):
        return self.__nombre_emisora
    
    def getFrecuencia(self):
        return self.__frecuencia
    
    def agregaProgramaR(self, unProg):
        if isinstance(unProg, Programa):
            self.__programas.append(unProg)
        else:
            raise TypeError
        
    def muestraProgramacion(self):
        for prog in self.__programas:
            print(prog)
    
    def __str__(self):
        return f"{super().__str__()} Nombre de emisora: {self.getNombreEmisora()}. Frecuencia: {self.getFrecuencia()}. "
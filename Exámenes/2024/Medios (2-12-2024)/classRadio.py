from classMedio import Medio
from classPrograma import Programa
from datetime import datetime

class Radio(Medio):
    __frecuencia: str
    __programas: list

    def __init__(self, xnomb, xaud, xfrecu):
        super().__init__(xnomb, xaud)
        self.__frecuencia = xfrecu
        self.__programas = []

    def agregaProgramas(self, xnomb, xhi, xhf):
            HI = datetime.strptime(xhi,"%H:%M").time()
            HF = datetime.strptime(xhf,"%H:%M").time()
            if HI < HF:
                self.__programas.append(Programa(xnomb, HI, HF))
            else:
                 raise ValueError("Error en el ingreso del horario.")

    def buscaProgNombre(self, xnomb):
        i = 0
        encontrado = False
        prog = None
        while i < len(self.__programas) and not encontrado:
            if self.__programas[i].getNombreP().lower() == xnomb:
                encontrado = True
                prog = self.__programas[i]
            else:
                i += 1
        return prog

    def getFrecuencia(self):
        self.__frecuencia

    def getIndiceAudiencia(self):
        return int(self.getCantAudiencia() / len(self.__programas))
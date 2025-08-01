from classPrensa import PrensaEScrita
from classRadio import Radio
import csv

class GestorMedios:
    __listaMedios: list

    def __init__(self):
        self.__listaMedios = []

    def agregaMedios(self, unMedio):
        self.__listaMedios.append(unMedio)

    def leeMedios(self):
        medios = open('Medios.csv', encoding = 'utf-8')
        readerM = csv.reader(medios, delimiter = ',')
        programas = open('Programas.csv', encoding = 'utf-8')
        readerP = csv.reader(programas, delimiter = ',')
        for filaM in readerM:
            if filaM[0] == 'R':
                radio = Radio(filaM[1], int(filaM[2]), filaM[3])
                for filaP in readerP:
                    if filaM[3] == filaP[0]:
                        radio.agregaProgramas(filaP[1], filaP[2], filaP[3])
                self.agregaMedios(radio)
                programas.seek(0)
            elif filaM[0] == 'P':
                self.agregaMedios(PrensaEScrita(filaM[1], int(filaM[2]), filaM[3], int(filaM[4])))
        medios.close()
        programas.close()
        print("Medios y programas agregados.")

    def incisoA(self):
        xnomb = input("Ingrese nombre del medio: ")
        xaud = int(input("Ingrese audiencia: "))
        xtipo = input("Ingrese tipo del medio (R/P): ").lower()
        if xtipo in ['r', 'p']:
            if xtipo == 'r':
                xfrec = input("Ingrese frecuencia: ")
                radio = Radio(xnomb, xaud, xfrec)
                esoyam = 'sis'
                while esoyam != 'no':
                    xnombP = input("Ingrese nombre del programa: ")
                    xhi = input("Ingrese hora de inicio (hh:mm): ")
                    xhf = input("Ingrese hora de finalización (hh:mm): ")
                    radio.agregaProgramas(xnombP, xhi, xhf)
                    print("Programa agregado.")
                    esoyam = input("¿Seguir agregando programas? ('no' para finalizar): ")
                self.agregaMedios(radio)
                print("Medio agregado.")
            if xtipo == 'p':
                xperiod = input("Ingrese periodicidad: ")
                xcantSecc = int(input("Ingrese cantidad de secciones: "))
                self.agregaMedios(PrensaEScrita(xnomb, xaud, xperiod, xcantSecc))
        else:
            raise TypeError("Error de tipos en el medio ingresado.")
    
    def incisoB(self, xnombP):
        i = 0
        encontrado = False
        prog = None
        while i < len(self.__listaMedios) and not encontrado:
            if isinstance(self.__listaMedios[i], Radio):
                prog = self.__listaMedios[i].buscaProgNombre(xnombP)
            if prog:
                print(prog)
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise Exception("Programa no encontrado.")
        
    def incisoC(self):
        for medio in self.__listaMedios:
            print(medio)
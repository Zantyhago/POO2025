from classNodo import Nodo
from classPrensa import PrensaEscrita
from classTelevision import Television
from classRadio import Radio
from classPrograma import Programa
import csv

class GestorLista:
    __actual: Nodo
    __comienzo: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration("le gusta lo kinki nasty")
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def agregaMedioCAB(self, unMedio):
        nodo = Nodo(unMedio)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        self.__actual = nodo

    def leeMedios(self):
        archiMed = open('medios.csv', encoding = 'utf-8')
        archiProg = open('programa.csv', encoding = 'utf-8')
        readerMed = csv.reader(archiMed, delimiter = ';')
        next(readerMed)
        readerProg = csv.reader(archiProg, delimiter = ';')
        next(readerProg)
        for filaM in readerMed:
            if filaM[0] == 'T':
                television = Television(filaM[1], int(filaM[2]), filaM[3], int(filaM[4]))
                for filaP in readerProg:
                    if str(filaP[1]) == str(filaM[3]):
                        television.agregaProgramaT(Programa(filaP[2], filaP[3], filaP[4]))
                archiProg.seek(0)
                self.agregaMedioCAB(television)
            elif filaM[0] == 'R':
                radio = Radio(filaM[1], int(filaM[2]), filaM[5], filaM[6])
                for filaP in readerProg:
                    if str(filaP[1])== str(filaM[6]):
                        radio.agregaProgramaR(Programa(filaP[2], filaP[3], filaP[4]))
                archiProg.seek(0)
                self.agregaMedioCAB(radio)
            elif filaM[0] == 'P':
                self.agregaMedioCAB(PrensaEscrita(filaM[1], int(filaM[2]), filaM[7], filaM[8]))
        archiMed.close()
        archiProg.close()
        print("Se cargaron los medios y sus respectivos programas.")

    def Inciso1(self, xpos):
        if xpos < 0 or xpos > self.__tope:
            raise IndexError("Posición fuera de rango.")
        else:
            unMedio = self.leeMedioManual()
            if xpos == 0:
                self.agregaMedioCAB(unMedio)
            else:
                aux = self.__comienzo
                for i in range(xpos-1):
                    aux = aux.getSiguiente()
                nodo = Nodo(unMedio)
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                self.__tope += 1
    
    def leeMedioManual(self):
        medio = None
        xtipo = input("Ingrese tipo de Medio (T/R/P): ").lower()
        if xtipo in ['t', 'r', 'p']:
            xnombre = input("Ingrese nombre del Medio: ")
            xaud = input("Ingrese cantidad de audiencia: ")
            if xtipo == 't':
                xcant = int(input("Ingrese cantidad de canales: "))
                xcanal = input("Ingrese número de canal: ")
                medio = Television(xnombre, xaud, xcanal, xcant)
                bandera = input("Desea agregar el/los programas? (si/no): ")
                while bandera != 'no':
                    xnombreProg = input("Ingrese nombre del programa: ")
                    xhi = input("Ingrese hora de inicio: ")
                    xhf = input("Ingrese hora de finalización: ")
                    medio.agregaProgramaT(Programa(xnombreProg, xhi, xhf))
                    bandera = input('Desea seguir agregando programas? ("no" para finalizar): ')
            elif xtipo == 'r':
                xnomEm = input("Ingrese nombre de la emisora: ")
                xfrec = input("Ingrese frecuencia: ")
                medio = Radio(xnombre, xaud, xnomEm, xfrec)
                bandera = input("Desea agregar el/los programas? (si/no): ")
                while bandera != 'no':
                    xnombreProg = input("Ingrese nombre del programa: ")
                    xhi = input("Ingrese hora de inicio: ")
                    xhf = input("Ingrese hora de finalización: ")
                    medio.agregaProgramaR(Programa(xnombreProg, xhi, xhf))
                    bandera = input('Seguir agregando programas? ("no" para finalizar): ')
            elif xtipo == 'p':
                xtype = input("Ingrese tipo de la publicación: ")
                xperi = input("Ingrese periodicidad: ")
                medio = PrensaEscrita(xnombre, xaud, xtype, xperi)
        else:
            raise TypeError("Tipo de Medio no registreado.")
        return medio
    
    def inciso2(self):
        medio = self.leeMedioManual()
        if isinstance(medio, Radio) or isinstance(medio, Television) or isinstance(medio, PrensaEscrita):
            self.agregaMedioCAB(medio)
        else:
            raise TypeError

    def inciso4(self, xprog):
        encontrado = False
        aux = self.__comienzo
        programa = None
        while aux != None and not encontrado:
            if isinstance(aux.getDato(), Television):
                programa = aux.getDato().buscaPorName(xprog)
            if programa:
                print(f"{aux.getDato()}\n{programa}")
                encontrado = True
            else:
                aux = aux.getSiguiente()
        if not encontrado:
            raise IndexError("Programa ingresado no encontrado.")
    
    def inciso5(self, xemis):
        aux = self.__comienzo
        encontrado = False
        while aux is not None:
            if isinstance(aux.getDato(), Radio) and aux.getDato().getNombreEmisora().lower() == xemis:
                radio = aux.getDato()
                radio.muestraProgramacion()
                aux = None
                encontrado = True
            else:
                aux = aux.getSiguiente()
        if not encontrado:
            raise IndexError("Emisora ingresada no encontrada.")
        
    def inciso6(self):
        aux = self.__comienzo
        cantD = 0
        cantR = 0
        while aux is not None:
            if isinstance(aux.getDato(), PrensaEscrita):
                if aux.getDato().getTipo().lower() == 'diario':
                    cantD += 1
                elif aux.getDato().getTipo().lower() == 'revista':
                    cantR += 1
            aux = aux.getSiguiente()
        print(f"Hay un total de {cantR} revistas y {cantD} diarios.")
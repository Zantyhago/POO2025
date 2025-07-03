from classInscripto import Inscripto
import csv
import numpy as np

class GestorInscriptos:
    __dimension: int
    __cantidad: int
    __incremento: int
    __listaInscriptos: np.ndarray
    
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 3
        self.__incremento = 3
        self.__listaInscriptos = np.empty(self.__dimension, dtype = Inscripto)
        
    def agregaInscripto(self, unInsc):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaInscriptos.resize(self.__dimension)
        self.__listaInscriptos[self.__cantidad] = unInsc
        self.__cantidad += 1
    
    def leeIncriptos(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/Extraordinario/inscripciones.csv', encoding = 'utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            self.agregaInscripto(Inscripto(fila[0], fila[1], int(fila[2]), int(fila[3]), float(fila[4])))
        archivo.close()
        print("Se cargaron los inscriptos.")

    def inciso1(self, xdni):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            inscripto = self.__listaInscriptos[i]
            if inscripto.getDNI() == xdni:
                encontrado = True
                inscripto.setDiaAsistio(1)
                print(f"{inscripto.getAyN()}")
            else:
                i += 1
        if not encontrado:
            print("No se encontró el inscripto indicado.")
    
    def muestraPorcentajes(self, xid, xdias):
        for inscripto in self.__listaInscriptos:
            if inscripto.getIDc() == xid:
                if inscripto.getcantDa() >= xdias:
                    print(f"{inscripto.getDNI()} - {inscripto.getAyN()}")
    
    def inciso3(self, xdni):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            inscripto = self.__listaInscriptos[i]
            if inscripto.getDNI() == xdni:
                print(inscripto.getAyN())
                encontrado = True
            else:
                i += 1
        if not encontrado:
            print("No se encontró el inscripto indicado.")
        else:
            xnota = float(input("Ingrese nota final: "))
            inscripto.setNotaF(xnota)
    
        
    def ordenador(self):
        self.__listaInscriptos.sort()
        
    def listaInscriptos(self, xid, xcantDm):
        for inscripto in self.__listaInscriptos:
            if inscripto.getIDc() == xid and inscripto.getNotaF() >= 7 and inscripto.getcantDa() >= xcantDm:
                print(inscripto)
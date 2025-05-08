from classCancha import Cancha
import csv
import numpy as np

class GestorCancha:
    __listaCanchas: np.ndarray
    __cantidad: int
    __incremento: int
    __dimension: int

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 3
        self.__incremento = 3
        self.__listaCanchas = np.empty(self.__dimension, dtype = Cancha)

    def agregaCancha(self, unaCancha):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaCanchas.resize(self.__dimension)
        self.__listaCanchas[self.__cantidad] = unaCancha
        self.__cantidad += 1

    def leeCancha(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/2024/PO 1/Recuperatorio/Filtrados/Tema 2/Canchas.csv')
        leedor = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in leedor:
            if bandera:
                bandera = False
            else:
                self.agregaCancha(Cancha(fila[0], fila[1], float(fila[2])))
        print("Se cargaron las canchas")
        archivo.close()
    
    def retornaImporte(self, xid):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__listaCanchas[i].getID() == xid:
                importeH = self.__listaCanchas[i].getImporteHora()
                encontrado = True
            else:
                i += 1
        return importeH
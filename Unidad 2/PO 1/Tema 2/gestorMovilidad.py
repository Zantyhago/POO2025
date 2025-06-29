from classMovilidad import Movilidad
import numpy as np
import csv

class GestorMovilidad:
    __listaMovilidades: np.ndarray
    __cantidad: int
    __incremento: int
    __dimension: int

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 2
        self.__incremento = 2
        self.__listaMovilidades = np.empty(self.__dimension, dtype = Movilidad)

    def agregaMovilidad(self, unaMov):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaMovilidades.resize(self.__dimension)
        self.__listaMovilidades[self.__cantidad] = unaMov
        self.__cantidad += 1

    def leeMovilidades(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/movilidades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaMovilidad(Movilidad(fila[0], fila[1], int(fila[2]), float(fila[3]), fila[4], fila[5]))
        print("Se cargaron las movilidades.")
        archivo.close()

    def incisoA(self, gg, xpatente):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__listaMovilidades[i].getPatente() == xpatente:
                print(f"{self.__listaMovilidades[i].getPatente()}  {self.__listaMovilidades[i].getTipo()}  {self.__listaMovilidades[i].getCapacidadTrans()}")
                print(f"{self.__listaMovilidades[i].getImportePat()}  {self.__listaMovilidades[i].getMarca()}  {self.__listaMovilidades[i].getModelo()}")
                print("Gastos")
                print("Fecha            Importe             Descripción")
                subimporte = gg.listaDatos(xpatente)
                print(f"Total de Gastos (incluye Patente): {subimporte + self.__listaMovilidades[i].getImportePat()}")
                encontrado = True
            else:
                i += 1
        if not encontrado:
            print("No se encontró la patente.")
    
    def listaDatazos(self, xpatente):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if xpatente == self.__listaMovilidades[i].getPatente():
                print(self.__listaMovilidades[i])
                encontrado = True
            else:
                i += 1
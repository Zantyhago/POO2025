from classCabaña import Cabaña
import numpy as np
import csv

class GestorCabaña:
    __listaCabañas: np.ndarray
    __cantidad: int
    __incremento: int
    __dimension: int

    def __init__(self):
        self.__dimension = 5
        self.__incremento = 5
        self.__cantidad = 0
        self.__listaCabañas = np.empty(self.__dimension, dtype = Cabaña)
    
    def agregaCabaña(self, unaCabaña):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaCabañas.resize(self.__dimension)
        self.__listaCabañas[self.__cantidad] = unaCabaña
        self.__cantidad += 1
    
    def leeCabañas(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/2024/PO 1/Recuperatorio/Filtrados/Tema 1/Cabañas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaCabaña(Cabaña(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4])))
        print("Se cargaron las cabañas :p")
        archivo.close()
    
    def muestraNumeros(self, xcant, gr):
        indisponibilidad = True
        for i in range(self.__cantidad):
            if self.__listaCabañas[i] >= xcant:
                if gr.BuscaDesocupado(self.__listaCabañas[i].getNumeroC()):
                    print(f"Cabaña numero: {self.__listaCabañas[i].getNumeroC()} dosponible. Capacidad: {self.__listaCabañas[i].getCapacidad()} personas.")
                    indisponibilidad = False
        if indisponibilidad:
            print("No hay cabañas disponibles.")
    
    def getImporteDia(self, xnum):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if xnum == self.__listaCabañas[i]:
                importe = self.__listaCabañas[i].getImporte()
                encontrado = True
            else:
                i+=1
        return importe
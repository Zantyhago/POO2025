import numpy as NANPI
import csv
from classFacultad import Facultad
class GestorFacultad:
    __listaFacus: NANPI.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def __init__(self, dim = 5):
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 1
        self.__listaFacus = NANPI.empty(self.__dimension, dtype = Facultad)

    def agregaFacu(self, unaFacu):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaFacus.resize(self.__dimension)
        self.__listaFacus[self.__cantidad] = unaFacu
        self.__cantidad += 1

    def cargaFacultades(self):
        archivo = open("C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/Ejercicio 4/Facultades.csv")
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaFacu(Facultad(int(fila[0]), fila[1], fila[2], fila[3], fila[4]))
        print("Se cargaron las facultades.")
        archivo.close()
    
    def dadordeNombre(self, xid):
        return self.__listaFacus[xid-1].getNombreFacu()
    
    def mustraOferta(self, gc):
        for i in range(self.__cantidad):
            print(f"Para la {self.__listaFacus[i].getNombreFacu()}:")
            gc.cantidadRaces(self.__listaFacus[i].getCodFacu())
            print("")
    
    def mustraDuracion(self, gc, xnom):
        i = 0
        NotFound = True
        while i < self.__cantidad and NotFound:
            if self.__listaFacus[i].getNombreFacu() == xnom:
                NotFound = False
                print(f"Para la {self.__listaFacus[i].getNombreFacu()}:")
                gc.incisoE(self.__listaFacus[i].getCodFacu())
            else:
                i += 1

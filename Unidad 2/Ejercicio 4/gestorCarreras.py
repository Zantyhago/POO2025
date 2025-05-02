import numpy as NANPI
import csv
from classCarrera import Carrera
class GestorCarrera:
    __listaCarreras: NANPI.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def __init__(self, dim = 5):
        self.__cantidad = 0
        self.__dimension = dim
        self.__incremento = 1
        self.__listaCarreras = NANPI.empty(self.__dimension, dtype = Carrera)

    def agregaCarrera(self, unaCarrera):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaCarreras.resize(self.__dimension)
        self.__listaCarreras[self.__cantidad] = unaCarrera
        self.__cantidad += 1

    def cargaCarreras(self):
        archivo = open("C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/Ejercicio 4/Carreras.csv")
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaCarrera(Carrera(int(fila[0]), fila[1], fila[2], fila[3], fila[4], int(fila[5])))
        print("Se cargaron las carreras.")
        archivo.close()

    def muestraNombre(self, xnomb, gf):
        i = 0
        NoEncontrado = True
        while NoEncontrado and i < len(self.__cantidad):
            if xnomb.lower() == self.__listaCarreras[i].getNombreCarrera().lower():
                nombFacu = gf.dadordeNombre(self.__listaCarreras[i].getCodFacuDic())
                nombCar = self.__listaCarreras[i].getNombreCarrera()    #nombre de la carrera bien escrota
                NoEncontrado = False
            else:
                i += 1
        if NoEncontrado:
            print("No se econtró la carrera ingresada.")
        else:
            print(f"La carrera {nombCar} se dicta en la {nombFacu}.")
            
    def cantidadRaces(self, xid):
        cont = 0
        for i in range(self.__cantidad):
            if xid == self.__listaCarreras[i].getCodFacuDic():
                cont += 1
                print(f"{self.__listaCarreras[i].getNombreCarrera()}")
        print(f"Total: {cont} carreras.")

    def incisoE(self, xid):
        self.__listaCarreras.sort()
        for carrera in self.__listaCarreras:
            if xid == carrera.getCodFacuDic():
                print(carrera)

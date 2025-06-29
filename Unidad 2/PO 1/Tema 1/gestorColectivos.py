from classColectivo import Colectivo
import numpy as anashe
import csv as seceve

class GestorColectivos:
    __cantidad: int
    __dimension: int
    __incremento: int
    __listaColectivos: anashe.ndarray

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 2
        self.__incremento = 2
        self.__listaColectivos = anashe.empty(self.__dimension, Colectivo)

    def agregaColectivo(self, unCol):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaColectivos.resize(self.__dimension)
        self.__listaColectivos[self.__cantidad] = unCol
        self.__cantidad += 1

    def leeColectivos(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/Tema 1/colectivos.csv')
        reader = seceve.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaColectivo(Colectivo(fila[0], fila[1], int(fila[2]), int(fila[3]), fila[4]))
        print("Se leyeron los colectivos.")
        archivo.close()

    def incisoA(self, gt, xdni):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__listaColectivos[i].getDNI() == xdni:
                encontrado = True
                gt.datosA(self.__listaColectivos[i].getPatente())
            else:
                i += 1
        if not encontrado:
            print("No se encontó el Chofer.")
    
    def incisoB(self, gt): # Mostrar por cada colectivo la cantidad total de km recorridos y el gasto estimado en combustible para la cantidad total de km recorrido
        print("Listado de colectivos con sus km y presupuesto:\nPatente:      Cant. de KM recorridos:            Presupuesto:         DNI chofer:")
        for colectivo in self.__listaColectivos:
            cantkm = gt.cuentaKM(colectivo.getPatente())
            #Patente:         Cant. de KM recorridos:            Presupuesto:         DNI chofer:
            print(f"{colectivo.getPatente()}        {cantkm}            {colectivo.getConsumo() * cantkm}           {colectivo.getDNI()}")
from classResultado import Resultado
import numpy as np
import csv

class GestorResultado:
    __listaResultados: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 4
        self.__incremento = 4
        self.__listaResultados = np.empty(self.__dimension, dtype = Resultado)

    def agregaResultado(self, unResultado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaResultados.resize(self.__dimension)
        self.__listaResultados[self.__cantidad] = unResultado
        self.__cantidad += 1

    def leeResultado(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/Recuperatorio/resultadosLiguilla.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaResultado(Resultado(fila[0], fila[1], int(fila[2]), fila[3], int(fila[4])))
        print("Se cargaron los resultados.")
        archivo.close()
#imprimir los equipos (denominación) con los resultados obtenidos en dicha fecha. Al final del listado el importe recaudado por inscripción de los equipos
    def incisoA(self, xfecha, ge):
        subtotal = 0
        for i in range(self.__cantidad):
            if xfecha == self.__listaResultados[i].getFecha():
                subtotal += self.__listaResultados[i].getInscripcion()
                denomLoc = ge.retornaDenom(self.__listaResultados[i].getIDlocal())
                denomVis = ge.retornaDenom(self.__listaResultados[i].getIDvisitante())
                print(f"{denomLoc} ({self.__listaResultados[i].getGolsLocal()}) - ({self.__listaResultados[i].getGolsVisitante()}) {denomVis}")
        print(f"Total recaudado: {subtotal * 2}")
        
##Leer el nombre de un equipo, mostrar los resultados de los partidos de local que jugó, indicando el nombre del equipo contrincante y el resultado
    def muestraResults(self, ge, xid, xnom):
        print(f"Lista de resultados localaes para {xnom}")
        for i in range(self.__cantidad):
            if self.__listaResultados[i].getIDlocal() == xid:
                denomVist = ge.retornaDenom(self.__listaResultados[i].getIDvisitante())
                print(f"{self.__listaResultados[i].getGolsLocal()} - {self.__listaResultados[i].getGolsVisitante()} {denomVist}")

    def incisoC(self, ge):
        for i in range(self.__cantidad):
            gl = self.__listaResultados[i].getGolsLocal()
            gv = self.__listaResultados[i].getGolsVisitante()
            if self.__listaResultados[i].getGolsLocal() == self.__listaResultados[i].getGolsVisitante():
                puntosLoc = 1
                puntosVis = 1
            elif self.__listaResultados[i].getGolsLocal() > self.__listaResultados[i].getGolsVisitante():
                puntosLoc = 3
                puntosVis = 0
            elif self.__listaResultados[i].getGolsLocal() < self.__listaResultados[i].getGolsVisitante():
                puntosLoc = 0
                puntosVis = 3
            ge.seteador(self.__listaResultados[i].getIDlocal(), puntosLoc, gl, gv)
            ge.seteador(self.__listaResultados[i].getIDvisitante(), puntosVis, gl, gv)
        ge.muestratabla()
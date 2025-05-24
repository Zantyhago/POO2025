#python
from classEquipo import Equipo
import csv

class GestorEquipo:
    __listaEquipos: list

    def __init__(self):
        self.__listaEquipos = []

    def agregaEquipo(self, unEquipo):
        self.__listaEquipos.append(unEquipo)

    def leeEquipo(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/Recuperatorio/equiposLiguilla.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaEquipo(Equipo(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6])))
        print("Se cargaron los equipos.")
        archivo.close()

    def retornaDenom(self, xid):
        i = 0
        encontrado = False
        while i<len(self.__listaEquipos) and not encontrado:
            if xid == self.__listaEquipos[i].getID():
                denom = self.__listaEquipos[i].getDenominacion()
                encontrado = True
            else:
                i += 1
        return denom

    def incisoB(self, gr, xnom):
        i = 0
        encontrado = False
        while i<len(self.__listaEquipos) and not encontrado:
            if xnom == self.__listaEquipos[i].getDenominacion():
                encontrado = True
                gr.muestraResults(self, self.__listaEquipos[i].getID(), xnom)
            else:
                i += 1

    def seteador(self, xid, xpuntos, gl, gv):
        i = 0
        encontrado = False
        tope = len(self.__listaEquipos)
        while i < tope and not encontrado:
            if self.__listaEquipos[i].getID() == xid:
                encontrado = True
                self.__listaEquipos[i].setPuntos(xpuntos)
                self.__listaEquipos[i].setgetGolesAFavor(gl)
                self.__listaEquipos[i].setgetGolesContra(gv)
                diferencia = gl - gv
                self.__listaEquipos[i].setDiferencia(diferencia)
            else:
                i += 1
    
    def muestratabla(self):
        self.__listaEquipos.sort(reverse=True)
        i = 0
        print("Listado solicitado:")
        print("Posición Equipo                 Puntos      Goles a Favor       Goles en Contra     Diferencia de goles")
        for equipo in self.__listaEquipos:
            print(f"{i}.       {equipo}")
            i+=1

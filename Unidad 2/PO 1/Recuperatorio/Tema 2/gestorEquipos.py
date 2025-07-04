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
        archivo = open('equiposLiguilla.csv')
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

    def seteador(self, xid, pts, gl, gv):
        i = 0
        encontrado = False
        while i < len(self.__listaEquipos) and not encontrado:
            if self.__listaEquipos[i].getID() == xid:
                encontrado = True
                self.__listaEquipos[i].setPuntos(pts)
                self.__listaEquipos[i].setgetGolesAFavor(gl)
                self.__listaEquipos[i].setgetGolesContra(gv)
                diferencia = gl - gv
                self.__listaEquipos[i].setDiferencia(diferencia)
            else:
                i += 1
    
    def cereador(self): #reestablece los valores porque cada vez que muestra la tabla se van sumando los mismos
        for equipo in self.__listaEquipos:
                equipo.setPuntos(-1)
                equipo.setgetGolesAFavor(-1)
                equipo.setgetGolesContra(-1)
                equipo.setDiferencia(-1)
    
    def muestratabla(self):
        self.__listaEquipos.sort(reverse=True)
        i = 1
        print("Listado solicitado:")
        print(f"{'Posición':<10}{'Equipo':<26}{'Puntos':<6}   {'Goles a Favor':<13}   {'Goles en Contra':<15}   {'Diferencia de goles':<19}")
        for equipo in self.__listaEquipos:
            print(f"{i}.       {equipo}")
            i+=1

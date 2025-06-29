from classTramo import Tramo
import csv as seceve

class GestorTramos:
    __listaTramos: list

    def __init__(self):
        self.__listaTramos = []
    
    def agregaTramo(self, unTramo):
        self.__listaTramos.append(unTramo)

    def leeTramos(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/Tema 1/tramos.csv')
        reader = seceve.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaTramo(Tramo(fila[0], fila[1], float(fila[2]), fila[3]))
        print("Se leyeron los tramos.")
        archivo.close()

    def datosA(self, xpatente):
        cantKm = 0
        for tramo in self.__listaTramos:
            if tramo.getPatente() == xpatente:
                cantKm += tramo.getDistanciaKM()
                print(f"{tramo.getOrigen()} - {tramo.getDestino()} - {tramo.getDistanciaKM()}")
        print(f"Kilómetros totales: {cantKm}")

    def cuentaKM(self, xpat):
        cantKM = 0
        for tramo in self.__listaTramos:
            if tramo.getPatente() == xpat:
                cantKM += tramo.getDistanciaKM()
        return cantKM
    
    def incisoC(self, cantKm):
        for tramo in self.__listaTramos:
            if tramo > cantKm:
                print(f"{tramo.getOrigen()} - {tramo.getDestino()} - {tramo.getPatente()}")
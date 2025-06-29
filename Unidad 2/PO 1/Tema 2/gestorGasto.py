from classGasto import Gasto
import csv
class GestorGasto:
    __listaGastos: list

    def __init__(self):
        self.__listaGastos = []

    def agregarGasto(self, unGasto):
        self.__listaGastos.append(unGasto)
    
    def leeGastos(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/gastosAbril2025.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregarGasto(Gasto(fila[0], fila[1], float(fila[2]), (fila[3])))
        print("Se cargaron los gastos.")
        archivo.close()
    
    def listaDatos(self, xpatente):
        importe = 0
        for gasto in self.__listaGastos:
            if gasto.getPatente().lower() == xpatente.lower():
                print(f"{gasto.getFecha()}          {gasto.getImpGasto()}           {gasto.getDescripcion()}")
                importe += gasto.getImpGasto()
        return importe
    
    def incisoB(self, xfecha):
        cant = 0
        for gasto in self.__listaGastos:
            if gasto.getFecha() == xfecha:
                cant += gasto.getImpGasto()
        print(f"Gastos para fecha {xfecha}: {cant}")

    def incisoC(self, xfecha, gm):
        self.__listaGastos.sort()
        i = 0
        while i < len(self.__listaGastos):
            if self.__listaGastos[i].getFecha() == xfecha:
                gm.listaDatazos(self.__listaGastos[i].getPatente())
            i += 1
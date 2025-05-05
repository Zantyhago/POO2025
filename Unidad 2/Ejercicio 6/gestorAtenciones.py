import csv as seeseve
import numpy as nanpi
from classAtenciones import Atenciones
class ManejadorAtencioes:
    __incremento: int
    __cantidad: int
    __dimension: int
    __listaPacientes: nanpi.ndarray

    def __init__(self):
        self.__dimension = 8
        self.__incremento = 8
        self.__cantidad = 0
        self.__listaAtts = nanpi.empty(self.__dimension, dtype = Atenciones)
    
    def AgregarAtencion(self, unaAtencion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaAtts.resize(self.__dimension)
        self.__listaAtts[self.__cantidad] = unaAtencion
        self.__cantidad += 1

    def cargaAtenciones(self):
        archivo = open('atenciones.csv')
        reader = seeseve.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.AgregarAtencion(Atenciones(int(fila[0]), fila[1], float(fila[2])))
        archivo.close()
    
    def incisoA(self, xfecha, gp):
        impTotal = 0
        cant = 0
        print(f"Datos para la fecha {xfecha}:")
        for i in range(self.__cantidad):
            if self.__listaAtts[i].getFecha() == xfecha:
                cant += 1
                impTotal += self.__listaAtts[i].getImporte()
        print(f"Hubieron {cant} atenciones. Importe total requerido: ${impTotal}")

    def incisoB(self, xdni, gp):
        NoEncontrado = True
        cont = 0
        for i in range(self.__cantidad):
            if self.__listaAtts[i].getDNIat() == xdni:
                NoEncontrado = False
                cont += 1
        if NoEncontrado:
            print("No se encontró el DNI proveído.")
        else:
            nombre = gp.retornaname(xdni)
            print(f"El paciente {nombre} tuvo {cont} atenciones.")
    
    def buscaAtencion(self, xdni):
        encontrado = False
        i = 0
        while i < self.__cantidad and not encontrado:
            if self.__listaAtts[i]. getDNIat() == xdni:
                encontrado = True
            else:
                i += 1
        return encontrado
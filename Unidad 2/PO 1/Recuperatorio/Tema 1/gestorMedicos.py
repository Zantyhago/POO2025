from classMedico import Medico
import numpy as np
import csv

class GestorMedicos:
    __cantidad: int
    __dimension: int
    __incremento: int
    __listaMedicos: np.ndarray

    def __init__(self, xcant = 3):
        self.__cantidad = 0
        self.__dimension = xcant
        self.__incremento = 1
        self.__listaMedicos = np.empty(self.__dimension, dtype = Medico)
    
    def agregaMedico(self, unMed):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaMedicos.resize(self.__dimension)
        self.__listaMedicos[self.__cantidad] = unMed
        self.__cantidad += 1

    def leeMedicos(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/Recuperatorio/Tema 1/medicos.csv', encoding = 'utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            self.agregaMedico(Medico(fila[0], fila[1], fila[2], fila[3], fila[4]))
        archivo.close()
        print("se cargaron los medicos.")

    def buscaName(self, xdni):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__listaMedicos[i].getDNI() == xdni:
                encontrado = self.__listaMedicos[i].getNombre()
            else:
                i += 1
        return encontrado
    
    #Mostrar  para  cada  médico:  nombre  completo,  especialidad,  zona  de cobertura, total de visitas realizadas, e importe total a facturar (visitas realizadas * valor fijo por visita).
    def incisoB(self, gv):
        for medico in self.__listaMedicos:
            cant = gv.cantVisitas(medico.getDNI())
            importe = cant * medico.getPrecio()
            print(f"NyA: {medico.getNombre()}\n- Especialidad: {medico.getEspecialidad()}\n- Zona: {medico.getZona()}\n- Cantidad de visitas: {cant}\n- Importe a cobrar: {importe}\n\n")
            
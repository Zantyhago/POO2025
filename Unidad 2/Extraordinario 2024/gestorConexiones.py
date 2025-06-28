from classConexion import Conexion
import csv
import numpy as nanpi
class GestorConexiones:
    __dimension: int
    __cantidad: int
    __incremento: int
    __listaConexiones: nanpi.ndarray

    def __init__(self):
        self.__dimension = 6
        self.__cantidad = 0
        self.__incremento = 6
        self.__listaConexiones = nanpi.empty(self.__dimension, dtype = Conexion)

    def agregaConexion(self, unaConex):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaConexiones.resize(self.__dimension)
        self.__listaConexiones[self.__cantidad] = unaConex
        self.__cantidad += 1

    def leeConexion(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/2024/PO 1/Extraordinario/conexiones.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            self.agregaConexion(Conexion(fila[0], fila[1], fila[2], fila[3], int(fila[4]), int(fila[5])))
        archivo.close()
        print("Se cargaron las conexiones.")

    def muestradatitos(self, xid, TLimit, precioBase, porcentaje):
        horasT = 0
        horasExc = 0
        conexion = False
        print(f"IP:                Fecha:         Hora inic.:      Hora fin.: ")
        for i in range(self.__cantidad):
            if self.__listaConexiones[i].getIDj() == xid:
                conexion = self.__listaConexiones[i]
                horasT += conexion.getHoraF() - conexion.getHoraI()
                print(f"{conexion.getIP()}     {conexion.getFecha()}     {conexion.getHoraI()}                {conexion.getHoraF()}")
        if conexion:
            if horasT > TLimit:        
                horasExc = horasT - TLimit
            costoBase = (horasT - horasExc) * precioBase
            costoAd = precioBase * horasExc * porcentaje
            print(f"Total horas: {horasT}                           Horas en exceso: {horasExc}")
            print(f"Importe a facturar: {costoBase + costoAd}")
        else:
            print(f"El/la usuario no se conectó.")

    def incisoB(self, gg, xnom):
        conexion = False
        nadie = False
        encabezado = False
        for i in range(self.__cantidad):
            if self.__listaConexiones[i].getNombreJ().lower() == xnom.lower():
                conexion = self.__listaConexiones[i]
                if not encabezado:
                    print(f"Titulo original: {conexion.getNombreJ()}\n- IP:                 -NyA:               Alias:       -Plan:")
                    encabezado = True
                if gg.muestraotrosdatos(conexion.getIP(), conexion.getIDj()):
                    nadie = True
        if not conexion:
            print("No se encontró el juego.")
        if not nadie:
            print(f"Nadie jugó el juego indicado.")

    def ordenador(self,):
        self.__listaConexiones.sort()
    
    def listadoBasicos(self, xid):
        bandera = False
        i = 0
        for i in range(self.__cantidad):
            conexionA = self.__listaConexiones[i]
            if conexionA.getIDj() == xid:
                for j in range(self.__cantidad):
                    if i != j:
                        conexionB = self.__listaConexiones[j]
                        if conexionB.getIDj() == xid and conexionA == conexionB:
                                bandera = True
        return bandera
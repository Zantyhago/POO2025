from classAlquiler import Alquiler
import csv

class GestorAlquiler:
    __listaAlquileres: list

    def __init__(self):
        self.__listaAlquileres = []

    def agregaAlquiler(self, unAlquiler):
        self.__listaAlquileres.append(unAlquiler)

    def leeAlquiler(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/2024/PO 1/Recuperatorio/Filtrados/Tema 2/Alquiler.csv')
        leedor = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in leedor:
            if bandera:
                bandera = False
            else:
                self.agregaAlquiler(Alquiler(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4])))
        print("Se cargaron los alquileres")
        archivo.close()

    def listaAlquileres(self, gc):
        self.__listaAlquileres.sort()
        recaudado = 0
        print("Hora - Id de Cancha - Duración alquiler - Importe por hora - Importe alquiler")
        for alquiler in self.__listaAlquileres:
            impHora = gc.retornaImporte(alquiler.getCancha())
            duracion = alquiler.getDuracion()/60
            importeAlquiler = impHora * duracion
            print(f"{alquiler.getHora()} | {alquiler.getCancha()} | {duracion} | {impHora} | {importeAlquiler}")
            recaudado += importeAlquiler
        print(f"Total recaudado: {recaudado}")
    
    def cantAlquilada(self, xid):
        cant = 0
        for alquiler in self.__listaAlquileres:
            if alquiler.getCancha() == xid:
                cant += alquiler.getDuracion()
        print(f"La cancha {xid} estuvo {cant} minutos alquilada.")
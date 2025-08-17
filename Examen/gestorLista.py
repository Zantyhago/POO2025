from classNodo import Nodo
from classElectrico import Electrico
from classBateria import Bateria
from classColectivo import Colectivo
import csv

class GestorLista:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __indice: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__indice += 1
            self.__actual = self.__actual.getSiguiente()
            return dato
        
    def agregaVehiculo(self, unVehi):
        nodo = Nodo(unVehi)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        self.__actual = nodo
        
    def agregaVehiculoManual(self):
        vehiculo = None
        xtipo = input("Ingrese tipo de vehículo (E/C): ").lower()
        if xtipo in ['e', 'c']:
            xpatente = input("Ingrese patente: ")
            xcapacidadP = int(input("Ingrese capacidad de pasajeros: "))
            xkmRecorr = float(input("Ingrese KM a recorrer: "))
            if xtipo == 'c':
                xemp = input("Ingrese empresa: ")    
                xcapacidadC = float(input("Ingrese capacidad de combustile: "))
                xtipoC = input("Ingrese tipo de combustible: ")
                vehiculo = Colectivo(xpatente, xcapacidadP, xkmRecorr, xemp, xcapacidadC, xtipoC)
                print("Se agregó un colectivo a la lista.")
            elif xtipo == 'e':
                xauton = int(input("Ingrese autonomía: "))
                xefic = float(input("Ingrese consumo energético por km: "))
                electric = Electrico(xpatente, xcapacidadP, xkmRecorr, xauton, xefic)
                bandera = 'sis'
                while bandera != 'no':
                    xcapacidadKWH = float(input("Ingrese capacidad de kwh: "))
                    xcargaActu = float(input("Ingrese carga actual: "))
                    electric.agregaBaterias(Bateria(xpatente, xcapacidadKWH, xcargaActu))
                    bandera = input("Agregar mas baterias? ('no' para finalizar): ").lower()       
                print("Se agregó un auto eléctrico a la lista.")
                vehiculo = electric
        else:
            raise TypeError("Tipo de vehículo mal ingresado.")
        return vehiculo
    
    def leeVehiculos(self):
        ArchiVehiculos = open('Vehiculos.csv', encoding = 'utf-8')
        ArchiBaterias = open('Baterias.csv', encoding = 'utf-8')
        readerVehi = csv.reader(ArchiVehiculos, delimiter = ';')
        readerBat = csv.reader(ArchiBaterias, delimiter = ';')
        next(ArchiVehiculos)
        next(ArchiBaterias)
        for filaV in readerVehi:
            if filaV[0] == 'C':
                self.agregaVehiculo(Colectivo(filaV[1], int(filaV[2]), float(filaV[3]), filaV[4], float(filaV[5]), filaV[6]))
            elif filaV[0] == 'E':
                electric = Electrico(filaV[1], int(filaV[2]), float(filaV[3]), int(filaV[4]), float(filaV[5]))
                for filaB in readerBat:
                    if filaB[0] == filaV[1]:
                        electric.agregaBaterias(Bateria(filaB[0], float(filaB[1]), float(filaB[2])))
                ArchiBaterias.seek(0)
                self.agregaVehiculo(electric)
        ArchiBaterias.close()
        ArchiVehiculos.close()
        print("Se cargaron los vehículos.")
    
    def inciso2(self, xdistancia): # arreglar
        encabezado = False
        for vehiculoE in self:
            if isinstance(vehiculoE, Electrico):
                if xdistancia <= vehiculoE.buscaCapacidad():
                    if not encabezado:
                        print("Patentes que pueden recorrer la distancia:")
                        encabezado = True
                    print(vehiculoE.getPatente())
        if not encabezado:
            print("No hay vehículos eléctricos que puedan recorrer dicha distancia.")
                
    def inciso3(self):
        for vehiculo in self:
            if isinstance(vehiculo, Colectivo):
                print(f"{vehiculo}\n - Colectivo")
            elif isinstance(vehiculo, Electrico):
                print(f"{vehiculo}\n - Eléctrico")
    
    def inciso4(self, xindice):
        if xindice < 0 or xindice > self.__tope:
            raise IndexError("Índice fuera de rango.")
        else:
            vehiculo = self.agregaVehiculoManual()
            nodo = Nodo(vehiculo)
            if xindice == 0:
                self.agregaVehiculo(vehiculo)
            else:
                aux = self.__comienzo
                for i in range(xindice-1):
                    aux = aux.getSiguiente()
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                self.__tope += 1

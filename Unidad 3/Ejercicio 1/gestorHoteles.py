from classHabitacion import Habitacion
from classHotel import Hotel
import csv

class GestorHoteles:
    __listaHoteles: list

    def __init__(self):
        self.__listaHoteles = []

    def agregaHotel(self, unHotel):
        self.__listaHoteles.append(unHotel)

    def leeDatos(self):
        archivo = open('Hoteles.csv')
        reader = csv.reader(archivo, delimiter = ';')
        i = -1
        for fila in reader:
            if len(fila) == 3:
                self.agregaHotel(Hotel(fila[0], fila[1], fila[2]))
                i += 1
            else:
                if fila[4].lower() == 'true':
                    disp = True
                else:
                    disp = False
                self.__listaHoteles[i].agregaHabitacion(int(fila[0]), int(fila[1]), fila[2], float(fila[3]), disp)
        print("Se cargaron los datos.")

    def buscaPorNombre(self, xnom):
        i = 0
        encontrado = False
        while i< len(self.__listaHoteles) and not encontrado:
            if self.__listaHoteles[i].getNombre().lower() == xnom.lower():
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError
        return i

    def Inciso1(self, xnomb):
        indice = self.buscaPorNombre(xnomb)
        xnum = int(input("Ingrese el numero: "))
        xpiso = int(input("Ingrese piso: "))
        xtipo = input("Ingrese tipo: ")
        xprec = float(input("Ingrese precio por noche: "))
        self.__listaHoteles[indice].agregaHabitacion(xnum, xpiso, xtipo, xprec)
        self.__listaHoteles[indice].ordenador()
        print("Habitacion agregada.")
    
    def inciso2(self, xnom, xnum):
        indice = self.buscaPorNombre(xnom)
        subindice = self.__listaHoteles[indice].buscaPorNum(xnum)
        disponible = self.__listaHoteles[indice].getttterDisp(subindice)
        if disponible == True:
            self.__listaHoteles[indice].setttterDisponib(subindice, 0)
            print(f"Habitación {xnum} reservada exitosamente anasheee.")
        else:
            print(f"Habitación {xnum} ya reservada.")

    def Inciso3(self, xnom, xnum):
        indice = self.buscaPorNombre(xnom)
        subindice = self.__listaHoteles[indice].buscaPorNum(xnum)
        self.__listaHoteles[indice].setttterDisponib(subindice, 1)
        print(f"Habitación {xnum} liberada.")

    def inciso4(self, xtipo):
        for hotel in self.__listaHoteles:
            hotel.muestraTipos(xtipo, hotel.getNombre())

    def inciso5(self):
        for hotel in self.__listaHoteles:
            hotel.muestraLibres()
        
    def inciso6(self):
        for tipo in ['doble','sencilla','suite']:
            print(f"Tipo de habitacion: {tipo}")
            for hotel in self.__listaHoteles:
                hotel.listaInfo(tipo)

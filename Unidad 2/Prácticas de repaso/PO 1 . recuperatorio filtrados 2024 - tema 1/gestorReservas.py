from classReserva import Reserva
import csv

class GestorReserva:
    __listaReservas: list

    def __init__(self):
        self.__listaReservas = []

    def agregaReserva(self, unaReserva):
        self.__listaReservas.append(unaReserva)

    def leeReserva(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/2024/PO 1/Recuperatorio/Filtrados/Tema 1/Reservas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaReserva(Reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), float(fila[6])))
        print("Se cargaron las reservas c:")
        archivo.close()

    def BuscaDesocupado(self, xnum):
        i = 0
        encontrado = False
        while i < len(self.__listaReservas) and not encontrado:
            if self.__listaReservas[i].getCabana() == xnum:
                encontrado = True
            else:
                i+=1
        return encontrado
    
    def BuscaFecha(self, gc, xfecha):
        print("N° de Cabaña - Imp. or día - Cant. de días - Seña - Imp. a cobrar")
        for reserva in self.__listaReservas:
            if reserva == xfecha:
                impDiario = gc.getImporteDia(reserva.getCabana())
                ImpTotal = (reserva.getCantDias() * impDiario) - reserva.getSena()
                print(f"{reserva.getCabana()} - {impDiario} - {reserva.getCantDias()} - {reserva.getSena()} - {ImpTotal}")

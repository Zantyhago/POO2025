from classPrograma import ProgramaCapacitacion
import csv

class GestorProgramas:
    __listaProgramas: list

    def __init__(self):
        self.__listaProgramas = []

    def agregaPrograma(self, unProg):
        self.__listaProgramas.append(unProg)

    def leeProgramas(self):
        archivo = open('programas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaPrograma(ProgramaCapacitacion(fila[0], fila[1], int(fila[2])))
        archivo.close()
        print("Se cargaron los programas.")

    def buscaPPorNombre(self, xnombre):
        i = 0
        encontrado = False
        while i < len(self.__listaProgramas) and not encontrado:
            if xnombre.lower() == self.__listaProgramas[i].getNombre().lower():
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError
        return self.__listaProgramas[i]

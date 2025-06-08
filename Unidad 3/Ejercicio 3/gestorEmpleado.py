from classEmpleado import Empleado
import csv

class GestorEmpleados:
    __listaEmpleados: list

    def __init__(self):
        self.__listaEmpleados = []

    def agregaEmpleado(self, unEmp):
        self.__listaEmpleados.append(unEmp)

    def leeEmpleados(self):
        archivo = open('empleados.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaEmpleado(Empleado(fila[0], int(fila[1]), fila[2]))
        archivo.close()
        print("Se cargaron los empleados.")

    def buscaEPorNombre(self, xnombre):
        i = 0
        encontrado = False
        while i < len(self.__listaEmpleados) and not encontrado:
            if xnombre.lower() == self.__listaEmpleados[i].getNyA().lower():
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError
        return self.__listaEmpleados[i]       
    
    def inciso3(self, gm):
        print("Empleado/s que no está/n incripto/s en ningún programa:")
        i = 1
        for empleado in self.__listaEmpleados:
            inscripto = gm.buscaInscripcion(empleado.getIDemleado())
            if not inscripto:
                print(f"{i}. {empleado}")
                i += 1

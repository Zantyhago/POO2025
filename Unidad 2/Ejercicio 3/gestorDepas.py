import csv
from classDepa import Departamento
class GestorDepartamento:
    __departamentos: list

    def __init__(self):
        self.__departamentos = []

    def agregaDepartamento(self, unDepa):
        self.__departamentos.append(unDepa)

    def leeDepartamentos(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/Ejercicio 2/Departamentos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregaDepartamento(Departamento(int(fila[0]), fila[1]))
        archivo.close()
    
    def muestraAccisMes(self, j, accidentes):
        for depa in self.__departamentos:
            print(f'''Nombre del departamento: {depa.getNombre()}.
                  Cantidad de Accidentes en el mes {j}: {accidentes.getAccidentes(depa.getID(),j)}''')
            
    def muestraMayorCant(self, mes, accidentes):
        i = accidentes.buscaIndiceMayor(mes)
        print(f"El departamento {self.__departamentos[i].getNombre()} registro la mayor cantidad de accidentes: {accidentes.getAccidentes(i+1,mes)}")

    def buscaIndice(self, xnombre):
        encontrado = True
        i = 0
        while encontrado and i < len(self.__departamentos):
            if xnombre == self.__departamentos[i].getNombre():
                encontrado = False
                indice = i
            else:
                i += 1
        return indice
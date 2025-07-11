from classTelefonia import Telefonia
from classTelevision import Television
import csv

class GestorPlanes:
    __listaPlanes: list

    def __init__(self):
        self.__listaPlanes = []

    def agregaPlan(self, planero):
        self.__listaPlanes.append(planero)

    def leePlanes(self):
        archivo = open('planes.csv', encoding = 'utf-8')
        reader = csv.reader(archivo, delimiter = ';')    
        next(reader)
        for fila in reader:
            if fila[0] == 'M':
                self.agregaPlan(Telefonia(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6])))
            elif fila[0] == 'T':
                self.agregaPlan(Television(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6])))
        archivo.close()
        print("Se cargaron los planes.")

    def inciso1(self, xi):
        j = 0
        encontrado = False
        while j < len(self.__listaPlanes) and not encontrado:
            if j == xi-1:
                encontrado = True
                plan = self.__listaPlanes[j]
                if isinstance(plan, Telefonia):
                    print(f"La componente en la posición {xi} es de tipo Telefonía.")
                elif isinstance(plan, Television):
                    print(f"La componente en la posición {xi} es de tipo Televisión.")
            else:
                j += 1
        if not encontrado:
            raise IndexError
        return

    def inciso2(self, xcob):
        cantM = 0
        cantT = 0
        for plan in self.__listaPlanes:
            if plan.getCobertura().lower() == xcob.lower():
                if isinstance(plan, Telefonia):
                    cantM += 1
                if isinstance(plan, Television):
                    cantT += 1
        print(f"Hay un total de {cantM + cantT} plan/es con la cobertura {xcob}.")
        print(f"Con {cantM} de Telefonía y {cantT} de Televisión.")

    def inciso3(self, xcant):
        cero = True
        for plan in self.__listaPlanes:
            if isinstance(plan, Television) and plan.getCanInt() >= xcant:
                print(f"{plan.getCompañia()} ofrece {plan.getCanInt()} canales.")
                cero = False
        if cero:
            raise IndexError
        
    
    def inciso4(self):
        print(f"{'Tipo de Plan:':<15}{'Compañia:':<19}{'Duración:':<11}{'Cobertura:':<27}{'Precio final:'}")
        for plan in self.__listaPlanes:
            print(plan)
import csv as seeseve
from classPaciente import Paciente
class ManejadorPacientes:
    __listaPacs: list

    def __init__(self):
        self.__listaPacs = []
    
    def agregarPaciente(self, unPaciente):
        self.__listaPacs.append(unPaciente)
    
    def cargaPacientes(self):
        archivo = open('pacientes.csv')
        reader = seeseve.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregarPaciente(Paciente(int(fila[0]), fila[1], fila[2]))
        archivo.close()
    
    def retornaname(self, xdni):
        i = 0
        bandera = True
        while i < len(self.__listaPacs) and bandera:
            if xdni == self.__listaPacs[i].getDNI():
                xname = self.__listaPacs[i].getNombre()
                bandera = False
            else:
                i+=1
        return xname
    
    def incisoC(self, ga):
        for paciente in self.__listaPacs:
            if not ga.buscaAtencion(paciente.getDNI()):
                print(f"El paciente {paciente.getNombre()} no tuvo atenciones.")
    
    def incisoD(self):
        self.__listaPacs.sort()
        print("Pacientes (AyN - DNI - Unidad):")
        for paciente in self.__listaPacs:
            print(paciente)
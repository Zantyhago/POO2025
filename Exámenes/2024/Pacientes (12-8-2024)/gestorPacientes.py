from classHospis import PacHospitalizado
from classObreSoc import PacObraSocial
from classPaciente import Paciente
from classNodo import Nodo
import csv

class GestorPacientes:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __indice: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            self.__indice += 1 
            return dato
        
    def agregaPorCola(self, unPaciente):
        NuevoNodo = Nodo(unPaciente)
        aux = self.__comienzo
        if self.__comienzo is None:
            self.__comienzo = NuevoNodo
            self.__actual = NuevoNodo
        else:
            while aux.getSiguiente() is not None:
                aux = aux.getSiguiente()
            aux.setSiguiente(NuevoNodo)
        self.__tope += 1

    def leePacientes(self):
        archivo = open('pacientes.csv', encoding = 'utf-8')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            if fila[0] == 'P':
                self.agregaPorCola(Paciente(fila[1], fila[2], fila[3], fila[4]))
            elif fila[0] == 'O':
                self.agregaPorCola(PacObraSocial(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))
            elif fila[0] == 'H':
                self.agregaPorCola(PacHospitalizado(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], float(fila[9])))
        archivo.close()
        print("Pacientes agregados a la lista ashei.")

    def incisoB(self):
        cantNeumoniaticos = 0
        cant = 0
        for paciente in self:
            if isinstance(paciente, PacHospitalizado) and paciente.getDiagnostico() == 'Neumonía':
                cantNeumoniaticos += 1
            else:
                cant += 1
        print(f"Cantidad de pac. hosp. con neumonía: {cantNeumoniaticos}\nCantidad de pacientes totales: {cant + cantNeumoniaticos}") # ni idea acá exactamente xd

    def incisoC(self):
        unPaciente = self.__comienzo.getDato()
        print(f"Monto cobrado a todos los pacientes: {unPaciente.getValorCons():.2f} pesos")
        print(f"Total recaudado: {unPaciente.getValorCons() * self.__tope:.2f} pesos.")

    def incisoD(self, xindice):
        if xindice < 0 or xindice > self.__tope:
            raise IndexError("Índice fuera de rango.")
        else:
            aux = self.__comienzo
            for i in range(xindice):
                aux = aux.getSiguiente()
            if isinstance(aux.getDato(), PacHospitalizado):
                print(f'EL paciente {aux.getDato().getNyA()} es de tipo "Paciente Hospitalizado".')
            elif isinstance(aux.getDato(), PacObraSocial):
                print(f'EL paciente {aux.getDato().getNyA()} es de tipo "Paciente con Obra Social".')
            else:
                print(f'EL paciente {aux.getDato().getNyA()} es de tipo "Paciente" :v') # acá tampoco

    def incisoE(self, xmonto):
        Paciente.setValorCons(xmonto)
        self.incisoC()
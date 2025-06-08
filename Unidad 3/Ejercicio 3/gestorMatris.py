from classMatricula import Matricula
import csv

class GestorMatriculas:
    __listaMatriculas: list

    def __init__(self):
        self.__listaMatriculas = []

    def agregaMatricula(self, unaMatri):
        self.__listaMatriculas.append(unaMatri)

    def leeMatriculas(self, ge, gp):
        archivo = open('matriculas.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                empleado = ge.buscaEPorNombre(fila[1])
                programa = gp.buscaPPorNombre(fila[2])
                self.agregaMatricula(Matricula(fila[0], empleado, programa))
        archivo.close()
        print("Se cargaron las matriculas.")

    def inciso1(self, xid):
        datos = False
        durTot = 0
        for matri in self.__listaMatriculas:
            if xid == matri.getEmpleado().getIDemleado():
                if not datos:
                    print(f"Empleado: {matri.getEmpleado().getNyA()}\nPrograma/s:")
                    datos = True
                print(f"{matri.getPrograma().getNombre()} - Duración: {matri.getPrograma().getDuracion()}")
                durTot += matri.getPrograma().getDuracion()
        if durTot == 0:
            raise IndexError
        print(f"Duración total: {durTot}")
        
    def inciso2(self, xnomb):
        datos = False
        i = 1
        for matri in self.__listaMatriculas:
            if xnomb.lower() == matri.getPrograma().getNombre().lower():
                if not datos:
                    print(f"Empleados inscriptos a {matri.getPrograma().getNombre()}:")
                    datos = True
                print(f"{i}. {matri.getEmpleado()}")
                i+=1
        if not datos:
            raise IndexError

    def buscaInscripcion(self, xid):
        i = 0
        inscripto = False
        while i<len(self.__listaMatriculas) and not inscripto:
            matri = self.__listaMatriculas[i]
            if xid == matri.getEmpleado().getIDemleado():
                inscripto = True
            else:
                i += 1
        return inscripto

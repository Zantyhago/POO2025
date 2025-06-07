from classMatricula import Matricula
import csv

class GestorMatriculas:
    __listaMatriculas: list

    def __init__(self):
        self.__listaMatriculas = []

    def agregaMatricula(self, unaMatri):
        self.__listaMatriculas.append(unaMatri)

    def leeMatriculas(self, ge, gp):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 3/Ejercicio 3/matriculas.csv', encoding='utf-8')
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

    def inciso1(self, xid): #Dado  el  Id  del  empleado,  informe  la  duración  de  todos  los  programas  de capacitación en los que está matriculado.
        datos = False
        durTot = 0
        for matri in self.__listaMatriculas:
            if xid == matri.getEmpleado().getIDemleado():
                if not datos:
                    print(f"Empleado: {matri.getEmpleado().getNyA()}\nPrograma/s:")
                    datos = True
                print(f"{matri.getPrograma().getNombre()} - Duración: {matri.getPrograma().getDuracion()}")
                durTot += matri.getPrograma().getDuracion()
        print(f"Duración total: {durTot}")  #hacer exepcion en el caso infeliz
        
    def inciso2(self, xnomb):  #Dado el nombre de un programa de  capacitación, muestre el/los empleados matriculados en el mismo.
        datos = False
        for matri in self.__listaMatriculas:
            if xnomb.lower() == matri.getPrograma().getNombre().lower():    #hacer exepcion en el caso infeliz
                if not datos:
                    print(f"Empleados inscriptos a {matri.getPrograma().getNombre()}:")
                    datos = True
                #print(f"NyA: {matri.getEmpleado().getNyA()} - ID: {matri.getEmpleado().getIDemleado()}")
                print(matri.getEmpleado())

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
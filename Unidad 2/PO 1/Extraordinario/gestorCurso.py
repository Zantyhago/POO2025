from classCurso import Curso
import csv
class GestorCurso:
    __listaCursos: list
    
    def __init__(self):
        self.__listaCursos = []
        
    def agregaCurso(self, unCurso):
        self.__listaCursos.append(unCurso)
        
    def leeCursos(self):
        archivo = open('cursos.csv', encoding = 'utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            self.agregaCurso(Curso(int(fila[0]), fila[1], int(fila[2]), int(fila[3]), int(fila[4])))
        archivo.close()
        print("Se cargaron los cursos.")

    def inciso2(self, gi, xid):
        i = 0
        encontrado = False
        while i < len(self.__listaCursos) and not encontrado:
            curso = self.__listaCursos[i]
            if curso.getID() == xid:
                encontrado = True
                print(curso.getDenominacion())
                cantDiasM = curso.getCantD() * 0.7
                gi.muestraPorcentajes(xid, cantDiasM)
            else:
                i += 1
        if not encontrado:
            print("No se encontró el curso indicado.")
            
    def inciso4(self, gi):
        gi.ordenador()
        encabezado = False
        for curso in self.__listaCursos:
            if not encabezado:
                print(f"--- {curso.getDenominacion()} - Cupo: {curso.getCupo()}")
                encabezado = True
            cantDiasM = curso.getCantD() * 0.7
            gi.listaInscriptos(curso.getID(),cantDiasM)
            encabezado = False
            

from classBiblio import Biblioteca
from classLibro import Libro
import csv

class GestorBiblio:
    __listaBiblios: list

    def __init__(self):
        self.__listaBiblios = []

    def agregaBiblioteca(self, unaBiblio):
        self.__listaBiblios.append(unaBiblio)

    def leeDatos(self):
        archivo = open('Biblioteca.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        i = -1
        for fila in reader:
            if len(fila) == 3:
                self.agregaBiblioteca(Biblioteca(fila[0], fila[1], fila[2]))
                i += 1
            else:
                self.__listaBiblios[i].agregarLibro(Libro(fila[0], fila[1], fila[2], fila[3]))
        archivo.close()
        print("Se cargaron los datos correctamente.")
    
    def buscaBibPorNombre(self, xnombre):   # hacer bloque try
        i = 0
        encontrado = False
        while i < len(self.__listaBiblios) and not encontrado:
            if xnombre.lower() == self.__listaBiblios[i].getNombre().lower():
                encontrado = True
            else:
                i += 1
        return i
    
    def incisoA(self, xnombre):
        indice = self.buscaBibPorNombre(xnombre)
        xtitulo = input("Ingrese titulo: ")
        xautor = input("Ingrese autor/es: ")
        xisbn = input("Ingrese ISBN: ")
        xgenero = input("Ingrese genero: ")
        self.__listaBiblios[indice].agregarLibro(Libro(xtitulo, xautor, xisbn, xgenero))
        print("Libro agregado exitantemente.")

    def incisoB(self, xnombre):
        indice = self.buscaBibPorNombre(xnombre)
        xtitulo = input("Ingrese titulo: ")
        self.__listaBiblios[indice].deleteaLibro(xtitulo)

    def incisoC(self, xtitulo):
        print("Datos y ubicacion/es:")
        datos = False
        for biblio in self.__listaBiblios:
            libro =  biblio.buscaExistenciaLibro(xtitulo)
            if libro:
                if not datos:
                    print(f"Autor: {libro.getAutor()}\nGenero: {libro.getGenero()}")
                    datos = True
                print(biblio.getNombre())
    
    def incisoD(self):
        for biblio in self.__listaBiblios:
            biblio.listaLibros()

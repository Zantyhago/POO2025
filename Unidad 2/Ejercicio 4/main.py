from gestorCarreras import GestorCarrera
from gestorFacu import GestorFacultad

def menu():
    opcion = input('''
            a) Cargar los datos de las Carreras desde el archivo Carreras.csv. 
            b) Cargar los datos de las Facultades desde del archivo Facultades.csv.
            c) Dado el Nombre de una Carrera, mostrar el nombre de la Facultad en la que se dicta.
            d) Para todas las facultades, mostrar la cantidad de carreras que se dictan en cada una de ellas.
            e) Dado el nombre de una Facultad, generar un listado ordenado alfabéticamente. 
            - su opcion: ''')
    while opcion != 'z':
        if opcion == 'a':
            gFacu.cargaFacultades()
        elif opcion == 'b':
            gCarrera.cargaCarreras()
        elif opcion == 'c':
            xnomb = input("Ingrese nombre de la carrera: ")
            gCarrera.muestraNombre(xnomb, gFacu)
        elif opcion == 'd':
            gFacu.mustraOferta(gCarrera)
        elif opcion == 'e':
            xnomb = input("Ingrese nombre de la facultad: ")
            gFacu.mustraDuracion(gCarrera, xnomb)
        else:
            print("ERROR: opción mal ingresada.")
        opcion = menu()

if __name__ == '__main__':
    gFacu = GestorFacultad()
    gCarrera = GestorCarrera()
    menu()
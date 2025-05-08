from gestorAlquiler import GestorAlquiler
from gestorCancha import GestorCancha

def  menu():
    op = input('''Menu de opciones:
               a) Emitir listado con todos los alquileres registrados.
               b) Ingresar id de una cancha y mostrar la cantidad total de minutos que estuvo alquilada.
               z) Salir.
               su opción --> ''')
    while op != 'z':
        if op == 'a':
            ga.listaAlquileres(gc)
        elif op == 'b':
            id = input("Ingrese id de la cancha: ")
            ga.cantAlquilada(id)
        else:
            print("ERROR. Opción mal ingresada. Intente nuevamente.")
        menu()
    print("Gracias por contar con nostros. Atte., Zantyhago SA (yo)")

if __name__ == '__main__':
    ga = GestorAlquiler()
    gc = GestorCancha()
    ga.leeAlquiler()
    gc.leeCancha()
    menu()
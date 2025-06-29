#Santiago David Sanchez Godoy - E21005 - 43122763
from gestorGasto import GestorGasto
from gestorMovilidad import GestorMovilidad

def menu():
    op = input('''Menú de opciones:
               a) Listar los gastos que ha tenido la movilidad en el mes de abril, indicando el total de gastos.
               b) Indicar los gastos que se produjeron cierto día.
               c) Indicar datos de movilidad dada una fecha.
               z) Salir.
               su opcion -> ''')
    while op != 'z':
        if op == 'a':
            xpatente = input("Ingrese patente: ")
            gm.incisoA(gg, xpatente)
        elif op == 'b':
            xfecha = input("Ingrese fecha: ")
            gg.incisoB(xfecha)
        elif op == 'c':
            xfecha = input("Ingrese fecha: ")
            gg.incisoC(xfecha, gm)
        else:
            print("ERROR. intente nuevamente.")
        menu()
if __name__ == '__main__':
    gm = GestorMovilidad()
    gg = GestorGasto()
    gm.leeMovilidades()
    gg.leeGastos()
    menu()
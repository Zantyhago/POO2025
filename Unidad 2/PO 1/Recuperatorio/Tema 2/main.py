from gestorEquipos import GestorEquipo
from gestorResultados import GestorResultado

def menu():
    op = input('''Menu de opciones:
                a) Mostrar datos en una fecha indicada.
                b) Mostrar resultados de local.
                c) Mostrar tabla de posiciones.
                z) Salir.
                su opcion -> ''')
    while op != 'z':
        if op == 'a':
            xfecha = input("Ingrese fecha: ")
            gr.incisoA(xfecha, ge)
        elif op == 'b':
            xnombre  = input("Ingrese nombre: ")
            ge.incisoB(gr, xnombre)
        elif op == 'c':
            gr.incisoC(ge)
            ge.cereador()
        else:
            print("ERROR. intente nuevamente.")
        menu()
    
if __name__ == '__main__':
    ge = GestorEquipo()
    gr = GestorResultado()
    ge.leeEquipo()
    gr.leeResultado()
    menu()
    print("Gracias por contar conmigo.")
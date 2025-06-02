from gestorBibliotecas import GestorBiblio

def menu():
    op = input('''Menu de opciones:
               a) Agregar un libro.
               b) Eliminar un libro.
               c) Ubicar un libro.
               d) Listar todos los libros.
               z) Salir.
               elejí pibe: ''')
    while op != 'z':
        if op == 'a':
            xnombre = input("Ingrese nombre de la biblioteca: ")
            gb.incisoA(xnombre)
        elif op == 'b':
            xnombre = input("Ingrese nombre de la biblioteca: ")
            gb.incisoB(xnombre)
        elif op == 'c':
            xtitulo = input("Ingrese titulo de la obra: ")
            gb.incisoC(xtitulo)
        elif op == 'd':
            gb.incisoD()
        menu()
    print("Gracias por coso")

if __name__ == '__main__':
    gb = GestorBiblio()
    gb.leeDatos()
    menu()
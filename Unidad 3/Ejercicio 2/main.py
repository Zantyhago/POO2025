from gestorBibliotecas import GestorBiblio

def opciones():
    return '''Menu de opciones:
               a) Agregar un libro.
               b) Eliminar un libro.
               c) Ubicar un libro.
               d) Listar todos los libros.
               z) Salir.
               elejí pibe: '''

def menu():
    try:
        op = input(opciones())
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
            else:
                raise ValueError
            op = input(opciones())
        print("Gracias por usarme :3")
    except ValueError:
        print(f"ERROR. Opción mal ingresada.")
        menu()
    except IndexError:
        print("Instancia no encontrada.")
        menu()

if __name__ == '__main__':
    gb = GestorBiblio()
    gb.leeDatos()
    menu()
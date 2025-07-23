from gestorLista import GestorLista

def menu(op = -1):
    try:
        while op != 0:
            op = int(input('''MENÚ DE OPCIONES:
                       1) Insertar medios en determinada posición.
                       2) Insertar medios.
                       3) Mostrar los medios de la lista.
                       4) Mostrar en que canal y horario se transmite determinado programa.
                       5) Listar toda la programación de una emisora.
                       6) Mostrar cantidad de revistas y diarios.
                       0) Salir.
                       Ingrese su opción -> '''))
            if op == 1:
                xpos = int(input("Ingrese posición: "))
                gl.Inciso1(xpos)
            elif op == 2:
                gl.inciso2()
            elif op == 3:
                for medio in gl:
                    print(medio)
            elif op == 4:
                xprog = input("Ingrese nombre del programa: ").lower()
                gl.inciso4(xprog)
            elif op == 5:
                xemis = input("Ingrese emisora: ").lower()
                gl.inciso5(xemis)
            elif op == 6:
                gl.inciso6()
            else:
                if op != 0:
                    print("Opción mal ingresada. Intente nuevamente.")
        print("chauchis :3")

    except IndexError as a:
        print(a)
        menu()
    except TypeError as b:
        print(b)
        menu()
    except ValueError as c:
        print(c)
        menu()
    except StopIteration as d:
        print(d)

if __name__ == '__main__':
    gl = GestorLista()
    gl.leeMedios()
    menu()
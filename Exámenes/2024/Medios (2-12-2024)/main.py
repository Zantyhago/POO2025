from gestorMedios import GestorMedios
from datetime import date, datetime

def menu(op = 'y'):
    try:
        while op != 'z':
            op = input('''                            MENÚ DE OPCIONES:
                            A) Agregar medio manualmente.
                            B) Mostrar informacion de un programa indicado:
                            C) Mostrar información de todos los medios
                            Z) Salir.
                            Ingrese su opción -> ''').lower()
            if op == 'a':
                gm.incisoA()
            elif op == 'b':
                xnombP = input("Ingrese nombre del programa: ").lower()
                gm.incisoB(xnombP)
            elif op == 'c':
                gm.incisoC()
            else:
                if op != 'z':
                    print("Opción mal ingresada. Intente nuevamente.")
    except IndexError as a:
        print(a)
        menu()
    except ValueError as b:
        print(b)
        menu()
    except TypeError as c:
        print(c)
        menu()
    except Exception as d:
        print(d)
        menu()
    else:
        print("bueno eso es todo")    

if __name__ == '__main__':
    gm = GestorMedios()
    gm.leeMedios()
    menu()
from gestorPacientes import GestorPacientes

def menu(op = -1):
    try:
        while op != 'z':
            op = input('''MENÚ DE OPCIONES:
                            A) Insertar pacientes en la lista.
                            B) Indicar cant. de pac. hospitalizados y ambulatorios.
                            C) Mostrar importe cobrado a todos los pacientes.
                            D) Mostrar el tipo de paciente de una poición indicada.
                            E) Modificar el importe cobrado a todos los pacientes.
                            Z) Salir.
                            Ingrese su opción -> ''').lower()
            if op == 'a':
                gp.leePacientes()
            elif op == 'b':
                gp.incisoB()
            elif op == 'c':
                gp.incisoC()
            elif op == 'd':
                xindice = int(input("Ingrese posición (>0): "))
                gp.incisoD(xindice - 1)
            elif op == 'e':
                xmonto = float(input("Ingrese nuevo monto: "))
                gp.incisoE(xmonto)
            else:
                if op != 'z':
                    print("Opción mal inngresada. Intente nuevamente.")
    except IndexError as a:
        print(a)
        menu()
    except ValueError as b:
        print(b)
        menu()
    except TypeError as c:
        print(c)
        menu()
    else:
        print("nos re vimos")

if __name__ == '__main__':
    gp = GestorPacientes()
    menu()

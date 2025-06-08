from gestorEmpleado import GestorEmpleados
from gestorMatris import GestorMatriculas
from gestorProgramas import GestorProgramas

def opciones():
    return '''- MENÚ DE OPCIONES -
                    1) Informar duracion total de un empleado en los programas.
                    2) Mostrar empleados inscriptos en un programa.
                    3) Mostrar empleados no inscriptos en ningún programa.
                    0) Salir.
                    su opción --> '''

def menu():
    try:
        op = int(input(opciones()))
        if op > 3 or op < 0:
            raise ValueError
        while op != 0:
            if op == 1:
                xid = int(input("Ingrese ID del empleado: "))
                gm.inciso1(xid)
            elif op == 2:
                xnomb = input("Ingrese nombre del programa: ")
                gm.inciso2(xnomb)
            elif op == 3:
                ge.inciso3(gm)
            op = int(input(opciones()))
            if op > 3 or op < 0:
                raise ValueError
        print("Nos vemos 7u7")
    except ValueError:
        print(f"Opción mal ingresada.")
        menu()
    except IndexError:
        print(f"Instancia no encontrada.")
        menu()

if __name__ == '__main__':
    ge = GestorEmpleados()
    ge.leeEmpleados()
    gp = GestorProgramas()
    gp.leeProgramas()
    gm = GestorMatriculas()
    gm.leeMatriculas(ge, gp)
    menu()

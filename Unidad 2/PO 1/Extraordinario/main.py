from gestorCurso import GestorCurso
from gestorInscriptos import GestorInscriptos

def menu(op):
    while op != 0:
        if op == 1:
            xdni = input("Ingrese DNI del incripto: ")
            gi.inciso1(xdni)
        elif op == 2:
            xid = int(input("Ingrese ID del curso: "))
            gc.inciso2(gi, xid)
        elif op == 3:
            xdni = input("Ingrese DNI del inscripto: ")
            gi.inciso3(xdni)
        elif op == 4:
            gc.inciso4(gi)
        else:
            print("Opción mal ingresada. Intente nuevamente.")
        op = int(input('''MENÚ DE OPCIONES:
                1) Buscar inscripto para asistencia.
                2) Mostrar inscriptos con porcentaje mínimo de asistencia.
                3) Fijar nota de un inscripto.
                4) Mostrar todos los inscriptos en los cursos.
                0) Salir.
                Ingrese su opcion -> '''))
    print("Santiago David Sanchez Godoy - E21005. Nos vemos el 28/7 :)")            

if __name__ == '__main__':
    gc = GestorCurso()
    gi = GestorInscriptos()
    gc.leeCursos()
    gi.leeIncriptos()
    op = int(input('''MENÚ DE OPCIONES:
                1) Buscar inscripto para asistencia.
                2) Mostrar inscriptos con porcentaje mínimo de asistencia.
                3) Fijar nota de un inscripto.
                4) Mostrar todos los inscriptos en los cursos.
                0) Salir.
                Ingrese su opcion -> '''))
    menu(op)
from gestorMedicos import GestorMedicos
from gestorVisitas import GestorVisitas

def menu(op):
    while op.lower() != 'z':
        if op.lower() == 'a':
            xdni = input("Ingrese DNI: ")
            gv.incisoA(gm, xdni)
        elif op.lower() =='b':
            gm.incisoB(gv)
        elif op.lower() == 'c':
            xzona = input("Ingrese zona: ")
            gv.incisoC(gm, xzona)
        else:
            print("Opcion mal ingresada. Intente nuevamente.")
        op = input('''MENÚ DE OPCIONES:
            A) Mostrar listado de visitas realizadas por un médico.
            B) Mostrar datos de médicos.
            C) Listar visitas realizadas en una zona especificada.
            su opcion -> ''')
    print("See you c:")

if __name__ == '__main__':
    gv = GestorVisitas()
    gv.leeVisitas()
    cant = int(input("Ingrese cantidad de medicos: "))
    if cant > 3:
        print("Cantidad ingreesada fuera de rango.")
    gm = GestorMedicos(cant)
    gm.leeMedicos()
    op = input('''MENÚ DE OPCIONES:
            A) Mostrar listado de visitas realizadas por un médico.
            B) Mostrar datos de médicos.
            C) Listar visitas realizadas en una zona especificada.
            su opcion -> ''')
    menu(op)
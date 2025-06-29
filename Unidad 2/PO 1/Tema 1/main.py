from gestorTramos import GestorTramos
from gestorColectivos import GestorColectivos

def menu(op):
    while op.lower() != 'z':
        if op.lower() == 'a':
            xdni = input("Ingrese dni: ")
            gc.incisoA(gt, xdni)
        elif op.lower() == 'b':
            gc.incisoB(gt)
        elif op.lower() == 'c':
            cantkm = float(input("Ingrese cantidad de KM: "))
            gt.incisoC(cantkm)
        else:
            print("Opcion mal ingresada.")
        op = input('''MENÚ DE OPCIONES:
               A) Listar datos de un chofer.
               B) Mostrar KM recorridos y gasto por cada colectivo.
               C) Indicada una distancia, mostrar tramos que la superan.
               Z) Salir.
               su opcion -> ''')
    print("ciao")

if __name__ == '__main__':
    gc = GestorColectivos()
    gc.leeColectivos()
    gt = GestorTramos()
    gt.leeTramos()
    op = input('''MENÚ DE OPCIONES:
               A) Listar datos de un chofer.
               B) Mostrar KM recorridos y gasto por cada colectivo.
               C) Indicada una distancia, mostrar tramos que la superan.
               Z) Salir.
               su opcion -> ''')
    menu(op.lower())

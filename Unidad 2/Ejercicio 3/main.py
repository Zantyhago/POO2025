from gestorDepas import GestorDepartamento
from classAccid import Accidente

def cargaAccidentes():
    i = int(input("Ingrese ID del departamento (0 para cancelar): "))
    while i > 0:
        j = int(input("Ingrese numero del mes: "))
        cant = int(input("Ingrese la cantidad de accidentes: "))
        matrizAccids.setCantidad(i, j, cant)
        i = int(input("Ingrese ID del departamento (0 para finalizar): "))

def menu():
    op = input('''Seleccione una opcion:
            a) Dado un mes, mostrar cantidad de accidentes.
            b) Dado un mes, mostrar mostrar departamento con mayor cantidad de accidentes.
            c) Dado un nombre, indicar cantidad de accidentes.
            d) Mostrar todos los datos.
            z) Salir.
            - su opcion: ''')
    while op != 'z':
        if op == 'a':
            mes = int(input("Ingrese numero del mes: "))
            gestorDeps.muestraAccisMes(mes, matrizAccids)
        elif op == 'b':
            mes = int(input("Ingrese numero del mes: "))
            gestorDeps.muestraMayorCant(mes, matrizAccids)
        elif op == 'c':
            xdepa = input("Ingrese nombre del departamento: ")
            matrizAccids.totalAccisDepa(xdepa, gestorDeps)
        elif op == 'd':
            pass
        else:
            print("ERROR: opción mal ingresada.")
        op = input("Nueva opcion: ")

if __name__=='__main__':
    gestorDeps = GestorDepartamento()
    gestorDeps.leeDepartamentos()
    matrizAccids = Accidente()
    matrizAccids.cerea()
    cargaAccidentes()
    menu()
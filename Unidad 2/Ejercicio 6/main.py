from gestorAtenciones import ManejadorAtencioes
from gestorPacientes import ManejadorPacientes

def menu():
    op = input('''Menu de opciones:
               a) Infomrar atenciones en una fecha indicada.
               b) Indicar cantidad de atenciones que tuvo un paciente.
               c) Listar pacientes que no tuvieron ninguna atención.
               d) Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad.
               Su opcion -> ''')
    while op != 'z':
        if op == 'a':
            xfecha = input("Ingrese la fecha (dd/mm/aa): ")
            ga.incisoA(xfecha, gp)
        elif op == 'b':
            xdni = int(input("Ingrese DNI: "))
            ga.incisoB(xdni, gp)
        elif op == 'c':
            gp.incisoC(ga)
        elif op == 'd':
            gp.incisoD()
        else:
            print("ERROR: opción mal ingresada. Intente nuevamente.")
        menu()

if __name__ == '__main__':
    gp = ManejadorPacientes()
    ga = ManejadorAtencioes()
    gp.cargaPacientes()
    ga.cargaAtenciones()
    menu()
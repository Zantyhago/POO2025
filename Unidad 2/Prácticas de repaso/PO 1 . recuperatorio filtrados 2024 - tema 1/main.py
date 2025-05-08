from gestorCabaña import GestorCabaña
from gestorReservas import GestorReserva

def menu():
    op = input('''Menu de opciones:
               a) Ingresar cantidad de huéspedes y mostrar el o los números de las cabañas que tienen una capacidad igual o mayor y está disponible.
               b) Ingresar una fecha y emitir un listado con las reservas cuya fecha de inicio del hospedaje sea igual a la ingresada.
               z) Salir
               Su opcion -> ''')
    while op != 'z':
        if op == 'a':
            cant = int(input("Ingrese cantidad: "))
            gc.muestraNumeros(cant, gr)
        elif op == 'b':
            fecha = str(input("Ingrese fecha (dd/mm/aa): "))
            gr.BuscaFecha(gc, fecha)
        else:
            print("ERORR. Opción mal ingresada, intente nuevamente.")
        menu()

if __name__ == '__main__':
    gc = GestorCabaña()
    gr = GestorReserva()
    gc.leeCabañas()
    gr.leeReserva()
    menu()
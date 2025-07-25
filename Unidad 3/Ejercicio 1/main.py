from gestorHoteles import GestorHoteles

def opciones():
    return '''Menu de opciones:
               1) Agregar una habitación a un hotel.
               2) Reservar una habitación.
               3) Liberar una habitacion.
               4) Mostrar número y piso de las habitaciones de un tipo.
               5) Mostrar la cantidad de habitaciones libres por piso.
               6) Para cada tipo de habitación mostrar el detalle asociado.
               0) Salir
               su opción -> '''

def menu():
    try:
        op = int(input(opciones()))
        if op < 0 or op > 6:
            raise ValueError
        while op != 0:
            if op == 1:
                xnombre = input("Ingrtese nombre del hotel: ")
                gh.Inciso1(xnombre)
            elif op == 2:
                xnom = input("Ingrese nombre del hotel: ")
                xnum = int(input("Ingrese numero de la habitacion: "))
                gh.inciso2(xnom, xnum)
            elif op == 3:
                xnom = input("Ingrese nombre del hotel: ")
                xnum = int(input("Ingrese numero de la habitacion: "))
                gh.Inciso3(xnom, xnum)
            elif op == 4:
                xtipo = input("Ingrese tipo: ")
                gh.inciso4(xtipo)
            elif op == 5:
                gh.inciso5()
            elif op == 6:
                gh.inciso6()
            op = int(input(opciones()))
            if op < 0 or op > 6:
                raise ValueError
        print("Gracias por elejirme ashe")
    except IndexError as e:
        print(f"Instancia ingresada no encontrada. {e}")
        menu()
    except ValueError as e:
        print(f"Error de tipos en el ingreso de datos. {e}")
        menu()

if __name__ == '__main__':
    gh = GestorHoteles()
    gh.leeDatos()
    menu()
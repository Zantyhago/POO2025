from gestorPlanes import GestorPlanes

def menu(op = -1):
    try:
        while op != 0:
            op = int(input('''MENÚ DE OPCIONES
                1) Mostrar que tipo de plan se encuntra en una determinada posición.
                2) Cantidad de planes con una cobertura indicada.
                3) Indicar que compañias poseen mas o igual cantidad de canales internacionales indicados.
                4) Mostrar info de todos los planes.
                0) Salir.
                Ingrese su opción -> '''))
            if op == 1:
                xi = int(input("Ingrese posicion (<0): "))
                gp.inciso1(xi)
            elif op == 2:
                xcob = input("Ingrese cobertura: ")
                gp.inciso2(xcob)
            elif op == 3:
                xcant = int(input("Ingrese cantidad: "))
                gp.inciso3(xcant)
            elif op == 4:
                gp.inciso4()
            else:
                if op == 0:
                    break #se queda en bucle por lo que salta el raise no me voy a complicar por un menú xd
                raise IndexError
        print("como me gusra el python")
    except IndexError as a:
        print(f"Dato ingresado fuera de rango. {a}")
        menu()
    except ValueError as e:
        print(f"Error de tipo en el ingreso de datos. {e}")
        menu()

if __name__ == '__main__':
    gp = GestorPlanes()
    gp.leePlanes()
    menu()
from gestorLista import GestorLista

def menu(op = -1):
    try:
        while op != 0:
            op = int(input('''MENÚ DE OPCIONES:
                    1) Leer vahículos.
                    2) Listar v. eléctricos que pueden recorrer cierta distancia.
                    3) Mostrar datos de todos los vehículos.
                    4) Ingresar nuevo vehículo en una posición indicada.
                    0) Salir.
                    Su opción -> '''))
            if op == 1:
                gl.leeVehiculos()
            elif op == 2:
                xdistancia = float(input("Ingrese distancia: "))
                gl.inciso2(xdistancia)
            elif op == 3:
                gl.inciso3()
            elif op == 4:
                xindice = int(input("Ingrese índice: "))
                gl.inciso4(xindice)
            else:
                if op != 0:
                    print("Error. Opción mal ingresada.")
    except ValueError as a:
        print(a)
        menu()
    except TypeError as b:
        print(b)
        menu()
    except IndexError as c:
        print(c)
        menu()
    else:
        print("Sanchez Godoy Santiago David - E21005 c:")
                
if __name__ == '__main__':
    gl = GestorLista()
    menu()
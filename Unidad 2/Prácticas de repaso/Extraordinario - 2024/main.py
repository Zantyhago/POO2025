from gestorConexiones import GestorConexiones
from gestorGammers import GestorGammers

def menu(op):
    while op.lower() != 'z':
        if op.lower() == 'a':
            xdni = input("Ingrese DNI: ")
            gg.incisoA(gc, xdni)
        elif op.lower() =='b':
            xnom = input("Ingrese el nombre del juego: ")
            gc.incisoB(gg, xnom)
        elif op.lower() == 'c':
            gg.incisoC(gc)
        else:
            print("Opcion mal ingresada. Intente nuevamente.")
        op = input('''MENÚ DE OPCIONES:
            A) Mostrar listado de conexiones de un jugador.
            B) Mostrar que jugadores jugaron un juego.
            C) Jugadores con plan Basico que usaron IP's distintas en simultaneo.
            su opcion -> ''')
    print("See you c:")
    
if __name__ == '__main__':
    gg = GestorGammers()
    gg.leeGammer()
    gc = GestorConexiones()
    gc.leeConexion()
    op = input('''MENÚ DE OPCIONES:
            A) Mostrar listado de conexiones de un jugador.
            B) Mostrar que jugadores jugaron un juego.
            C) Jugadores con plan Basico que usaron IP's distintas en simultaneo.
            su opcion -> ''')
    menu(op)
from gestorBecas import GestorBeca
from gestorBeneficiarios import GestorBeneficiario

def menu():
    op = input('''Seleccione una opción:
        a) Informar beneficiarios de una beca con su importe final.
        b) Informar si un beneficiario posee mas de una beca.
        c) Listar beneficiarios ordenados por sus respecticas facultades.
        d) Listar los estudiantesq ue poseae un promedio mayor que 8 y no poseen beca de ayuda económica.
        Opcion -> ''')
    
    if op == 'a':
        xtipo = input("Ingrese un tipo de beca: ")
        gbec.infMonto(xtipo, gben)
    elif op == 'b':
        xdni = int(input("Ingrese DNI: "))
        gben.mustraCantBecas(xdni)
    elif op == 'c':
        gben.mustraTodosLosBeneficiarios()
    elif op == 'd':
        gben.mustraNoEcon()
    else:
        print("ERROR: opcion mal ingresada. Intente nuevamente.")
        menu()
    menu()

if __name__ == '__main__':
    gbec = GestorBeca()
    gben = GestorBeneficiario()
    gben.cargaBeneficiario()
    gbec.cargaBeca()
    menu()
from classBeneficiario import Beneficiario
import csv as seeseve
class GestorBeneficiario:
    __listaBenes: list

    def __init__(self):
        self.__listaBenes = []

    def agregarBeneficiario(self, unBenef):
        self.__listaBenes.append(unBenef)

    def cargaBeneficiario(self):
        archivo = open("beneficiarios.csv")
        reader = seeseve.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregarBeneficiario(Beneficiario(int(fila[0]), fila[1], fila[2], fila[3], fila[4], int(fila[5]), float(fila[6]), int(fila[7])))
        archivo.close()

    def muestraBenes(self, xid):
        cont = 0
        for bene in self.__listaBenes:
            if bene.getIDasign() == xid:
                cont += 1
                print(f"{bene.getApellido()} {bene.getNombre()} - {bene.getDNI()}")
        return cont
    
    def mustraCantBecas(self, xdni):
        cont = 0
        #espacio = str(' ')
        NoEncontrado = True
        for bene in self.__listaBenes:
            if bene.getDNI() == xdni:
                NoEncontrado = False
                NyA = bene.getNombre()+ str(' ') +bene.getApellido()
                cont += 1
        if NoEncontrado:
            print("ERROR: DNI no registrado.")
        else:
            if cont > 1:
                print(f"{NyA} posee {cont} becas.")
            elif cont == 1:
                print(f"{NyA} posee solo una beca.")
            else:
                print("se re bugueaba no")            
    
    def mustraTodosLosBeneficiarios(self):
        self.__listaBenes.sort()
        print("Lista completa de beneficiados:")
        print("NyA:         DNI:            Carrera:            Año que cursa:          Promedio:           Facultad:")
        for bene in self.__listaBenes:
            print(bene)
    
    def mustraNoEcon(self):
        for bene in self.__listaBenes:
            if bene.getIDasign() != 4:
                if bene.getPromedio() > 8:
                    print(f"NyA: {bene.getNombre()} {bene.getApellido()}. Promedio {bene.getPromedio()}")

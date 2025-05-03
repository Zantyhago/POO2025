from classBeca import Beca
import csv as seeseve
class GestorBeca:
    __listaBecas: list

    def __init__(self):
        self.__listaBecas = []
    
    def agregarBeca(self, unaBeca):
        self.__listaBecas.append(unaBeca)

    def cargaBeca(self):
        archivo = open("becas.csv")
        reader = seeseve.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                self.agregarBeca(Beca(int(fila[0]), fila[1], float(fila[2])))
        archivo.close()

    def infMonto(self, xtipo, gben):
        i = 0
        NotFound = True
        while i < len(self.__listaBecas) and NotFound:
            if xtipo.lower() == self.__listaBecas[i].getTipo().lower():
                NotFound = False
            else:
                i += 1
        if NotFound:
            print("No se encontró el tipo de beca.")
        else:
            print(f"Beneficiados para la beca de tipo {self.__listaBecas[i].getTipo()}")
            cant = gben.muestraBenes(i+1)
            print(f"Importe total de la beca: ${cant*self.__listaBecas[i].getImporte()}")

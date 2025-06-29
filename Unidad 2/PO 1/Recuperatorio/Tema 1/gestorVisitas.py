from classVisita import Visita
import csv

class GestorVisitas:
    __listaVisitas: list

    def __init__(self):
        self.__listaVisitas = []

    def agregaVisitas(self, unaVis):
        self.__listaVisitas.append(unaVis)

    def leeVisitas(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/PO 1/Recuperatorio/Tema 1/Visitas.csv', encoding = 'utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            self.agregaVisitas(Visita(fila[0], fila[1], fila[2], fila[3], fila[4]))
        archivo.close()
        print("se cargaron las visitas.")

    def incisoA(self, gm, xdni):
        cant = 0
        encabezado = False
        for visita in self.__listaVisitas:
            if visita.getDNIm() == xdni:
                if not encabezado:
                    print(f"Visitas de {gm.buscaName(xdni)}:\nFecha:        Zona:           Diagnostico:")
                    encabezado = True
                cant += 1
                print(f"{visita.getFecha()}         {visita.getZona()}      {visita.getDiagnostico()}")
        if not encabezado:
            print("El Doctor ingresado no hizo visitas o no existe.")
        print(f"Cantidad de visitas: {cant}")

    def cantVisitas(self, xdni):
        cant = 0
        for visita in self.__listaVisitas:
            if visita.getDNIm() == xdni:
                cant += 1
        if cant == 0:
            print("El medico indicado no hizo visitas.")
        return cant
    
    def incisoC(self,gm, cabezona):
        hubo = False
        for visita in self.__listaVisitas:
            if visita == cabezona:
                hubo = True
                #fecha, DNI del paciente, nombre del médico, y diagnóstico.
                name = gm.buscaName(visita.getDNIm())
                print(f"{visita} - {name}")
        if not hubo:
            print("Noi hubieron visitas en esa zona o fue mal ingresada.")
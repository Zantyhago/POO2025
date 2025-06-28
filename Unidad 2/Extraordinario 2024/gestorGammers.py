from classGammer import Gamer
import csv
class GestorGammers:
    __listaGammers: list

    def __init__(self):
        self.__listaGammers = []

    def agregaGammer(self, unGammer):
        self.__listaGammers.append(unGammer)

    def leeGammer(self):
        archivo = open('C:/Users/Vaf_Tecnology/Desktop/Santy/Programación Orientada a Objetos/Unidad 2/2024/PO 1/Extraordinario/gammers.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            self.agregaGammer(Gamer(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], float(fila[6]), int(fila[7])))
        archivo.close()
        print("Se cargaron los gordos gammer.")

    def incisoA(self, gc, xdni):
        i = 0
        encontrado = False
        while i < len(self.__listaGammers) and not encontrado:
            if self.__listaGammers[i].getDNI() == xdni:
                encontrado = True
                gammer = self.__listaGammers[i]
            else:
                i += 1
        if encontrado:
            print(f"DNI: {gammer.getDNI()}     NyA: {gammer.getNombre()} {gammer.getApellido()}")
            print(f"Alias: {gammer.getAlias()}     Plan: {gammer.getPlan()}     Importe Base: {gammer.getImporteBase()}")
            if gammer.getPlan() == 'Basico':
                porcentaje = 1.25
            elif gammer.getPlan() == 'Completo':
                porcentaje = 1.30
            elif gammer.getPlan() == 'Extendido':
                porcentaje = 1.40
            gc.muestradatitos(gammer.getID(), gammer.getTiempoLimite(), gammer.getImporteBase(), porcentaje)
        else:
            print("No se encontró el gammer indicado.")
    
    def muestraotrosdatos(self, xip, xid):
        i = 0
        encontrado = False
        while i < len(self.__listaGammers) and not encontrado:
            if self.__listaGammers[i].getID() == xid:
                gammer = self.__listaGammers[i]
                encontrado = True
            else:
                i += 1
        if encontrado:
            print(f"{xip}        {gammer.getNombre()} {gammer.getApellido()}       {gammer.getAlias()}       {gammer.getPlan()}")
        return encontrado

    def incisoC(self, gc):
        encabezado = False
        gc.ordenador()
        for gammer in self.__listaGammers:
            if gammer.getPlan() == 'Basico':
                if not encabezado:
                    print("Jugadores con plan basico que juegan en mas de una IP:")
                    encabezado = True
                if gc.listadoBasicos(gammer.getID()):
                    print(f"- {gammer.getNombre()} {gammer.getApellido()}")
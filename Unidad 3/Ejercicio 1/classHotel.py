from classHabitacion import Habitacion
class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaHabitaciones: list

    def __init__(self, xnom, xdir, xtel):
        self.__nombre = xnom
        self.__direccion = xdir
        self.__telefono = xtel
        self.__listaHabitaciones = []

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def agregaHabitacion(self, xnum, xpiso, xtipo, xprecio, xdispon = True):
        self.__listaHabitaciones.append(Habitacion(xnum, xpiso, xtipo, xprecio, xdispon))
        
    def ordenador(self):
        self.__listaHabitaciones.sort()

    def buscaPorNum(self, xnum):
        i = 0
        encontrado = False
        while i < len(self.__listaHabitaciones) and not encontrado:
            if xnum == self.__listaHabitaciones[i].getNumero():
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError
        return i

    def getttterDisp(self, xindice):
        return self.__listaHabitaciones[xindice].getDisponibilidad()
    
    def setttterDisponib(self, xindice, valor):
        self.__listaHabitaciones[xindice].setDisponibilidad(valor)

    def muestraTipos(self, xtipo, nombreH):
        print(f"Habitaciones con el tipo {xtipo} en el {self.getNombre()}:")
        for habitacion in self.__listaHabitaciones:
            if habitacion.getTipoHab() == xtipo:
                print(f"Número: {habitacion.getNumero()}. Piso: {habitacion.getPiso()}")

    def muestraLibres(self):
        print(f"- {self.getNombre()} -")
        for i in range(1,5):  # i representa el piso
            cant = 0
            for j in range(len(self.__listaHabitaciones)):
                if self.getttterDisp(j) and self.__listaHabitaciones[j].getPiso() == i:
                    cant += 1
            if cant > 1:
                print(f"Hay {cant} habitaciones disponibles en el piso {i}.")                
            elif cant == 1:
                print(f"Hay solo una habitacion disponible en el piso {i}.")
            else:
                print(f"No hay habitaciones disponibles en el piso {i}.")
    
    def listaInfo(self, xtipo):
        #self.__listaHabitaciones.sort()
        for habitacion in self.__listaHabitaciones:
            if xtipo == habitacion.getTipoHab():
                print(habitacion)
class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __numeroTarjeta: int
    __saldoAnterior: float
    def __init__(self, nomb, ape, dni, numtar, saldant):
        self.__nombre = nomb
        self.__apellido = ape
        self.__dni = dni
        self.__numeroTarjeta = numtar
        self.__saldoAnterior = saldant
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getNumeroTarjeta(self):
        return self.__numeroTarjeta
    def getSaldoAnterior(self):
        return self.__saldoAnterior
    def actualizar_saldo(self, nuevo_saldo):
        self.__saldoAnterior = nuevo_saldo

from claseCliente import Cliente
class GestorClientes:
    __listaClientes: list
    def __init__(self):
            self.__listaClientes=[]
    def agregarCliente(self, unCliente):
        if isinstance(unCliente, Cliente):
            self.__listaClientes.append(unCliente)
        else:
            raise TypeError
        
from claseGestorCliente import GestorClientes
from claseCliente import Cliente
def test1():
    gestorCliente=GestorClientes()
    unObjetoCliente = Cliente("Hernan", "Castro", 20333111, 5551, 28000)
try:
    gestorCliente.agregarCliente(unObjetoCliente)
except TypeError:
print("Error de tipos")
def test2():
    gestorCliente=GestorClientes()
try:
    gestorCliente.agregarCliente("agregando un string")
except TypeError:
    print("Error de tipos")
if __name__=="__main__":
    test1()
    test2()
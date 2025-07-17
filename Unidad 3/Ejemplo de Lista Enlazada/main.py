from classLista import Lista
from classProfesor import Profesor

def testLista():
    lista = Lista()
    profesor = Profesor(20201234, 'Moreno', 'Karina')
    lista.agregaProfesor(profesor)
    profesor = Profesor(11234432, 'Díaz', 'Mónica')
    lista.agregaProfesor(profesor)
    profesor = Profesor(31002008, 'Pusineri', 'Lucas')
    lista.agregaProfesor(profesor)
    for dato in lista:
        print(dato)
    lista.eliminarPorDNI(11234432)
    print('Luego de Borrar\n')
    lista.listarDatosProfesores()

if __name__=='__main__':
    testLista()
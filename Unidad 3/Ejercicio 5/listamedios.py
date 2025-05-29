class Nodo:
  __dato: None
  __siguiente: None
#NoSoyAcosadoruwu
def __init__(self, xmedio):
  self.__dato = xmedio
  self.__siguiente = None

def getDato(self):
  return self.__dato

def setSiguiente(self, nodo):
  self.__siguiente = nodo

def getSiguiente(self):
  return self.__siguiente

class Lista:
  __comienzo: None
  __actual: None
  __indice = 0
  __tope = 0

  def __init__(self):
    self.__comienzo = None
    self.__actual = None

  def __iter__(self):
    return self

  def __next__(self):
    if self.__indice == self.__tope:
      self.__actual = self.__comienzo
      self.__indice = 0
    else:
      self.___indice += 1
      dato = self.__actual.getDato()
      self.__actual = self.__actual.getSiguiente()

from classMedio import Medio
from classPrograma import Programa

class Television(Medio):
  __cantidad_canales: int
  __canal: str
  __programas: list

  def __init__(self, xnomb, xaud, xcanal, xcant):
    super().__init__(xnomb, xaud)
    self.__canal = xcanal
    self.__cantidad_canales = xcant
    self.__programas = []

  def getCantCanales(self):
    return self.__cantidad_canales
  
  def agregaProgramaT(self, unProg):
    if isinstance(unProg, Programa):
      self.__programas.append(unProg)
    else:
      raise TypeError
    
  def buscaPorName(self, xnom):
    encotrado = False
    retorno = None
    i = 0
    while i < len(self.__programas) and not encotrado:
      if xnom == self.__programas[i].getNombProg().lower():
        encotrado = True
      else:
        i += 1
    if encotrado: #xd encotrado ni ganas de cambiar todo siendo que en vez de escribir todo esto podría haberlo corregido
      retorno = self.__programas[i]
    return retorno

  def __str__(self):
    return f"{super().__str__()} Cantidad de canales: {self.getCantCanales()}"
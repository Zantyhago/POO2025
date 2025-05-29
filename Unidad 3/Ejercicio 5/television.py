from medio import Medio
class Television(Medio):
  __cantidad_canales: int
  _programas: list

  def __init__(self, xnom, xaud, xcant)
    super().__init__(xnom, xaud)
    self.__cantidad_canales = xcant
    self.__programas = []

  def getCantidad(self)
    return self.__cantidad_canales

  def getProgramas(self):
    return self.__programas

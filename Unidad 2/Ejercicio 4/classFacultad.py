class Facultad:
    __codFacu: int
    __nombreFacu: str
    __direccion: str
    __localidad: str
    __telefono: str

    def __init__(self, xcod, xnomb, xdirrec, xloc, xtel):
        self.__codFacu = xcod
        self.__nombreFacu = xnomb
        self.__direccion = xdirrec
        self.__localidad = xloc
        self.__telefono = xtel

    def getCodFacu(self):
        return self.__codFacu
    
    def getNombreFacu(self):
        return self.__nombreFacu

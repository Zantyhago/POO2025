class Conexion:
    __idjugador: str
    __IPConexion: str
    __nombreJuego: str
    __fecha: str
    __horaInicio: int
    __horaFinalizacion: int

    def __init__(self, xid, xip, xnombre, xfecha, xhInic, xhFin):
        self.__idjugador = xid
        self.__IPConexion = xip
        self.__nombreJuego = xnombre
        self.__fecha = xfecha
        self.__horaInicio = xhInic
        self.__horaFinalizacion = xhFin

    def getIDj(self):
        return self.__idjugador
    def getIP(self):
        return self.__IPConexion
    def getNombreJ(self):
        return self.__nombreJuego
    def getFecha(self):
        return self.__fecha
    def getHoraI(self):
        return self.__horaInicio
    def getHoraF(self):
        return self.__horaFinalizacion
    
    def __eq__(self, otro):
        return (
            self.getIDj() == otro.getIDj() and 
            self.getFecha() == otro.getFecha() and
            self.getHoraI() == otro.getHoraI() and
            self.getIP() != otro.getIP())

    def __lt__(self, otro):
        retorno = None
        if self.getIDj() != otro.getIDj():
            retorno = self.getIDj() < otro.getIDj()
        elif self.getFecha() != otro.getFecha():
            retorno = self.getFecha() < otro.getFecha()
        elif self.getHoraI() != otro.getHoraI():
            retorno = self.getHoraI() < otro.getHoraI()
        else:
            retorno = self.getIP() < otro.getIP()
        return retorno
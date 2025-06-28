class Gamer:
    __idjugador: str
    __dni: str
    __nombre: str
    __apellido: str
    __alias: str
    __plan: str
    __importeBase: float
    __tiempoLimite: int

    def __init__(self, xid, xdni, xnom, xap, xalias, xplan, ximp, xtiemp):
        self.__idjugador = xid
        self.__dni = xdni
        self.__nombre = xnom
        self.__apellido = xap
        self.__alias = xalias
        self.__plan = xplan
        self.__importeBase = ximp
        self.__tiempoLimite = xtiemp

    def getID(self):
        return self.__idjugador
    def getDNI(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getAlias(self):
        return self.__alias
    def getPlan(self):
        return self.__plan
    def getImporteBase(self):
        return self.__importeBase
    def getTiempoLimite(self):
        return self.__tiempoLimite
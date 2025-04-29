class Departamento:
    __ID: int
    __nombre: str

    def __init__(self, xid, xnom):
        self.__ID = xid
        self.__nombre = xnom

    def getID(self):
        return self.__ID
    
    def getNombre(self):
        return self.__nombre
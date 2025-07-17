class CuentaCampus:
    __dominio = "@unsj-cuim.edu.ar"
    __id = 0
    __idUsuario: str
    __nombreUsuario: str
    __clave: str

    def __init__(self, nick, clave, idu = 1):
        self.__nombreUsuario = nick+self.__dominio
        self.__idUsuario = idu
        self.__clave = clave

    def __str__(self):
        return f"Usuario: {self.__nombreUsuario}\nClave: {self.__clave}\n"
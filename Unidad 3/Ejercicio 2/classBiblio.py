class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaLibros: list

    def __init__(self, xnom, xdir, xtel):
        self.__nombre = xnom
        self.__direccion = xdir
        self.__telefono = xtel
        self.__listaLibros = []

    def agregarLibro(self, unLibro):
        self.__listaLibros.append(unLibro)

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono

    def buscaPorTitulo(self, xtitulo):
        i = 0
        encontrado = False
        while i < len(self.__listaLibros) and not encontrado:
            if xtitulo.lower() == self.__listaLibros[i].getTitulo().lower():
                encontrado = True
            else:
                i += 1
        if not encontrado:
            raise IndexError
        return i

    def deleteaLibro(self, xtitulo):
        indice = self.buscaPorTitulo(xtitulo)
        del self.__listaLibros[indice]

    def buscaExistenciaLibro(self, xtitulo):
        indice = self.buscaPorTitulo(xtitulo)
        return self.__listaLibros[indice]

    def listaLibros(self):
        i = 1
        print(f"- {self.getNombre()} -")
        for book in self.__listaLibros:
            print(f"{i}. {book}")
            i += 1
class Libro:
    __titulo: str
    __autor: str
    __isbn: str
    __genero: str

    def __init__(self, xtit, xaut, xisbn, xgen):
        self.__titulo = xtit
        self.__autor = xaut
        self.__isbn = xisbn
        self.__genero = xgen

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor
    
    def getISBN(self):
        return self.__isbn
    
    def getGenero(self):
        return self.__genero
    
    def __del__(self):
        print(f"Libro ''{self.getTitulo()}'' borrado.")

    def __str__(self):
        return self.getTitulo()
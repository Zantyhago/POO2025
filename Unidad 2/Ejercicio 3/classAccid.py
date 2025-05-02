class Accidente:
    __accidentes: list
    __cantFil = int
    __cantCol = int


    def __init__(self):
        self.__accidentes = []
        self.__cantFil = 19
        self.__cantCol = 12

    def cerea(self):
        for i in range(self.__cantFil):
            fila = []
            for j in range(self.__cantCol):
                fila.append(0)
            self.__accidentes.append(fila)

    def setCantidad(self, i, j, cant):
        self.__accidentes[i-1][j-1] = cant
        print(f"Datos para el departamento {i} y mes {j} cargados.")

    def getAccidentes(self, i, j):
        return(self.__accidentes[i-1][j-1])
    
    def buscaIndiceMayor(self, j):
        max = -1
        for i in range(self.__cantFil):
            if self.getAccidentes(i, j-1) > max:
                max = self.getAccidentes(i, j-1)
                indice = i
        return indice
    
    def totalAccisDepa(self, xnomb, gd):
        i = gd.buscaIndice(xnomb)
        for j in range(self.__cantCol):
            total = self.getAccidentes(i,j)
        print(f"Para el departamento {xnomb}, se registró un total de {total} accidentes.")

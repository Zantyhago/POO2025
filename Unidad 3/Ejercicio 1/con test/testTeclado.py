from classHotel import Hotel

class Teclado:
    def test(self, gh):
        op2 = input('''Tipo de clase a ingresar:
                    1: Hotel
                    2: libro
                    0: finalizar
                    -> ''')
        while op2 != '0':
            if op2 == '1':
                xnombre = input("Ingrese nombre: ")
                xdir = input("Ingrese direccion: ")
                xtel = input("Ingrese telefono: ")
                gh.agregaHotel(Hotel(xnombre, xdir, xtel))
            elif op2 == '2':
                xnombreB = input("Ingrese nombre del hotel: ")
                xnum = int(input("Ingrese el numero: "))
                xpiso = int(input("Ingrese piso: "))
                xtipo = input("Ingrese tipo: ")
                xprec = float(input("Ingrese precio por noche: "))
                gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
            op2 = input('''Tipo de clase a ingresar:
                    1: Hotel
                    2: libro
                    0: finalizar
                    -> ''')
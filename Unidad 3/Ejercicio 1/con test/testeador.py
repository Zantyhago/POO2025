from classHotel import Hotel
class Tester:
    def testeador(self, gh):
        h1 = Hotel('Hotel Paraiso Tropical', 'Avenida Costera 1234', '0341698631')
        gh.agregaHotel(h1)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 101
        xpiso = 1
        xtipo = 'sencilla'
        xprec = 5000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 102
        xpiso = 1
        xtipo = 'sencilla'
        xprec = 5000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 201
        xpiso = 2
        xtipo = 'doble'
        xprec = 8000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 202
        xpiso = 2
        xtipo = 'doble'
        xprec = 8000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 301
        xpiso = 3
        xtipo = 'suite'
        xprec = 12000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 303
        xpiso = 3
        xtipo = 'suite'
        xprec = 13000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 304
        xpiso = 3
        xtipo = 'doble'
        xprec = 7500
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 401
        xpiso = 4
        xtipo = 'sencilla'
        xprec = 5100
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Paraiso Tropical'
        xnum = 402
        xpiso = 4
        xtipo = 'suite'
        xprec = 13500
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        h2 = Hotel('Hotel Central', 'Avenidad Ignacio de la Roza 123', '2644200584')
        xnombreB = 'Hotel Central'
        xnum = 101
        xpiso = 1
        xtipo = 'sencilla'
        xprec = 5100
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Central'
        xnum = 202
        xpiso = 2
        xtipo = 'doble'
        xprec = 8000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Central'
        xnum = 301
        xpiso = 3
        xtipo = 'suite'
        xprec = 12000
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
        xnombreB = 'Hotel Central'
        xnum = 402
        xpiso = 4
        xtipo = 'suite'
        xprec = 13500
        gh.agregaHab(xnombreB, xnum, xpiso, xtipo, xprec, True)
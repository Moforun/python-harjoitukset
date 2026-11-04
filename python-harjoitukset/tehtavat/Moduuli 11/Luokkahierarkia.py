class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print("Kirja: " + self.nimi)
        print("Kirjoittaja: " + self.kirjoittaja)
        print("Sivumäärä: " + str(self.sivumäärä))
        return


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print("Lehti: " + self.nimi)
        print("Päätoimittaja: " + self.päätoimittaja)
        return


# Pääohjelma

lehti = Lehti("Helsingin Sanomat", "Kaius Niemi")
kirja = Kirja("Tuntematon sotilas", "Väinö Linna", 480)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()
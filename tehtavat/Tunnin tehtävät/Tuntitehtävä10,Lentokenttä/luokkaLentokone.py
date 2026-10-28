class Lentokone:
    def __init__(self, rekisteritunnus, bensaa):
        self.rekisteritunnus = rekisteritunnus
        self.bensaa = bensaa

class Lentokenttä:
    def lentää(self, lentokone, bensaa):
        lentokone.bensaa = bensaa

lentokenttä = Lentokenttä()
lentokone = Lentokone("Finnair1", "0")
print("Kentällä Helsinki-Vantaa on nyt: ")
lentokenttä.lentää(lentokone, "0")
print("Koneen nimi: " + lentokone.rekisteritunnus)
print("Bensaa tankissa: " + lentokone.bensaa)
print("Bensatankin maksimi 100")

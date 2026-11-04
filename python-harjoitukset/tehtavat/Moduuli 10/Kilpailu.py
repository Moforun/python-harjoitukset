import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit
        return


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot
        self.tunnit = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
        self.tunnit += 1
        return

    def tulosta_tilanne(self):
        print("Kilpailu " + self.nimi + ", tunti " + str(self.tunnit))
        print(f"{'Rekisteritunnus':<16}{'Huippunopeus':>14}{'Nopeus':>10}{'Matka (km)':>14}")
        print("-" * 54)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:>14}{auto.nopeus:>10}{auto.kuljettu_matka:>14}")
        print()
        return

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False



autot = []
for i in range(1, 11):
    autot.append(Auto("ABC-" + str(i), random.randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if kilpailu.tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

print("Kilpailu on päättynyt!")
kilpailu.tulosta_tilanne()
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


autot = []
for i in range(1, 11):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu_kaynnissa = False

print(f"{'Rekisteritunnus':<17}{'Huippunopeus':>14}{'Nopeus':>10}{'Matka':>12}")
print("-" * 53)
for auto in autot:
    print(f"{auto.rekisteritunnus:<17}{auto.huippunopeus:>10} km/h{auto.nopeus:>6} km/h{auto.matka:>8.0f} km")
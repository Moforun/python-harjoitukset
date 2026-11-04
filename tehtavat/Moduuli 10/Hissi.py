class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print("Hissi on nyt kerroksessa " + str(self.kerros))
        return

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print("Hissi on nyt kerroksessa " + str(self.kerros))
        return

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print("Kerrosta " + str(kohdekerros) + " ei ole")
            return
        while self.kerros < kohdekerros:
            self.kerros_ylös()
        while self.kerros > kohdekerros:
            self.kerros_alas()
        return


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print("Hissiä " + str(hissin_numero) + " ei ole")
            return
        print("Ajetaan hissiä " + str(hissin_numero) + " kerrokseen " + str(kohdekerros))
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)
        return

    def palohälytys(self):
        print("PALOHÄLYTYS! Kaikki hissit pohjakerrokseen")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)
        return


# Pääohjelma

# Tehtävä 1: yksittäinen hissi
h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

# Tehtävä 2: talo ja hissit
talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 4)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 2)

# Tehtävä 3: palohälytys
talo.palohälytys()
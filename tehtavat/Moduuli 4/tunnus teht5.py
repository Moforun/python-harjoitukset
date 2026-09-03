oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break

    yritykset += 1

    if yritykset == 5:
        print("Pääsy evätty")
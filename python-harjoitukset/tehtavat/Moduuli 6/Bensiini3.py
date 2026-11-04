def muunna_litroiksi(gallonat):
    return gallonat * 3.785


gallonat = float(input("Anna gallonamäärä: "))

while gallonat >= 0:
    litrat = muunna_litroiksi(gallonat)
    print(f"{litrat:.2f} litraa")
    gallonat = float(input("Anna gallonamäärä: "))
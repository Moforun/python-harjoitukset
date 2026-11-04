def laske_summa(luvut):
    summa = 0

    for luku in luvut:
        summa += luku

    return summa


luvut = [2, 4, 6, 8, 10]

summa = laske_summa(luvut)

print(f"Lukujen summa on {summa}.")
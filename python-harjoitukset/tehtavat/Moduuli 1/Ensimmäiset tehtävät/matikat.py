gramma = int(input("kuinka monta grammaa: "))
g = gramma % 1000
kg = gramma // 1000
print(f"Määrä kiloina ja grammoina: {kg:.0f} kg {g} g")
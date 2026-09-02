leiviskät = int(input("Anna leiviskät.\n")) 
naulat = int(input("\nAnna naulat.\n")) 
luodit = float(input("\nAnna luodit.\n")) 
luoteja = leiviskät * 20 * 32 + naulat * 32 + luodit
gramma = luoteja * 13.3
kilogramma = int(gramma // 1000)
gramma = gramma % 1000

print(f"\nMassa nykymittojen mukaan:\n{kilogramma} kilogrammaa ja {gramma} grammaa.")
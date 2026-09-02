hyttiluokka = input("Mikä on teidän hyttiluokka? (LUX, A, B, C): ").upper()

if hyttiluokka == "LUX":
    print("Parvekkeellinen hytti autokannen yläpuolella.")

elif hyttiluokka =="A":
    print("Ikkunallinen hytti autokannen yläpuolella.")

elif hyttiluokka == "B":
    print("Ikkunaton hytti autokannen yläpuolella.")

elif hyttiluokka == "C":
    print("Ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")
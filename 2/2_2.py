perenimi = input("Sisestage Leedu perenimi: ")
if perenimi[-2:] == "ne":
    print("abielus")
elif perenimi[-2:] == "te":
    print("määramata")
elif perenimi[-1] == "e":
    print("ilmselt ei ole leedulanna perekonnanimi")

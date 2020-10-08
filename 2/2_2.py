perenimi = input("Sisestage Leedu perenimi: ")
if perenimi[-2:] == "ne":
    print("abielus")
elif perenimi[-2:] == "te":
    print("vallaline")
elif perenimi[-1] == "e":
    print("määramata")
elif perenimi[-1] != "e":
    print("Ei ole leedulanna")

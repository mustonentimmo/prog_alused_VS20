vanus = int(input("Sisesta oma vanus: "))
sugu = input("Sisestage oma sugu (M/N): ").upper()
treeningutüüp = int(input("treeningu tüüp (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening)"))
koormus_mees = 220 - vanus
koormus_naine = 206 - (vanus * 88 / 100)

def koormus():
    if sugu[0] == "M":
        print("Teie maksimaalne koormus on: " + str(koormus_mees))
        if treeningutüüp == 1:
            treening1 = koormus_mees * 0.5
            treening2 = koormus_mees * 0.6
            print("tervisetreeningu puhul peaks teie pulss olema " + str(treening1) + " ja " + str(treening2))
        if treeningutüüp == 2:
            treening1 = koormus_mees * 0.7
            treening2 = koormus_mees * 0.8
            print("põhivastupidavuse treeningu puhul peaks teie pulss olema " + str(treening1) + " ja " + str(treening2))
        if treeningutüüp == 3:
            treening1 = koormus_mees * 0.8
            treening2 = koormus_mees * 0.9
            print("intensiivne aeroobse treeningu puhul peaks teie pulss olema " + str(treening1) + " ja " + str(treening2))
    else:
        print("Teie maksimaalne koormus on: " + str(koormus_naine))
        if treeningutüüp == 1:
            treening1 = koormus_naine * 0.5
            treening2 = koormus_naine * 0.6
            print("tervisetreeningu puhul peaks teie pulss olema " + str(treening1) + " ja " + str(treening2))
        if treeningutüüp == 2:
            treening1 = koormus_naine * 0.7
            treening2 = koormus_naine * 0.8
            print("põhivastupidavuse treeningu puhul peaks teie pulss olema " + str(treening1) + " ja " + str(treening2))
        if treeningutüüp == 3:
            treening1 = koormus_naine * 0.8
            treening2 = koormus_naine * 0.9
            print("intensiivne aeroobse treeningu puhul peaks teie pulss olema " + str(treening1) + " ja " + str(treening2))



koormus()
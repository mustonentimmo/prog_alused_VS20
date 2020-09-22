nimi = input("Sisesta oma nimi: ")
lubatudKiirus = int(input("Sisestage lubatud kiirus: "))
tegelikKiirus = int(input("Sisestage oma kiirus: "))
lause_keskosa = ", kiiruse ületamise eest on teie trahv "

if tegelikKiirus > lubatudKiirus:
    ületatudKiirus = int(tegelikKiirus - lubatudKiirus)
    trahv = int(ületatudKiirus * 3)
    print(nimi + lause_keskosa + str(trahv))



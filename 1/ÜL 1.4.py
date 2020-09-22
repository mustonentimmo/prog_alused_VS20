nimi = input("Sisesta oma nimi: ")
lubatudKiirus = int(input("Sisestage lubatud kiirus: "))
tegelikKiirus = int(input("Sisestage oma kiirus: "))
lause_keskosa = ", kiiruse ületamise eest teie trahv on "

if tegelikKiirus > lubatudKiirus:
    ületatudKiirus = int(tegelikKiirus - lubatudKiirus)
    trahv = min(190, ületatudKiirus * 3)
    print(nimi + lause_keskosa + str(trahv))
else:
    print(nimi + " te ei ole kiirust ületanud")


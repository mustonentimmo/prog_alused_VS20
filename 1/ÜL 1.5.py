ainepunktid = int(input("Sisestage ainepunktide arv: "))
nädalateArv = int(input("Sisestage nädalate arv: "))
ajakulu = ainepunktid * 26
nädalaJaotis = round(ajakulu / nädalateArv)
print(nädalaJaotis)
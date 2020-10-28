# Sisend, mis küsib kasutajalt kõneminuti hinda ning kõnede koguarvu
minhind = float(input('Sisesta kõneminuti hind '))
kõnedkokku = int(input('Sisesta kõnede koguarv'))
# Kõnekestvuse nimekiri
konekestvused = []

import random

#Funktsioon, mis genereerib suvalised arvud vahemikus 1 - 1000 ning lükkab need nimekirja konekestvused
def random_kõnekestvus(kõnedkokku):
        for i in range(kõnedkokku):
            juhuarv = random.randint(1, 1000)
            konekestvused.append(juhuarv)


#random_kõnekestvuse funktsiooni käivitamine võttes argumendiks - kõnedkokku
random_kõnekestvus(kõnedkokku)


#võtab väärtused nimekirjast "konekestvused" ning kontrollib kõne kestvuse pikkust ning seejärel arvutab hinna
def kone_maksumus(konekestvused, minhind):
    koguhind = 0

    for i in konekestvused:
        if i < 60:
            print("Kõnehind on " + str(minhind))
            koguhind = koguhind + minhind
        if i > 600:
            hind = minhind * 10
            print("Kõnehind on " + str(hind))
            koguhind = koguhind + hind
        else:
            sekundihind = minhind / 60
            print("kõnehind on " + str(sekundihind))
            koguhind = koguhind + sekundihind

    #Väljastab kogu summa
    print("kogu arve " + str(round(koguhind, 2)) + " EUR")

#kone_maksumus funktsiooni käivitamine võttes argumendiks - konekestvused, minhind
kone_maksumus(konekestvused, minhind)



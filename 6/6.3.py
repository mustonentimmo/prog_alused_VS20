kuupäev = input("sisesta kuupäev formaadis DD.MM.YYYY ")

kuud = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"]

päev = kuupäev.split('.')[0]
kuu = kuupäev.split('.')[1]
aasta = kuupäev.split('.')[2]

def changeFormat(kuu):
    format = int(kuu) - 1
    print(päev + "." + " " + kuud[format] + " " + aasta + "." + " a")

changeFormat(kuu)
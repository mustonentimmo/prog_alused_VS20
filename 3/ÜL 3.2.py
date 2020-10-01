ringideArv = int(input("Sisesta ringide arv:"))
ringiNumber = 1
porgandiArv = 0

while(ringiNumber <= ringideArv):
    print("Ringi number " + str(ringiNumber))
    if((ringideArv % 2) == 0):
        porgandiArv = ringideArv + ringiNumber
        print("Said " + str(porgandiArv) + " porgandit")

    ringiNumber += 1


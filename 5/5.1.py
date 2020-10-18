aasta = int(input("Sisesta aasta "))

fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()


if aasta == 2011:
     print("sel aastal võeti vsatu " + str(vastuvõetud[0]))
if aasta == 2012:
     print("sel aastal võeti vsatu " + str(vastuvõetud[1]))
if aasta == 2013:
     print("sel aastal võeti vsatu " + str(vastuvõetud[2]))
if aasta == 2014:
     print("sel aastal võeti vsatu " + str(vastuvõetud[3]))
if aasta == 2015:
     print("sel aastal võeti vsatu " + str(vastuvõetud[4]))
if aasta == 2016:
     print("sel aastal võeti vsatu " + str(vastuvõetud[5]))
if aasta == 2017:
     print("sel aastal võeti vsatu " + str(vastuvõetud[6]))
if aasta == 2018:
     print("sel aastal võeti vsatu " + str(vastuvõetud[7]))
if aasta == 2019:
     print("sel aastal võeti vsatu " + str(vastuvõetud[8]))
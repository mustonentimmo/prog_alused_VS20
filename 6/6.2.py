külaliste_arv = int(input("Mitu inimest on kutsutud? "))
tulemas_arv = int(input("Mitu inimest on tulemas? "))

def eelarve(külaliste_arv, tulemas_arv):
    max_eelarve = külaliste_arv * 10 + 55
    print("Maksimaalne eelarve: " + str(max_eelarve) + " eurot")
    min_eelarve = tulemas_arv * 10 + 55
    print("Minimaalne eelarve: " + str(min_eelarve) + " eurot")


eelarve(külaliste_arv, tulemas_arv)
täringuteArv = int(input("Sisestage täringute arv: "))
x = 1

import random

while(x <= täringuteArv):
    print(random.randint(1, 6))
    x += 1


õunad = 14
pöialpoisid = int(input("Mitmele pöialpoisile õunu jagada? "))
x = 1

import random

while(x <= pöialpoisid):
    print(random.randint(1, 2))
    z = z + random.randint(1, 2)
    x += 1

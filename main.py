import random
import os

nomes = ["Joelson", "Rui", "Roberto", "Raffaele", "Rafael", "Paulo", "Josias", "Kenny", "Ronaldo", "Carlos"]
random.shuffle(nomes)
equipa1 = []
equipa2 = []

for elm in nomes:
    sort = False
    while True:
        rand = random.randint(0, 100)
        if rand>50 and len(equipa1)<len(nomes)/2:
            equipa1.append(elm)
            sort = True
        elif rand<50 and len(equipa2)<len(nomes)/2:
            equipa2.append(elm)
            sort = True

        if sort:
            break
    print("ok")

os.system("cls")
print("Equipa 1:")
[print(elm) for elm in equipa1]
print("\n")
print("Equipa 2:")
[print(elm) for elm in equipa2]
print("\n")

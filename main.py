'''
1. Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
'''
import random
lista = []
paroslista = []
for i in range(5):
    veletlen = random.randint(1, 10)
    lista.append(veletlen)
    print(veletlen)
for i in lista:
    if i % 2 == 0:
        paroslista.append(i)
print(f"A mennyi szám van a listában:{len(paroslista)} és a páros számok: {paroslista}")



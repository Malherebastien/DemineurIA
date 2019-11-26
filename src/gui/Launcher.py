from random import randint
from gui.Plateau import Plateau

import numpy as np

HAUTEUR = 8
LARGEUR = 8

def remplir_tableau():
    for i in range(0, HAUTEUR - 1):
        for j in range(0, LARGEUR - 1):
            if bombes[i, j] >= 20:
                if i > 0:
                    bombes[i-1, j] += 1
                    if j > 0:
                        bombes[i-1, j-1] += 1
                    if j < LARGEUR - 1:
                        bombes[i-1, j+1] += 1
                if i < HAUTEUR - 1:
                    bombes[i + 1, j] += 1
                    if j > 0:
                        bombes[i+1, j-1] += 1
                    if j < LARGEUR - 1:
                        bombes[i+1, j+1] += 1
                if j > 0:
                    bombes[i, j-1] += 1
                if j < LARGEUR -1:
                    bombes[i, j+1] += 1

bombes = np.zeros([HAUTEUR, LARGEUR], dtype=int)

for i in range(0, 10):
    x = randint(0, HAUTEUR - 1)
    y = randint(0, LARGEUR - 1)
    if bombes[x, y] == 0:
        bombes[x, y] = 20
        print(x, y)

remplir_tableau()
print(bombes)

plateau = Plateau(bombes, HAUTEUR, LARGEUR)

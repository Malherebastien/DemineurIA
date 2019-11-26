from tkinter import *
from gui.Case import Case

WIDTH = 800
HEIGHT = 600


class Plateau:
    def vide(event):
        event

    def bombe(event):
        print("boum")

    def __init__(self, tableau_bombes, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

        print("Truc")

        fenetre = Tk()
        canvas = Canvas(fenetre, width=WIDTH, height=HEIGHT)

        for i in range(0, self.hauteur):
            for j in range(0, self.largeur):
                voisins = []
                if i > 0:
                    voisins.append(tableau_bombes[i - 1, j])
                    if j > 0:
                        voisins.append(tableau_bombes[i - 1, j - 1])
                    if j < largeur - 1:
                        voisins.append(tableau_bombes[i - 1, j + 1])
                if i < hauteur - 1:
                    voisins.append(tableau_bombes[i + 1, j])
                    if j > 0:
                        voisins.append(tableau_bombes[i + 1, j - 1])
                    if j < largeur - 1:
                        voisins.append(tableau_bombes[i + 1, j + 1])
                if j > 0:
                    voisins.append(tableau_bombes[i, j - 1])
                if j < largeur - 1:
                    voisins.append(tableau_bombes[i, j + 1])

                if tableau_bombes[j, i] >= 20:
                    Case(canvas, (WIDTH / self.hauteur) * i, (HEIGHT / self.largeur) * j,
                         (WIDTH / self.hauteur) * (i + 1),
                         HEIGHT / self.largeur * (j + 1), tableau_bombes[j, i], voisins)
                else:
                    Case(canvas, (WIDTH / self.hauteur) * i, (HEIGHT / self.largeur) * j,
                         (WIDTH / self.hauteur) * (i + 1),
                         HEIGHT / self.largeur * (j + 1), tableau_bombes[j, i], voisins)

        canvas.pack()
        fenetre.mainloop()

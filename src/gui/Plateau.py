from tkinter import *

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
                if tableau_bombes[j, i] >= 20:
                    rectangle = canvas.create_rectangle((WIDTH / self.hauteur) * i, (HEIGHT / self.largeur) * j,
                                                        (WIDTH / self.hauteur) * (i + 1), HEIGHT / self.largeur * (j + 1),
                                                        fill="SlateGray2", activefill="blue")
                    canvas.tag_bind(rectangle, "<Button-1>", Plateau.bombe)
                else:
                    rectangle = canvas.create_rectangle((WIDTH / self.hauteur) * i, (HEIGHT / self.largeur) * j,
                                                        (WIDTH / self.hauteur) * (i + 1),
                                                        HEIGHT / self.largeur * (j + 1),
                                                        fill="SlateGray2", activefill="blue")
                    canvas.tag_bind(rectangle, "<Button-1>", Plateau.vide)

        canvas.pack()
        fenetre.mainloop()



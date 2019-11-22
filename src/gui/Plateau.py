from tkinter import *

WIDTH = 800
HEIGHT = 600


def _init_(self, tableauBombes, largeur, hauteur):
    self.largeur = largeur
    self.hauteur = hauteur

    fenetre = Tk()
    canvas = Canvas(fenetre, width=WIDTH, height=HEIGHT)

    for i in range(0, self.hauteur):
        for j in range(0, self.largeur):
            rectangle = canvas.create_rectangle((WIDTH / self.hauteur) * i, (HEIGHT / self.largeur) * j,
                                                (WIDTH / self.hauteur) * (i + 1), HEIGHT / self.largeur * (j + 1),
                                                fill="grey", activefill="blue")
            canvas.tag_bind(rectangle, "<Button-1>", key)

    canvas.pack()
    fenetre.mainloop()


def key(event):
    print("coucou")

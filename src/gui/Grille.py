from tkinter import Canvas


class Grille:
    def __init__(self, fenetre, width, height, bombes):
        self.id = Canvas(fenetre, width=width, height=height)
        self.bombes = bombes

    def revealAround(self, x, y):
        print("lel")


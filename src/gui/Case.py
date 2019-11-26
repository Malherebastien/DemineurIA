from tkinter.font import Font


class Case:
    def __init__(self, canvas, x1, y1, x2, y2, value, voisins):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="DeepSkyBlue2")
        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.on_click)
        self.value = value
        self.voisins = voisins
        self.clicked = False

    def on_click(self, event):
        self.click()

    def click(self):
        if not self.clicked:
            self.clicked = not self.clicked
            color = "CadetBlue1"
            self.canvas.itemconfigure(self.id, fill=color)
            if self.value != 0:
                self.canvas.create_text((self.x2 - self.x1) / 2 + self.x1, (self.y2 - self.y1) / 2 + self.y1,
                                        text=self.value, font=Font(size="20", weight="bold"))
            else:
                self.reveal_around()

    def reveal_around(self):
        for x in self.voisins:
            x.click()

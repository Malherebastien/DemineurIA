from tkinter.font import Font


class Case:
    def __init__(self, canvas, x1, y1, x2, y2, value):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="DeepSkyBlue2")
        self.value = value
        self.voisins = []
        self.clicked = False
        self.state = " "
        self.text_state = self.canvas.create_text((self.x2 - self.x1) / 2 + self.x1, (self.y2 - self.y1) / 2 + self.y1,
                                                  text=self.state, font=Font(size="35", weight="bold"))

        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.on_click)
        self.canvas.tag_bind(self.text_state, "<ButtonPress-1>", self.on_click)
        self.canvas.tag_bind(self.id, "<ButtonPress-3>", self.on_right_click)
        self.canvas.tag_bind(self.text_state, "<ButtonPress-3>", self.on_right_click)

    def on_right_click(self, event):
        if not self.clicked:
            if self.state == " ":
                self.state = "!"
            elif self.state == "!":
                self.state = "?"
            else:
                self.state = " "
            self.canvas.itemconfig(self.text_state, text=self.state)

    def on_click(self, event):
        self.click(True)

    def click(self, recurs):
        color = "CadetBlue1"
        if not self.clicked and self.state == " ":
            self.clicked = not self.clicked

            if self.value >= 20:
                color = "red"
            elif self.value != 0:
                self.canvas.create_text((self.x2 - self.x1) / 2 + self.x1, (self.y2 - self.y1) / 2 + self.y1,
                                        text=self.value, font=Font(size="20", weight="bold"))
            else:
                self.reveal_around(True)
            self.canvas.itemconfigure(self.id, fill=color)
        elif recurs:
            i = 0
            for x in self.voisins:
                if x.state == "!":
                    i += 1
            if i == self.value:
                self.reveal_around_clicked()

    def reveal_around(self, recurs):
        for x in self.voisins:
            if x.value < 20:
                x.click(recurs)

    def reveal_around_clicked(self):
        for x in self.voisins:
            x.click(False)
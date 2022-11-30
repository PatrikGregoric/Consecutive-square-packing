from sage.plot.polygon import polygon


class Kvadrat:

    def __init__(self, x, y, dolzina_stranice):
        self.x = x
        self.y = y
        self.dolzina_stranice = dolzina_stranice

    def narisi(self, barva="red"):
        return polygon(
            [(self.x, self.y), (self.x + self.dolzina_stranice, self.y),
             (self.x + self.dolzina_stranice, self.y + self.dolzina_stranice),
             (self.x, self.y + self.dolzina_stranice)],
            color=barva,
            edgecolor='black',
            alpha=0.5,
            zorder=1)
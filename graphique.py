import pygame as pg
from game import Chess
from variables import *
import sys

class Graphique:

    def __init__(self):
        pg.init()

        self.click = False

        Tplateau = X * SIZE, Y * SIZE

        self.window = pg.display.set_mode(Tplateau)
        pg.display.set_caption('Chess')
        self.clock = pg.time.Clock()

        self.game = Chess(self.window)

        self.mainloop()

    def draw(self):
        self.window.fill("black")
        self.game.draw(self.window)

    def recupe_case(self):
        for y in range(Y):
            if y * SIZE < pg.mouse.get_pos()[1] <= y * SIZE + SIZE:
                for x in range(X):
                    if x * SIZE < pg.mouse.get_pos()[0] <= x * SIZE + SIZE:
                        return x, y

    def mainloop(self):

        run = True
        while run:

            for event in pg.event.get():
                # fermer la fenetre si on clique sur la croix
                if event.type == pg.QUIT:
                    run = False

                if event.type == pg.MOUSEBUTTONDOWN and not self.click:
                    if event.button == 1:
                        self.click = True

                        coord = self.recupe_case()
                        if self.game.getCoordTmp() == self.game.getCase(coord):
                            self.game.setPtmp("vide")
                        elif self.game.verif_deplacement(coord):
                            self.game.deplacement(coord)
                            self.game.changer_joueur()
                        elif self.game.getCase(coord) != "vide":
                            self.game.setPtmpCoord(coord)
                            self.game.setCoordTmp(coord)

                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False

                keys = pg.key.get_pressed()

                if keys[pg.K_r]:
                    self.game.reinit()



            self.draw()
            pg.display.update()
            self.clock.tick(60)
        sys.exit()
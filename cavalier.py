import pygame as pg
from variables import *

class Cavalier:

    def __init__(self, surface):
        self.img = {}
        self.img["black"] = pg.transform.scale(pg.image.load("./Images/b_knight_png_128px.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))
        self.img["white"] = pg.transform.scale(pg.image.load("./Images/w_knight_png_128px.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))

    def draw(self, surface, x, y, size, color):
        surface.blit(self.img[color], (x*size + SIZE//10, y*size + SIZE//10))

    def case_possible(self, x, y, tab):
        l = []
        for coord in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            if 0 <= x+coord[0] < X and 0 <= y+coord[1] < Y:
                if tab[x][y] == "b_cavalier":
                    if tab[x+coord[0]][y+coord[1]] not in BLACKPIECES:
                        l.append((x+coord[0], y+coord[1]))
                elif tab[x][y] == "w_cavalier":
                    if tab[x+coord[0]][y+coord[1]] not in WHITEPIECES:
                        l.append((x+coord[0], y+coord[1]))
        return l[:]
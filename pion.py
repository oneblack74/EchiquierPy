import pygame as pg
from variables import *

class Pion:

    def __init__(self, surface):
        self.img = {}
        self.img["black"] = pg.transform.scale(pg.image.load("./Images/b_pawn.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))
        self.img["white"] = pg.transform.scale(pg.image.load("./Images/w_pawn.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))

    def draw(self, surface, x, y, size, color):
        surface.blit(self.img[color], (x*size + SIZE//10, y*size + SIZE//10))

    def case_possible(self, x, y, tab, tmpY):
        l = []
        if tab[x][y] == "b_pion":
            max = 2
            if tmpY == 1:
                max = 3
            for i in range(1, max):
                if 0 <= x < X and 0 <= y+i < Y and tab[x][y+i] == "vide":
                    l.append((x, y+i))
                else:
                    break
            if 0 <= x+1 < X and 0 <= y+1 < Y and tab[x+1][y+1] in WHITEPIECES:
                l.append((x+1, y+1))
            if 0 <= x-1 < X and 0 <= y+1 < Y and tab[x-1][y+1] in WHITEPIECES:
                l.append((x-1, y+1))
        else:
            max = 2
            if tmpY == 6:
                max = 3
            for i in range(1, max):
                if 0 <= x < X and 0 <= y-i < Y and tab[x][y-i] == "vide":
                    l.append((x, y-i))
                else:
                    break
            if 0 <= x+1 < X and 0 <= y-1 < Y and tab[x+1][y-1] in BLACKPIECES:
                l.append((x+1, y-1))
            if 0 <= x-1 < X and 0 <= y-1 < Y and tab[x-1][y-1] in BLACKPIECES:
                l.append((x-1, y-1))

        return l[:]

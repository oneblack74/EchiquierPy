import pygame as pg
from variables import *

class Roi:

    def __init__(self, surface):
        self.img = {}
        self.img["black"] = pg.transform.scale(pg.image.load("./Images/b_king_png_128px.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))
        self.img["white"] = pg.transform.scale(pg.image.load("./Images/w_king_png_128px.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))

    def draw(self, surface, x, y, size, color):
        surface.blit(self.img[color], (x*size + SIZE//10, y*size + SIZE//10))

    def case_possible(self, x, y, tab, joueur, check_rock):
        l = []
        for coord in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            if 0 <= x + coord[0] < X and 0 <= y + coord[1] < Y:
                if tab[x][y] == "b_roi":
                    if tab[x + coord[0]][y + coord[1]] not in BLACKPIECES:
                        l.append((x + coord[0], y + coord[1]))
                elif tab[x][y] == "w_roi":
                    if tab[x + coord[0]][y + coord[1]] not in WHITEPIECES:
                        l.append((x + coord[0], y + coord[1]))

        if joueur == 0:
            if not check_rock[0] and not check_rock[1]:
                if tab[6][7] == "vide" and tab[5][7] == "vide":
                    l.append((6, 7))
            if not check_rock[0] and not check_rock[2]:
                if tab[1][7] == "vide" and tab[2][7] == "vide" and tab[3][7] == "vide":
                    l.append((2, 7))

        else:
            if not check_rock[0] and not check_rock[1]:
                if tab[6][0] == "vide" and tab[5][0] == "vide":
                    l.append((6, 0))
            if not check_rock[0] and not check_rock[2]:
                if tab[1][0] == "vide" and tab[2][0] == "vide" and tab[3][0] == "vide":
                    l.append((2, 0))

        return l[:]
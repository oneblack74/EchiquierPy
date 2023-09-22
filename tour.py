import pygame as pg
from variables import *

class Tour:

    def __init__(self, surface):
        self.img = {}
        self.img["black"] = pg.transform.scale(pg.image.load("./Images/b_rook_png_128px.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))
        self.img["white"] = pg.transform.scale(pg.image.load("./Images/w_rook_png_128px.png").convert_alpha(surface), (SIZE - SIZE//5, SIZE - SIZE//5))

    def draw(self, surface, x, y, size, color):
        surface.blit(self.img[color], (x*size + SIZE//10, y*size + SIZE//10))

    def case_possible(self, x, y, tab):
        l = []
        for i in range(1, X):
            if 0 <= x + i < X and 0 <= y < Y:
                if tab[x][y] == "b_tour":
                    if tab[x + i][y] == "vide":
                        l.append((x + i, y))
                    elif tab[x + i][y] in BLACKPIECES:
                        break
                    elif tab[x + i][y] != "vide":
                        l.append((x + i, y))
                        break


                elif tab[x][y] == "w_tour":
                    if tab[x + i][y] == "vide":
                        l.append((x + i, y))
                    elif tab[x + i][y] in WHITEPIECES:
                        break
                    elif tab[x + i][y] != "vide":
                        l.append((x + i, y))
                        break

            else:
                break

        for i in range(1, X):
            if 0 <= x - i < X and 0 <= y < Y:
                if tab[x][y] == "b_tour":
                    if tab[x - i][y] == "vide":
                        l.append((x - i, y))
                    elif tab[x - i][y] in BLACKPIECES:
                        break
                    elif tab[x - i][y] != "vide":
                        l.append((x - i, y))
                        break


                elif tab[x][y] == "w_tour":
                    if tab[x - i][y] == "vide":
                        l.append((x - i, y))
                    elif tab[x - i][y] in WHITEPIECES:
                        break
                    elif tab[x - i][y] != "vide":
                        l.append((x - i, y))
                        break

            else:
                break

        for i in range(1, X):
            if 0 <= x < X and 0 <= y + i < Y:
                if tab[x][y] == "b_tour":
                    if tab[x][y + i] == "vide":
                        l.append((x, y + i))
                    elif tab[x][y + i] in BLACKPIECES:
                        break
                    elif tab[x][y + i] != "vide":
                        l.append((x, y + i))
                        break


                elif tab[x][y] == "w_tour":
                    if tab[x][y + i] == "vide":
                        l.append((x, y + i))
                    elif tab[x][y + i] in WHITEPIECES:
                        break
                    elif tab[x][y + i] != "vide":
                        l.append((x, y + i))
                        break

            else:
                break

        for i in range(1, X):
            if 0 <= x < X and 0 <= y - i < Y:
                if tab[x][y] == "b_tour":
                    if tab[x][y - i] == "vide":
                        l.append((x, y - i))
                    elif tab[x][y - i] in BLACKPIECES:
                        break
                    elif tab[x][y - i] != "vide":
                        l.append((x, y - i))
                        break


                elif tab[x][y] == "w_tour":
                    if tab[x][y - i] == "vide":
                        l.append((x, y - i))
                    elif tab[x][y - i] in WHITEPIECES:
                        break
                    elif tab[x][y - i] != "vide":
                        l.append((x, y - i))
                        break

            else:
                break

        return l[:]

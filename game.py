from pion import Pion
from cavalier import Cavalier
from tour import Tour
from reine import Reine
from roi import Roi
from fou import Fou
import pygame as pg
from variables import *

class Chess:

    def __init__(self, surface):

        self.tab = []

        self.pion = Pion(surface)
        self.cavalier = Cavalier(surface)
        self.fou = Fou(surface)
        self.tour = Tour(surface)
        self.reine = Reine(surface)
        self.roi = Roi(surface)

        self.pTmp = ""
        self.coordTmp = (-1, -1)


        self.joueur = 0

        self.reinit()


    def reinit(self):
        l = []
        for i in range(X):
            l.append([])
            for j in range(Y):
                l[i].append("vide")

        # black: =======================
        l[0][0] = "b_tour"
        l[7][0] = "b_tour"

        l[1][0] = "b_cavalier"
        l[6][0] = "b_cavalier"

        l[2][0] = "b_fou"
        l[5][0] = "b_fou"

        l[3][0] = "b_reine"
        l[4][0] = "b_roi"

        for x in range(X):
            l[x][1] = "b_pion"

        # white: =======================
        l[0][7] = "w_tour"
        l[7][7] = "w_tour"

        l[1][7] = "w_cavalier"
        l[6][7] = "w_cavalier"

        l[2][7] = "w_fou"
        l[5][7] = "w_fou"

        l[3][7] = "w_reine"
        l[4][7] = "w_roi"

        for x in range(X):
            l[x][6] = "w_pion"

        self.tab = l[:]
        self.pTmp = "vide"

        self.joueur = 0

        # verif si tour et roi on bouge pour le rock
        self.w_t1 = False
        self.w_t2 = False
        self.w_r = False

        self.b_t1 = False
        self.b_t2 = False
        self.b_r = False


    def draw(self, surface):
        for i in range(X):
            for j in range(Y):
                color = (54, 54, 54)
                #color = (81, 42, 42)
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    color = (89, 89, 89)
                    #color = (124, 76, 62)
                pg.draw.rect(surface, color, [i*SIZE, j*SIZE, SIZE, SIZE])

                if self.tab[i][j] == "b_pion":
                    self.pion.draw(surface, i, j, SIZE, "black")
                elif self.tab[i][j] == "w_pion":
                    self.pion.draw(surface, i, j, SIZE, "white")
                elif self.tab[i][j] == "w_cavalier":
                    self.cavalier.draw(surface, i, j, SIZE, "white")
                elif self.tab[i][j] == "b_cavalier":
                    self.cavalier.draw(surface, i, j, SIZE, "black")
                elif self.tab[i][j] == "w_fou":
                    self.fou.draw(surface, i, j, SIZE, "white")
                elif self.tab[i][j] == "b_fou":
                    self.fou.draw(surface, i, j, SIZE, "black")
                elif self.tab[i][j] == "w_tour":
                    self.tour.draw(surface, i, j, SIZE, "white")
                elif self.tab[i][j] == "b_tour":
                    self.tour.draw(surface, i, j, SIZE, "black")
                elif self.tab[i][j] == "w_reine":
                    self.reine.draw(surface, i, j, SIZE, "white")
                elif self.tab[i][j] == "b_reine":
                    self.reine.draw(surface, i, j, SIZE, "black")
                elif self.tab[i][j] == "w_roi":
                    self.roi.draw(surface, i, j, SIZE, "white")
                elif self.tab[i][j] == "b_roi":
                    self.roi.draw(surface, i, j, SIZE, "black")

        if self.pTmp != "vide":
            pg.draw.rect(surface, "red", [self.coordTmp[0] * SIZE, self.coordTmp[1] * SIZE, SIZE, SIZE], SIZE // 20)
            if self.pTmp in ("w_pion", "b_pion"):
                l = self.pion.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab, self.coordTmp[1])
            elif self.pTmp in ("w_cavalier", "b_cavalier"):
                l = self.cavalier.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
            elif self.pTmp in ("w_fou", "b_fou"):
                l = self.fou.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
            elif self.pTmp in ("w_tour", "b_tour"):
                l = self.tour.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
            elif self.pTmp in ("w_reine", "b_reine"):
                l = self.reine.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
            elif self.pTmp in ("w_roi", "b_roi"):
                if self.joueur == 0:
                    list = [self.w_r, self.w_t1, self.w_t2]
                else:
                    list = [self.b_r, self.b_t1, self.b_t2]
                l = self.roi.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab, self.joueur, list)
            else:
                l = [(-1, -1)]
            for coord in l:
                if self.tab[coord[0]][coord[1]] != "vide":
                    pg.draw.circle(surface, "black", (coord[0] * SIZE + SIZE // 2, coord[1] * SIZE + SIZE // 2),
                                   SIZE//2, SIZE//15)
                else:
                    pg.draw.circle(surface, "black", (coord[0] * SIZE + SIZE//2, coord[1] * SIZE + SIZE//2), SIZE//10)

    def setCoordTmp(self, coord):
        if self.joueur == 0:
            if self.tab[coord[0]][coord[1]] in WHITEPIECES:
                self.coordTmp = coord
        else:
            if self.tab[coord[0]][coord[1]] in BLACKPIECES:
                self.coordTmp = coord


    def setPtmpCoord(self, coord):
        if self.joueur == 0:
            if self.tab[coord[0]][coord[1]] in WHITEPIECES:
                self.pTmp = self.tab[coord[0]][coord[1]]
        else:
            if self.tab[coord[0]][coord[1]] in BLACKPIECES:
                self.pTmp = self.tab[coord[0]][coord[1]]

    def setPtmp(self, Ptmp):
        self.pTmp = Ptmp

    def getCoordTmp(self):
        return self.pTmp

    def getPtmp(self):
        return self.pTmp

    def getCase(self, coord):
        return self.tab[coord[0]][coord[1]]

    def changer_joueur(self):
        self.joueur = (self.joueur+1) % 2

    def getJoueur(self):
        return self.joueur

    def deplacement(self, coord):
        if self.coordTmp == (0,0) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "b_tour":
            self.b_t1 = True
        elif self.coordTmp == (7,0) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "b_tour":
            self.b_t2 = True
        elif self.coordTmp == (0,7) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "w_tour":
            self.w_t1 = True
        elif self.coordTmp == (4,7) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "w_roi":
            self.w_r = True
        elif self.coordTmp == (7,7) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "w_tour":
            self.w_t2 = True
        elif self.coordTmp == (4,0) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "b_roi":
            self.b_r = True

        if self.joueur == 0:
            if self.coordTmp == (4, 7) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "w_roi" and coord == (6, 7):
                self.tab[5][7] = "w_tour"
                self.tab[7][7] = "vide"

            elif self.coordTmp == (4, 7) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "w_roi" and coord == (2, 7):
                self.tab[3][7] = "w_tour"
                self.tab[0][7] = "vide"

        else:
            if self.coordTmp == (4, 0) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "b_roi" and coord == (6, 0):
                self.tab[5][0] = "b_tour"
                self.tab[7][0] = "vide"

            elif self.coordTmp == (4, 0) and self.tab[self.coordTmp[0]][self.coordTmp[1]] == "b_roi" and coord == (2, 0):
                self.tab[3][0] = "b_tour"
                self.tab[0][0] = "vide"

        self.tab[coord[0]][coord[1]] = self.pTmp
        self.tab[self.coordTmp[0]][self.coordTmp[1]] = "vide"
        self.pTmp = "vide"


    def verif_deplacement(self, coord):

        if self.pTmp in ("w_pion", "b_pion"):
            l = self.pion.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab, self.coordTmp[1])
        elif self.pTmp in ("w_cavalier", "b_cavalier"):
            l = self.cavalier.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
        elif self.pTmp in ("w_fou", "b_fou"):
            l = self.fou.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
        elif self.pTmp in ("w_tour", "b_tour"):
            l = self.tour.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
        elif self.pTmp in ("w_reine", "b_reine"):
            l = self.reine.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab)
        elif self.pTmp in ("w_roi", "b_roi"):
            if self.joueur == 0:
                list = [self.w_r, self.w_t1, self.w_t2]
            else:
                list = [self.b_r, self.b_t1, self.b_t2]
            l = self.roi.case_possible(self.coordTmp[0], self.coordTmp[1], self.tab, self.joueur, list)
        else:
            l = [(-1, -1)]
        if coord in l:
            return True
        return False

    def verif_echec(self):
        pass

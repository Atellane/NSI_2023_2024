import tkinter as tk
from graphe import Graphe
from time import sleep
from random import randint, choice, shuffle
import sys

class Labyrinthe:
    """Implémentation d'une classe permettant la génération facile et rapide de labyrinthe avec tkinter."""
    def __init__(self: object, hauteur: int, largeur: int) -> object:
        self.largeur = largeur
        self.hauteur = hauteur
        sys.setrecursionlimit(self.hauteur*self.largeur * 100)

        self.__racine: Tk = tk.Tk()
        self.__grille: list = [[{"haut": True, "bas": True, "gauche": True, "droite": True} for _ in range(self.largeur)] for _ in range(self.hauteur)]
        self.__graph: Graphe = self.creer_graphe_a_partir_labyrinthe()
    
    def afficher(self: object) -> None:
        """Crée la grille de base et les boutons nécessaires à la création d'un labyrinthe et à sa résolution."""
        for _, children in self.__racine.children.items():
            children.pack_forget()

        self.__canvas: Canvas = tk.Canvas(self.__racine, width=self.largeur*20, height=self.hauteur*20)
        self.__canvas.pack()

        for i in range(self.hauteur):
            for j in range(self.largeur):
                x1, y1 = j * 20, i * 20
                x2, y2 = x1 + 20, y1 + 20
                cellule = self.__grille[i][j]

                # Dessiner le mur du haut s'il est présent
                if cellule["haut"]:
                    self.__canvas.create_line(x1, y1, x2, y1, width=2)

                # Dessiner le mur de gauche s'il est présent
                if cellule["gauche"]:
                    self.__canvas.create_line(x1, y1, x1, y2, width=2)

                # # Dessiner le mur de droite s'il est présent
                # if j + 1 < self.largeur and self.__grille[i][j + 1]["gauche"]:
                #     self.__canvas.create_line(x2, y1, x2, y2, width=2)

                # # Dessiner le mur du bas s'il est présent
                # if i + 1 < self.hauteur and self.__grille[i + 1][j]["haut"]:
                #     self.__canvas.create_line(x1, y2, x2, y2, width=2)


        bouton_effacer: Button = tk.Button(self.__racine, text="Effacer le chemin suivi.", command=self.suppr_chemin_suivi)
        bouton_effacer.pack(side=tk.BOTTOM)
        bouton_dijsktra: Button = tk.Button(self.__racine, text="dijkstra", command=self.dijsktra_graphe)
        bouton_dijsktra.pack(side=tk.BOTTOM)
        bouton_main_a_droite: Button = tk.Button(self.__racine, text="main à droite", command=self.main_a_droite)
        bouton_main_a_droite.pack(side=tk.BOTTOM)
        bouton_gen_labyrinthe: Button = tk.Button(self.__racine, text="recursion", command=self.__parcours_en_profondeur)
        bouton_gen_labyrinthe.pack(side=tk.BOTTOM)

    def creer_graphe_a_partir_labyrinthe(self: object, premier_appel: bool=True) -> Graphe:
        """Crée un graphe à partir de l'objet Labyrinthe."""
        graph: Graphe = Graphe()

        if premier_appel:
            for i in range(self.hauteur):
                for j in range(self.largeur):
                    nom_sommet: tuple = (i, j)
                    graph.ajouter_sommet(nom_sommet)

                    if i != 0 and i > 0:
                        graph.ajouter_sommet((i-1, j))
                        graph.ajouter_arete(nom_sommet, (i-1, j), 1)
                    if i != self.hauteur - 1 and i < self.hauteur - 1:
                        graph.ajouter_sommet((i+1, j))
                        graph.ajouter_arete(nom_sommet, (i+1, j), 1)
                    if j != 0 and j > 0:
                        graph.ajouter_sommet((i, j-1))
                        graph.ajouter_arete(nom_sommet, (i, j-1), 1)
                    if j != self.largeur - 1 and j < self.largeur - 1:
                        graph.ajouter_sommet((i, j+1))
                        graph.ajouter_arete(nom_sommet, (i, j+1), 1)
            print(graph)
        else:
            for i in range(self.hauteur):
                for j in range(self.largeur):
                    nom_sommet: tuple = (i, j)
                    graph.ajouter_sommet(nom_sommet)

                    if not self.__grille[i][j]["bas"] and i != 0 and i > 0:
                        graph.ajouter_sommet((i-1, j))
                        graph.ajouter_arete(nom_sommet, (i-1, j), 1)
                    if not self.__grille[i][j]["haut"] and i != self.hauteur - 1 and i < self.hauteur - 1:
                        graph.ajouter_sommet((i+1, j))
                        graph.ajouter_arete(nom_sommet, (i+1, j), 1)
                    if not self.__grille[i][j]["droite"] and j != 0 and j > 0:
                        graph.ajouter_sommet((i, j-1))
                        graph.ajouter_arete(nom_sommet, (i, j-1), 1)
                    if not self.__grille[i][j]["gauche"] and j != self.largeur - 1 and j < self.largeur - 1:
                        graph.ajouter_sommet((i, j+1))
                        graph.ajouter_arete(nom_sommet, (i, j+1), 1)
            print(graph)

        return graph

    def main_a_droite(self: object, entree: tuple=None, sortie: tuple=None) -> None:
        """Implémentation de la résolution de labyrinthe par la technique de la main droite."""
        self.suppr_chemin_suivi()
        if entree == None:
            entree = (0, 0)
        if sortie == None:
            sortie = (self.hauteur - randint(1, self.hauteur-1), self.largeur - randint(1, self.largeur-1))
        self.__canvas.create_rectangle(entree[1]*20, entree[0]*20, entree[1]*20 + 20, entree[0]*20 + 20, fill="blue", outline="", tags="entree")
        self.__canvas.create_rectangle(sortie[1]*20, sortie[0]*20, sortie[1]*20 + 20, sortie[0]*20 + 20, fill="red", outline="", tags="sortie")
        self.__racine.update_idletasks()
        sleep(1)

        chemin_suivi: list = [entree]
        sommet_courant: tuple = entree
        stack: list = []

        while sommet_courant != sortie:
            voisins = self.__graph.voisins(sommet_courant)
            non_visites = [voisin for voisin in voisins if voisin not in chemin_suivi]

            if non_visites:
                voisin_suivant = choice(non_visites)
                stack.append(sommet_courant)
                sommet_courant = voisin_suivant
                chemin_suivi.append(sommet_courant)
                self.__canvas.create_rectangle(sommet_courant[1]*20, sommet_courant[0]*20, sommet_courant[1]*20 + 20, sommet_courant[0]*20 + 20, fill="green", outline="", tags="chemin_suivi")
                self.__racine.update_idletasks()
                sleep(0.027)
            elif stack:
                sommet_courant = stack.pop()
                chemin_suivi.append(sommet_courant)
                self.__canvas.create_rectangle(sommet_courant[1]*20, sommet_courant[0]*20, sommet_courant[1]*20 + 20, sommet_courant[0]*20 + 20, fill="green", outline="", tags="chemin_suivi")
                self.__racine.update_idletasks()
                sleep(0.027)
            else:
                break

    def dijsktra_graphe(self: object, entree: tuple=None, sortie: tuple=None) -> None:
        """Implémentation de la résolution de labyrithe à l'aide de l'algorithme de dijsktra."""
        self.suppr_chemin_suivi()
        if entree == None:
            entree = (0, 0)
        if sortie == None:
            sortie = (self.hauteur - randint(1, self.hauteur-2), self.largeur - randint(1, self.largeur-2))
            # sortie = (self.hauteur - 1, self.largeur - 1)
        self.__canvas.create_rectangle(entree[1]*20, entree[0]*20, entree[1]*20 + 20, entree[0]*20 + 20, fill="blue", outline="", tags="entree")
        self.__canvas.create_rectangle(sortie[1]*20, sortie[0]*20, sortie[1]*20 + 20, sortie[0]*20 + 20, fill="red", outline="", tags="sortie")
        self.__racine.update_idletasks()
        distances = self.__graph.dijkstra(sortie)
        chemin_suivi: list = [entree]
        sommet_courant: tuple = entree

        # Affichez le chemin suivi après chaque itération avec une pause
        self.__canvas.create_rectangle(sommet_courant[1]*20, sommet_courant[0]*20, sommet_courant[1]*20 + 20, sommet_courant[0]*20 + 20, fill="green", outline="", tags="chemin_suivi")
        self.__racine.update_idletasks()
        # sleep(0.027)  # Pause de 0.027 seconde (ajustez selon vos besoins)

        while distances[sommet_courant][1] != None:
            sommet_courant = distances[sommet_courant][1]
            chemin_suivi.append(sommet_courant)
            self.__canvas.create_rectangle(sommet_courant[1]*20, sommet_courant[0]*20, sommet_courant[1]*20 + 20, sommet_courant[0]*20 + 20, fill="green", outline="", tags="chemin_suivi")
            self.__racine.update_idletasks()
            # sleep(0.027)

    def suppr_chemin_suivi(self: object) -> None:
        """Supprime la représentation du chemin parcouru."""
        if self.__racine.winfo_exists():
            self.__canvas.delete("chemin_suivi")
            self.__canvas.delete("sortie")
            self.__canvas.delete("entree")

    def enlever_mur(self: object, cellule_actuelle: tuple, cellule_suivante: tuple) -> None:
            i_actuelle, j_actuelle = cellule_actuelle
            i_suivante, j_suivante = cellule_suivante

            if i_suivante > i_actuelle:
                self.__grille[i_actuelle][j_actuelle]["bas"] = False
                self.__grille[i_suivante][j_suivante]["haut"] = False
            elif i_suivante < i_actuelle:
                self.__grille[i_actuelle][j_actuelle]["haut"] = False
                self.__grille[i_suivante][j_suivante]["bas"] = False
            elif j_suivante > j_actuelle:
                self.__grille[i_actuelle][j_actuelle]["droite"] = False
                self.__grille[i_suivante][j_suivante]["gauche"] = False
            elif j_suivante < j_actuelle:
                self.__grille[i_actuelle][j_actuelle]["gauche"] = False
                self.__grille[i_suivante][j_suivante]["droite"] = False

    def __parcours_en_profondeur(self: object) -> None:
        deja_visite = []
        self.__grille = [[{"haut": True, "bas": True, "gauche": True, "droite": True} for _ in range(self.largeur)] for _ in range(self.hauteur)]
        cellule_depart = (choice(range(self.hauteur)), choice(range(self.largeur)))
        self.__graph = self.creer_graphe_a_partir_labyrinthe()    
        def parcours_en_profondeur(sommet_depart: str=None) -> list:
            print("UwU")
            if len(deja_visite) == (self.__graph.nombre_de_sommet() - 1):
                deja_visite.append(sommet_depart)
            else:
                deja_visite.append(sommet_depart)
                voisins: list = list(self.__graph.voisins(sommet_depart))
                shuffle(voisins)
                for voisin in voisins:
                    if voisin not in deja_visite:
                        parcours_en_profondeur(voisin)

        parcours_en_profondeur(cellule_depart)
        for coordonnee in range(1, len(deja_visite)):
            self.enlever_mur(deja_visite[coordonnee-1], deja_visite[coordonnee])

        self.__graph = self.creer_graphe_a_partir_labyrinthe(False)
        print(self.__graph)
        self.afficher()

    def mainloop(self: object) -> None:
        """Boucle principale, permet de lancer l'affichage de tout le travail exécuté auparavant. À mettre en fin de fichier."""
        self.__racine.mainloop()

if __name__ == "__main__":
    labyrinthe = Labyrinthe(40, 94)
    # labyrinthe = Labyrinthe(20, 50)
    labyrinthe.afficher()
    labyrinthe.mainloop()
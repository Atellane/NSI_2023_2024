import tkinter as tk
from graphe import Graphe
from time import sleep
from random import randint, choice, shuffle
import sys

class Labyrinthe:
    """Implémentation d'une classe permettant la génération facile et rapide de labyrinthe avec tkinter."""
    def __init__(self: object, hauteur: int, largeur: int) -> object:
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__coord_hauteur = 800//self.__hauteur
        self.__coord_largeur = 1880//self.__largeur
        sys.setrecursionlimit(self.__hauteur * self.__largeur * 10)

        self.__racine: tk.Tk = tk.Tk()
        self.__grille: list = [[{"haut": True, "bas": True, "gauche": True, "droite": True} for _ in range(self.__largeur)] for _ in range(self.__hauteur)]
        self.__graph: Graphe = self.__creer_graphe_a_partir_labyrinthe()
        self.__canvas: Canvas = None
        self.__afficher()
        self.__racine.mainloop()
    
    def __afficher(self: object) -> None:
        """Crée la grille de base et les boutons nécessaires à la création d'un labyrinthe et à sa résolution."""
        for _, children in self.__racine.children.items():
            children.pack_forget()

        self.__canvas = tk.Canvas(self.__racine, width=1880, height=800)
        self.__canvas.pack()

        for i in range(self.__hauteur):
            for j in range(self.__largeur):
                nom_sommet = (i, j)
                voisins = list(self.__graph.voisins(nom_sommet))

                if (i - 1, j) not in voisins:
                    self.__canvas.create_line(j * self.__coord_largeur, i * self.__coord_hauteur, (j + 1) * self.__coord_largeur, i * self.__coord_hauteur, fill="black", width=2)
                    self.__racine.update_idletasks()

                if (i + 1, j) not in voisins:
                    self.__canvas.create_line(j * self.__coord_largeur, (i + 1) * self.__coord_hauteur, (j + 1) * self.__coord_largeur, (i + 1) * self.__coord_hauteur, fill="black", width=2)
                    self.__racine.update_idletasks()

                if (i, j - 1) not in voisins:
                    self.__canvas.create_line(j * self.__coord_largeur, i * self.__coord_hauteur, j * self.__coord_largeur, (i + 1) * self.__coord_hauteur, fill="black", width=2)
                    self.__racine.update_idletasks()

                if (i, j + 1) not in voisins:
                    self.__canvas.create_line((j + 1) * self.__coord_largeur, i * self.__coord_hauteur, (j + 1) * self.__coord_largeur, (i + 1) * self.__coord_hauteur, fill="black", width=2)
                    self.__racine.update_idletasks()

        bouton_effacer: Button = tk.Button(self.__racine, text="Effacer le chemin suivi.", command=self.__suppr_chemin_suivi)
        bouton_effacer.pack(side=tk.BOTTOM)
        bouton_dijsktra: Button = tk.Button(self.__racine, text="Dijkstra", command=self.__dijsktra_graphe)
        bouton_dijsktra.pack(side=tk.BOTTOM)
        bouton_main_a_droite: Button = tk.Button(self.__racine, text="Main à droite", command=self.__main_a_droite)
        bouton_main_a_droite.pack(side=tk.BOTTOM)
        bouton_gen_labyrinthe: Button = tk.Button(self.__racine, text="Récursion", command=self.__parcours_en_profondeur)
        bouton_gen_labyrinthe.pack(side=tk.BOTTOM)
        self.__bouton_largeur: Scale = tk.Scale(self.__racine, from_=40, to=141, orient=tk.HORIZONTAL, showvalue=0, command=self.__modif_label_largeur)
        self.__bouton_largeur.bind("<ButtonRelease>", self.__modifier_largeur)
        self.__bouton_largeur.set(self.__largeur)
        self.__bouton_largeur.pack(side=tk.BOTTOM)
        self.__label_largeur: Label = tk.Label(self.__racine, fg="black", width=20, text=f"largeur : {self.__largeur}")
        self.__label_largeur.pack(side=tk.BOTTOM)
        self.__bouton_hauteur: Scale = tk.Scale(self.__racine, from_=23, to=60, orient=tk.HORIZONTAL, showvalue=0, command=self.__modif_label_hauteur)
        self.__bouton_hauteur.bind("<ButtonRelease>", self.__modifier_hauteur)
        self.__bouton_hauteur.set(self.__hauteur)
        self.__bouton_hauteur.pack(side=tk.BOTTOM)
        self.__label_hauteur: Label = tk.Label(self.__racine, fg="black", width=20, text=f"hauteur : {self.__hauteur}")
        self.__label_hauteur.pack(side=tk.BOTTOM)

    def __modif_label_largeur(self: object, valeur: int) -> None:
        self.__label_largeur.config(text=f"largeur : {valeur}")
    
    def __modifier_largeur(self: object, event: object) -> None:
        self.__largeur = self.__bouton_largeur.get()
        self.__coord_largeur = 1880//self.__largeur

    def __modif_label_hauteur(self: object, valeur: int) -> None:
        self.__label_hauteur.config(text=f"hauteur : {valeur}")

    def __modifier_hauteur(self: object, object: object) -> None:
        self.__hauteur = self.__bouton_hauteur.get()
        self.__coord_hauteur = 800//self.__hauteur

    def __creer_graphe_a_partir_labyrinthe(self: object, premier_appel: bool=True) -> Graphe:
        """Crée un graphe à partir de l'objet Labyrinthe."""
        graph: Graphe = Graphe()

        if premier_appel:
            for i in range(self.__hauteur):
                for j in range(self.__largeur):
                    nom_sommet: tuple = (i, j)
                    graph.ajouter_sommet(nom_sommet)

                    if i != 0 and i > 0:
                        graph.ajouter_sommet((i-1, j))
                        graph.ajouter_arete(nom_sommet, (i-1, j), 1)
                    if i != self.__hauteur - 1 and i < self.__hauteur - 1:
                        graph.ajouter_sommet((i+1, j))
                        graph.ajouter_arete(nom_sommet, (i+1, j), 1)
                    if j != 0 and j > 0:
                        graph.ajouter_sommet((i, j-1))
                        graph.ajouter_arete(nom_sommet, (i, j-1), 1)
                    if j != self.__largeur - 1 and j < self.__largeur - 1:
                        graph.ajouter_sommet((i, j+1))
                        graph.ajouter_arete(nom_sommet, (i, j+1), 1)

        else:
            for i in range(self.__hauteur):
                for j in range(self.__largeur):
                    nom_sommet: tuple = (i, j)
                    graph.ajouter_sommet(nom_sommet)

                    if not self.__grille[i][j]["bas"] and i != 0 and i > 0:
                        graph.ajouter_sommet((i-1, j))
                        graph.ajouter_arete(nom_sommet, (i-1, j), 1)
                    if not self.__grille[i][j]["haut"] and i != self.__hauteur - 1 and i < self.__hauteur - 1:
                        graph.ajouter_sommet((i+1, j))
                        graph.ajouter_arete(nom_sommet, (i+1, j), 1)
                    if not self.__grille[i][j]["droite"] and j != 0 and j > 0:
                        graph.ajouter_sommet((i, j-1))
                        graph.ajouter_arete(nom_sommet, (i, j-1), 1)
                    if not self.__grille[i][j]["gauche"] and j != self.__largeur - 1 and j < self.__largeur - 1:
                        graph.ajouter_sommet((i, j+1))
                        graph.ajouter_arete(nom_sommet, (i, j+1), 1)

        return graph

    def __main_a_droite(self: object, entree: tuple=None, sortie: tuple=None) -> None:
        """Implémentation de la résolution de labyrinthe par la technique de la main droite."""
        self.__suppr_chemin_suivi()
        if entree == None:
            entree = (0, 0)
        if sortie == None:
            sortie = (self.__hauteur - randint(1, self.__hauteur-1), self.__largeur - randint(1, self.__largeur-1))
        self.__canvas.create_rectangle(entree[1]*self.__coord_largeur, entree[0]*self.__coord_hauteur, entree[1]*self.__coord_largeur + self.__coord_largeur, entree[0]*self.__coord_hauteur + self.__coord_hauteur, fill="blue", outline="", tags="entree")
        self.__canvas.create_rectangle(sortie[1]*self.__coord_largeur, sortie[0]*self.__coord_hauteur, sortie[1]*self.__coord_largeur + self.__coord_largeur, sortie[0]*self.__coord_hauteur + self.__coord_hauteur, fill="red", outline="", tags="sortie")
        self.__racine.update_idletasks()
        # sleep(0.00002)

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
                self.__canvas.create_rectangle(sommet_courant[1]*self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur, sommet_courant[1]*self.__coord_largeur + self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur + self.__coord_hauteur, fill="green", outline="", tags="chemin_suivi")
                self.__racine.update_idletasks()
                # sleep(0.027)
            elif stack:
                sommet_courant = stack.pop()
                chemin_suivi.append(sommet_courant)
                self.__canvas.create_rectangle(sommet_courant[1]*self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur, sommet_courant[1]*self.__coord_largeur + self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur + self.__coord_hauteur, fill="green", outline="", tags="chemin_suivi")
                self.__racine.update_idletasks()
                # sleep(0.027)
            else:
                break

    def __dijsktra_graphe(self: object, entree: tuple=None, sortie: tuple=None) -> None:
        """Implémentation de la résolution de labyrithe à l'aide de l'algorithme de dijsktra."""
        self.__suppr_chemin_suivi()
        if entree == None:
            entree = (0, 0)
        if sortie == None:
            sortie = (self.__hauteur - randint(1, self.__hauteur-2), self.__largeur - randint(1, self.__largeur-2))
            # sortie = (self.__hauteur - 1, self.__largeur - 1)
        self.__canvas.create_rectangle(entree[1]*self.__coord_largeur, entree[0]*self.__coord_hauteur, entree[1]*self.__coord_largeur + self.__coord_largeur, entree[0]*self.__coord_hauteur + self.__coord_hauteur, fill="blue", outline="", tags="entree")
        self.__canvas.create_rectangle(sortie[1]*self.__coord_largeur, sortie[0]*self.__coord_hauteur, sortie[1]*self.__coord_largeur + self.__coord_largeur, sortie[0]*self.__coord_hauteur + self.__coord_hauteur, fill="red", outline="", tags="sortie")
        self.__racine.update_idletasks()
        distances = self.__graph.dijkstra(sortie)
        chemin_suivi: list = [entree]
        sommet_courant: tuple = entree

        # Affichez le chemin suivi après chaque itération avec une pause
        self.__canvas.create_rectangle(sommet_courant[1]*self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur, sommet_courant[1]*self.__coord_largeur + self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur + self.__coord_hauteur, fill="green", outline="", tags="chemin_suivi")
        self.__racine.update_idletasks()
        # sleep(0.027)  # Pause de 0.027 seconde (ajustez selon vos besoins)

        while distances[sommet_courant][1] != None:
            sommet_courant = distances[sommet_courant][1]
            chemin_suivi.append(sommet_courant)
            self.__canvas.create_rectangle(sommet_courant[1]*self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur, sommet_courant[1]*self.__coord_largeur + self.__coord_largeur, sommet_courant[0]*self.__coord_hauteur + self.__coord_hauteur, fill="green", outline="", tags="chemin_suivi")
            self.__racine.update_idletasks()
            # sleep(1)

    def __suppr_chemin_suivi(self: object) -> None:
        """Supprime la représentation du chemin parcouru."""
        if self.__racine.winfo_exists():
            self.__canvas.delete("chemin_suivi")
            self.__canvas.delete("sortie")
            self.__canvas.delete("entree")

    def __enlever_mur(self: object, cellule_actuelle: tuple, cellule_suivante: tuple) -> None:
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
        """Génère récursivement un nouveau labyrinthe, certaine partie générées (généralement pas pkus d'une ou deux cases) peuvent être totalement 
        innaccessible, si c'est le cas, djikstra n'ira pas au delà de la case départ et la main droite s'arrêtera après avoir remplis toutes les parties
        accessibles du labyrinthe."""
        deja_visite = []
        self.__grille = [[{"haut": True, "bas": True, "gauche": True, "droite": True} for _ in range(self.__largeur)] for _ in range(self.__hauteur)]
        cellule_depart = (choice(range(self.__hauteur)), choice(range(self.__largeur)))
        self.__graph = self.__creer_graphe_a_partir_labyrinthe()    
        def parcours_en_profondeur(sommet_depart: str=None) -> list:
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
            self.__enlever_mur(deja_visite[coordonnee-1], deja_visite[coordonnee])

        self.__graph = self.__creer_graphe_a_partir_labyrinthe(False)
        self.__afficher()

if __name__ == "__main__":
    # labyrinthe = Labyrinthe(40, 94)
    labyrinthe = Labyrinthe(60,141)

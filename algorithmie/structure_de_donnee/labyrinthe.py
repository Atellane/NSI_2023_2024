import tkinter as tk
from graphe import Graphe
from time import sleep

class Labyrinthe:
    """Implémentation d'une classe permettant la génération facile et rapide de labyrinthe avec tkinter."""
    def __init__(self: object, largeur: int, hauteur: int) -> object:
        self.largeur = largeur
        self.hauteur = hauteur
        self.__grille: list = self.__generer_grille()
        self.__graph: Graphe = self.creer_graphe_a_partir_labyrinthe()

    def __generer_grille(self: object) -> list:
        grille = [[{"haut": True, "bas": True, "gauche": True, "droite": True} for _ in range(self.largeur)] for _ in range(self.hauteur)]

        for i in range(self.hauteur):
            for j in range(self.largeur):
                grille[i][j]["haut"] = i == 0
                grille[i][j]["bas"] = i == self.hauteur - 1
                grille[i][j]["gauche"] = j == 0
                grille[i][j]["droite"] = j == self.largeur - 1

        return grille

    def afficher(self: object) -> None:
        """Crée la grille de base et les boutons nécessaires à la création d'un labyrinthe et à sa résolution."""
        self.__racine: Tk = tk.Tk()
        self.__canvas: Canvas = tk.Canvas(self.__racine, width=self.largeur*20, height=self.hauteur*20)
        self.__canvas.pack()

        for i in range(self.hauteur):
            for j in range(self.largeur):
                x, y = j*20, i*20
                self.__canvas.create_line(x, y, x + 20, y, width=2)
                self.__canvas.create_line(x, y + 20, x + 20, y + 20, width=2)
                self.__canvas.create_line(x, y, x, y + 20, width=2)
                self.__canvas.create_line(x + 20, y, x + 20, y + 20, width=2)

        bouton_effacer: Button = tk.Button(self.__racine, text="Effacer le chemin suivi", command=self.suppr_chemin_suivi)
        bouton_effacer.pack(side=tk.BOTTOM, pady=10)
        bouton_dijsktra: Button = tk.Button(self.__racine, text="dijkstra", command=self.dijsktra_graphe)
        bouton_dijsktra.pack(side=tk.BOTTOM, pady=10)

    def creer_graphe_a_partir_labyrinthe(self: object) -> Graphe:
        """Crée un graphe à partir de l'objet Labyrinthe."""
        graph: Graphe = Graphe()

        for i in range(self.hauteur):
            for j in range(self.largeur):
                nom_sommet: tuple = (i, j)
                graph.ajouter_sommet(nom_sommet)

                if not self.__grille[i][j]["haut"] and i > 0:
                    graph.ajouter_sommet((i-1, j))
                    graph.ajouter_arete(nom_sommet, (i-1, j), 1)
                if not self.__grille[i][j]["bas"] and i < self.hauteur - 1:
                    graph.ajouter_sommet((i+1, j))
                    graph.ajouter_arete(nom_sommet, (i+1, j), 1)
                if not self.__grille[i][j]["gauche"] and j > 0:
                    graph.ajouter_sommet((i, j-1))
                    graph.ajouter_arete(nom_sommet, (i, j-1), 1)
                if not self.__grille[i][j]["droite"] and j < self.largeur - 1:
                    graph.ajouter_sommet((i, j+1))
                    graph.ajouter_arete(nom_sommet, (i, j+1), 1)

        return graph

    def main_a_droite_graphe(self: object, entree: tuple=None, sortie: tuple=None) -> None:
        """Implémentation de la résolution de labyrinthe par la technique de la main droite."""
        if entree == None:
            entree = (0, 0)
        if sortie == None:
            sortie = (self.hauteur - 1, self.largeur - 1)
        chemin_suivi: list = [entree]
        sommet_courant: tuple = entree

        # Affichez le chemin suivi après chaque itération avec une pause
        self.afficher_chemin_suivi_direct(chemin_suivi)
        self.__racine.update_idletasks()
        sleep(0.027)  # Pause de 0.027 seconde (ajustez selon vos besoins)

        while sommet_courant != sortie:
            pass


    def dijsktra_graphe(self: object, entree: tuple=None, sortie: tuple=None) -> None:
        """Implémentation de la résolution de labyrithe à l'aide de l'algorithme de dijsktra."""
        if entree == None:
            entree = (0, 0)
        if sortie == None:
            sortie = (self.hauteur - 1, self.largeur - 1)
        distances = self.__graph.dijkstra(sortie)
        chemin_suivi: list = [entree]
        sommet_courant: tuple = entree

        # Affichez le chemin suivi après chaque itération avec une pause
        self.afficher_chemin_suivi_direct(chemin_suivi)
        self.__racine.update_idletasks()
        sleep(0.027)  # Pause de 0.027 seconde (ajustez selon vos besoins)

        while distances[sommet_courant][1] is not None:
            sommet_courant = distances[sommet_courant][1]
            chemin_suivi.append(sommet_courant)
            self.afficher_chemin_suivi_direct(chemin_suivi)
            self.__racine.update_idletasks()
            sleep(0.027)

    def afficher_chemin_suivi_direct(self: object, chemin_suivi: list) -> None:
        """Affiche le chemin parcouru."""
        if self.__racine.winfo_exists():
            self.__canvas.delete("chemin_suivi")
            for i, j in chemin_suivi:
                x, y = j*20, i*20
                self.__canvas.create_rectangle(x, y, x + 20, y + 20, fill="green", outline="", tags="chemin_suivi")

    def suppr_chemin_suivi(self: object) -> None:
        """Supprime la représentation du chemin parcouru."""
        if self.__racine.winfo_exists():
            self.__canvas.delete("chemin_suivi")


    def mainloop(self: object) -> None:
        """Boucle principale, permet de lancer l'affichage de tout le travail exécuté auparavant. À mettre en fin de fichier."""
        self.__racine.mainloop()

# Exemple d'utilisation
if __name__ == "__main__":
    labyrinthe = Labyrinthe(70, 45)
    labyrinthe.afficher()
    labyrinthe.mainloop()
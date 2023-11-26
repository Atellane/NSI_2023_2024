"""
Jeux de 32 cartes, le but est de se débarasser de toutes ses cartes. le premier joueur pose une carte face visible, les autres pose une carte sensé être de la même
couleur. Si un joueur pense que le joueur qui vient de joué ment, il peut le dire. S'il a effectivement mentis, il ramasse le tas ; sinon, celui qui l'as accusé
ramasse le tas. Le premier à se débarasser de toutes ses cartes a gagné.
"""
from paquet_carte import Paquet_Cartes
from random import randint

class Partie():
    def __init__(self: object, nombreJoueurs: int) -> object:
        self.__nombreJoueurs: int = nombreJoueurs
        self.__joueurActuel : int = 0
        self.__paquet: object = Paquet_Cartes(32)
        self.__cartes_joueurs: list = self.__distribuer_les_cartes()
        self.__premiereCarte: object = None
        self.__tas: list = []
        self.__jeux()

    def __distribuer_les_cartes(self: object) -> list:
        paquet: object = self.__paquet
        paquet: list = paquet.Obtenir_Cartes()
        paquet_temp: list = []
        for numeroDuJoueur in range(1, self.__nombreJoueurs+1):
            paquet_temp.append([])
            for _ in range(8):
                paquet_temp[numeroDuJoueur - 1].append(paquet[randint(0, len(paquet) - 1)])
        return paquet_temp

    def __jeux(self: object, debut: bool = True) -> None:
        debut: bool = True
        while len(self.__cartes_joueurs[self.__joueurActuel - 1]) != 0:
            if self.__joueurActuel < self.__nombreJoueurs:
                self.__joueurActuel += 1
            else:
                self.__joueurActuel = 1
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"C'est le tour du joueur {self.__joueurActuel}.")
            input("Appuyez sur entrer quand les autres joueurs regardent ailleurs.\n")
            print("Voici votre paquet :")
            numCarte: int = 1
            for carte in self.__cartes_joueurs[self.__joueurActuel - 1]:
                print(f"{numCarte} : {carte.Affiche_figure()}", end=" ")
                numCarte += 1
            print("\n")
            carteAjouer: int = int(input("choisissez le numéro de la carte à jouer :\n"))
            if debut:
                self.__premiereCarte = self.__cartes_joueurs[self.__joueurActuel - 1][carteAjouer - 1]
                self.__cartes_joueurs[self.__joueurActuel - 1].pop(carteAjouer - 1)
            else:
                self.__tas.append(self.__cartes_joueurs[self.__joueurActuel - 1][carteAjouer - 1])
                self.__cartes_joueurs[self.__joueurActuel - 1].pop(carteAjouer - 1)
                self.__est_un_menssonge(carteAjouer)
            debut: bool = False
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"Le joueur n°{self.__joueurActuel} a gagné !")

    def __est_un_menssonge(self: object, carteAjouer: int) -> None:
        menssonge: int = input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nsi vous pensez que la personne mentais et n'a pas posé une carte de couleur \"{self.__premiereCarte.Affiche_couleur()}\", mettez votre numéro de joueur :\n")
        if menssonge != '':
            menssonge = int(menssonge)
        else:
            return
        if menssonge <= self.__nombreJoueurs and menssonge != self.__joueurActuel:
            carteActuelle: object = self.__cartes_joueurs[self.__joueurActuel - 1][carteAjouer - 1]
            premiereCarte: object = self.__premiereCarte
            if carteActuelle.Affiche_couleur() != premiereCarte.Affiche_couleur():
                self.__cartes_joueurs[self.__joueurActuel - 1].append(self.__premiereCarte)
                for carte in self.__tas:
                    self.__cartes_joueurs[self.__joueurActuel - 1].append(carte)
                print(f"Le joueur n°{self.__joueurActuel} avait menti. Il récupère tous le tas.")
            else:
                self.__cartes_joueurs[menssonge - 1].append(self.__premiereCarte)
                for carte in self.__tas:
                    self.__cartes_joueurs[menssonge - 1].append(carte)
                print(f"Le joueur n°{self.__joueurActuel} n'avait pas menti. le joueur n°{menssonge} qui l'as accusé récupère tous le tas.")
        elif menssonge <= self.__nombreJoueurs:
            print(f"votre numéro de joueur dénonceur du menssonge n'existe pas, on considère donc que personne n'as estimé que le joueur n°{self.__joueurActuel} a menti.")
        elif menssonge == self.__joueurActuel:
            print("Un joueur ne peut pas se dénoncer lui même.")
        else:
            # rien a faire
            pass

if __name__ == "__main__":
    nombreDeJoueur: int = int(input("à combien voulez-vous jouer ?"))
    nouveauJeux: object = Partie(nombreDeJoueur)
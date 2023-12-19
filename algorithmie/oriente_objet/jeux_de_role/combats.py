from random import randint
from personnages import Personnage

class Combats():
    def __init__(self: object) -> object:
        vie_perso_1 = randint(1000, 10000)
        vie_perso_2 = randint(1000, 10000)
        point_armure_1 = randint(100, 1000)
        point_armure_2 = randint(100, 1000)
        arme_perso_1 = randint(100, 1000)
        arme_perso_2 = randint(100, 1000)
        personnages1 = Personnage("personnage 1", vie_perso_1, point_armure_1, arme_perso_1, "arme perso 1")
        personnages2 = Personnage("personnage 2", vie_perso_2, point_armure_2, arme_perso_2, "arme perso 2")
        self.__personnage1 = personnages1
        self.__personnage2 = personnages2
        self.__combats()

    def __attaque(self: object, personnages1: object, personnages2: object) -> None:
        qui_attaque = randint(0, 100)
        if qui_attaque < 50:
            qui_attaque = personnages1
            qui_attaque_pas = personnages2
        else:
            qui_attaque = personnages2
            qui_attaque_pas = personnages1
        print(f"c'est {qui_attaque.getNom()} qui attaque !")
        attaque = randint(1, 100)
        forceAttaque = qui_attaque.getForceDAttaque()
        attaque = forceAttaque * attaque
        print(f"iel enlève {attaque} points de vies à {qui_attaque_pas.getNom()}.")
        pointsDeVie = qui_attaque_pas.getPointsDeVie()
        qui_attaque_pas.setPointsDeVie(pointsDeVie - attaque)

    def __combats(self: object) -> None:
        personnages1 = self.__personnage1
        personnages2 = self.__personnage2
        while personnages1.getPointsDeVie() > 0 and personnages2.getPointsDeVie() > 0:
            self.__attaque(personnages1, personnages2)
        if personnages1.getPointsDeVie() > 0:
            print("personnages 1 a gagné :)")
        else:
            print("personnage 2 a gagné :)")

Combats()
"""Implémente une classe Personnage pour créer un jeux de rôle"""
class Personnage():
    def __init__(self: object, nom :str, pointsDeVie: int, pointsDArmure: int, forceDAttaque: int, arme: str) -> object:
        self.__nom = nom
        self.__pointsDeVie = pointsDeVie
        self.__pointsDArmure = pointsDArmure
        self.__forceDAttaque = forceDAttaque
        self.__arme = arme

    def getNom(self: object) -> str:
        """Pemet d'obtenir le nom du personnage"""
        return self.__nom

    def setNom(self: object, nom: str) -> None:
        """Permet de changer le nom du personnage"""
        self.__nom = nom

    def getPointsDeVie(self: object) -> int:
        """Pemet d'obtenir les points de vie du personnage"""
        return self.__pointsDeVie

    def setPointsDeVie(self : object, pointsDeVie: int) -> None:
        """Permet de changer les points de vie du personnage"""
        self.__pointsDeVie = pointsDeVie
    
    def getPointsDArmure(self: object) -> int:
        """Pemet d'obtenir les points d'armure du personnage"""
        return self.__pointsDArmure

    def setPointsDArmure(self : object, pointsDArmure: int) -> None:
        """Permet de changer les points d'armure du personnage"""
        self.__pointsDArmure = pointsDArmure
    
    def getForceDAttaque(self: object) -> int:
        """Pemet d'obtenir la force d'attaque du personnage"""
        return self.__forceDAttaque

    def setForceDAttaque(self : object, forceDAttaque: int) -> None:
        """Permet de changer la force d'attaque du personnage"""
        self.__forceDAttaque = forceDAttaque
    
    def getArme(self: object) -> str:
        """Pemet d'obtenir l'arme du personnage"""
        return self.__arme

    def setArme(self : object, arme: str) -> None:
        """Permet de changer l'arme du personnage"""
        self.__arme = arme
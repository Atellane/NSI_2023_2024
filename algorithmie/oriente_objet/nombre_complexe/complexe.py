from math import sqrt, atan2

"""implémentation basique des nombres complexes en python"""
class Complexe():
    def __init__(self: object, partieReelle: float, partieImaginaire: float) -> object:
        self.__partieReelle = partieReelle
        self.__partieImaginaire = partieImaginaire
        self.__module: float = self.__caluler_module()
        self.__argument: float = self.__caluler_argument()
        self.__complexeFormeAlgebrique: complex = f"{self.__partieReelle} + {self.__partieImaginaire}i"
        self.__complexeFormeExponentielle: complex = f"{self.__module}e^({self.__argument}i)"

    def __repr__(self: object) -> complex:
        return self.obtenir_forme_algebrique()

    def __caluler_module(self: object) -> float:
        return sqrt(self.__partieReelle**2 + self.__partieImaginaire**2)

    def __caluler_argument(self: object) -> float:
        if self.__partieReelle == 0 and self.__partieImaginaire == 0:
            return 0  # Par convention, argument de 0 + 0i est défini comme 0
        else:
            return atan2(self.__partieImaginaire, self.__partieReelle)

    def obtenir_partie_reelle(self: object) -> float:
        """retourne la partie réelle du nombre complexe"""
        return self.__partieReelle

    def obtenir_partie_imaginaire(self: object) -> float:
        """retourne la partie imaginaire du nombre complexe"""
        return self.__partieImaginaire

    def modifier_partie_reelle(self: object, nouvellePartieReelle: float) -> None:
        """modifie la partie réelle du nombre complexe"""
        self.__partieReelle = nouvellePartieReelle
        self.__module = self.__caluler_module()
        self.__argument = self.__caluler_argument()

    def modifier_partie_imaginaire(self: object, nouvellePartieImaginaire: float) -> None:
        """modifie la partie imaginaire du nombre complexe"""
        self.__partieImaginaire = nouvellePartieImaginaire
        self.__module = self.__caluler_module()
        self.__argument = self.__caluler_argument()

    def obtenir_module(self: object) -> float:
        """retourne le module du nombre complexe"""
        return self.__module

    def obtenir_argument(self: object) -> float:
        """retourne l'argument du nombre complexe"""
        return self.__argument

    def obtenir_forme_algebrique(self: object) -> complex:
        """retourne la forme algébrique du nombre complexe"""
        return self.__complexeFormeAlgebrique

    def obtenir_forme_exponentielle(self: object) -> complex:
        """retourne la forme exponentielle du nombre complexe"""
        return self.__complexeFormeExponentielle

if __name__ == "__main__":
    complexe: object = Complexe(3, 2)
    assert complexe.obtenir_partie_reelle() == 3, "probleme obtenir_partie_reelle"
    assert complexe.obtenir_partie_imaginaire() == 2, "probleme obtenir_partie_imaginaire"
    complexe.modifier_partie_reelle(2)
    assert complexe.obtenir_partie_reelle() == 2, "probleme modifier_partie_reelle"
    complexe.modifier_partie_imaginaire(3)
    assert complexe.obtenir_partie_imaginaire() == 3, "probleme modifier_partie_imaginaire"
    complexe.modifier_partie_reelle(3)
    complexe.modifier_partie_imaginaire(2)
    assert complexe.obtenir_module() == sqrt(complexe.obtenir_partie_reelle()**2 + complexe.obtenir_partie_imaginaire()**2), "probleme obtenir_module"
    if complexe.obtenir_partie_reelle() == 0 and complexe.obtenir_partie_imaginaire() == 0:
        assert complexe.obtenir_argument == 0, "probleme __caluler_argument pour reel 0 et imaginaire 0"
    else:
        assert complexe.obtenir_argument() == atan2(complexe.obtenir_partie_imaginaire(), complexe.obtenir_partie_reelle()), "probleme __caluler_argument pour reel différent de 0 et/ou imaginaire différent de 0"
    assert complexe.obtenir_forme_algebrique() == f"{complexe.obtenir_partie_reelle()} + {complexe.obtenir_partie_imaginaire()}i", "probleme à la définition de self.__complexeFormeAlgebrique"
    assert complexe.obtenir_forme_exponentielle() == f"{complexe.obtenir_module()}e^({complexe.obtenir_argument()}i)", "probleme à la définition de self.__complexeFormeExponentielle"
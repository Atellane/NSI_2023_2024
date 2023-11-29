from complexe import Complexe
"""implémentation des opérations de base sur les nombres complexes (addition, soustraction, multiplication, division)"""

class Operation_Complexe():
    @staticmethod
    def addition_deux_complexes(premierComplexe: object, deuxiemeComplexe: object) -> object:
        """additionne le premier complexe avec le deuxieme"""
        return Complexe(premierComplexe.obtenir_partie_reelle() + deuxiemeComplexe.obtenir_partie_reelle(), premierComplexe.obtenir_partie_imaginaire() + deuxiemeComplexe.obtenir_partie_imaginaire())
    
    @staticmethod
    def soustraction_deux_complexes(premierComplexe: object, deuxiemeComplexe: object) -> object:
        """soustrait le premier complexe par le deuxieme"""
        return Complexe(premierComplexe.obtenir_partie_reelle() - deuxiemeComplexe.obtenir_partie_reelle(), premierComplexe.obtenir_partie_imaginaire() - deuxiemeComplexe.obtenir_partie_imaginaire())

    @staticmethod
    def multiplication_deux_complexes(premierComplexe: object, deuxiemeComplexe: object) -> object:
        """multiplie le premier complexe par le deuxieme"""
        return Complexe(premierComplexe.obtenir_partie_reelle() * deuxiemeComplexe.obtenir_partie_reelle() - premierComplexe.obtenir_partie_imaginaire() * deuxiemeComplexe.obtenir_partie_imaginaire(), premierComplexe.obtenir_partie_reelle() * deuxiemeComplexe.obtenir_partie_reelle() + premierComplexe.obtenir_partie_imaginaire() * deuxiemeComplexe.obtenir_partie_imaginaire())

    @staticmethod
    def division_deux_complexes(premierComplexe: object, deuxiemeComplexe: object) -> object:
        """divise le premier complexe par le deuxieme"""
        return Complexe((premierComplexe.obtenir_partie_reelle() * deuxiemeComplexe.obtenir_partie_reelle() + premierComplexe.obtenir_partie_imaginaire() * deuxiemeComplexe.obtenir_partie_imaginaire()) / (deuxiemeComplexe.obtenir_partie_reelle()**2 + deuxiemeComplexe.obtenir_partie_imaginaire()**2), (premierComplexe.obtenir_partie_imaginaire() * deuxiemeComplexe.obtenir_partie_reelle() - premierComplexe.obtenir_partie_reelle() * deuxiemeComplexe.obtenir_partie_imaginaire()) / (deuxiemeComplexe.obtenir_partie_reelle()**2 + deuxiemeComplexe.obtenir_partie_imaginaire()**2))
    @staticmethod
    def addition_complexe_reel(complexe: object, reel: float) -> object:
        """additionne le complexe avec le réel"""
        return Complexe(complexe.obtenir_partie_reelle() + reel, complexe.obtenir_partie_imaginaire())

    @staticmethod
    def soustraction_complexe_reel(complexe: object, reel: float) -> object:
        """soustrait le complexe avec le réel"""
        return Complexe(complexe.obtenir_partie_reelle() - reel, complexe.obtenir_partie_imaginaire())

    @staticmethod
    def multiplication_complexe_reel(complexe: object, reel: float) -> object:
        """multiplie le complexe avec le reel"""
        return Complexe(complexe.obtenir_partie_reelle() * reel, complexe.obtenir_partie_imaginaire() * reel)

    @staticmethod
    def division_complexe_reel(complexe: object, reel: float) -> object:
        """divise le complexe avec le reel"""
        return Complexe(complexe.obtenir_partie_reelle() / reel, complexe.obtenir_partie_imaginaire() / reel)

if __name__ == "__main__":
    premierComplexe: object = Complexe(3, 2)
    deuxiemeComplexe: object = Complexe(2, 3)
    reel: float = 2.5

    fonction: object = Operation_Complexe.addition_deux_complexes(premierComplexe, deuxiemeComplexe)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object =  Complexe(3 + 2, 2 + 3)
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert  fonction == resultat, "probleme addition_deux_complexes"

    fonction: object = Operation_Complexe.soustraction_deux_complexes(premierComplexe, deuxiemeComplexe)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object = Complexe(3 - 2, 2 - 3)
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert fonction == resultat, "probleme soustraction_deux_complexes"

    fonction: object = Operation_Complexe.multiplication_deux_complexes(premierComplexe, deuxiemeComplexe)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object = Complexe(3*2 - 2*3, 3*2 + 2*3)
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert fonction == resultat, "probleme multiplication_deux_complexes"

    fonction: object = Operation_Complexe.division_deux_complexes(premierComplexe, deuxiemeComplexe)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object = Complexe((3*2 + 2*3) / (2**2 + 3**2), (2 * 2 - 3 * 3) / (2**2 + 3**2))
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert fonction == resultat, "probleme division_deux_complexes"

    fonction: object = Operation_Complexe.addition_complexe_reel(premierComplexe, reel)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object = Complexe(3 + 2.5, 2)
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert fonction == resultat, "probleme addition_complexe_reel"

    fonction: object = Operation_Complexe.soustraction_complexe_reel(premierComplexe, reel)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object = Complexe(3 - 2.5, 2)
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert fonction == resultat, "probleme soustraction_complexe_reel"

    fonction: object = Operation_Complexe.multiplication_complexe_reel(premierComplexe, reel)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object = Complexe(3*2.5, 2*2.5)
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert fonction == resultat, "probleme multiplication_complexe_reel"

    fonction: object = Operation_Complexe.division_complexe_reel(premierComplexe, reel)
    fonction: complex = fonction.obtenir_forme_algebrique()
    resultat: object = Complexe(3/2.5, 2/2.5)
    resultat: complex = resultat.obtenir_forme_algebrique()
    assert fonction == resultat, "probleme multiplication_complexe_reel"
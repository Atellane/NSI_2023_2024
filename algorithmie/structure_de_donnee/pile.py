from liste_chainee import Cellule_Liste, Liste

class Pile():
    def __init__(self: object, premier_element) -> object:
        """premier_element : <T>"""
        premier_element: object = Cellule_Liste(premier_element)
        self.__pile = Liste(premier_element)
    
    def __repr__(self: object) -> str:
        return str(self.__pile)
    
    def ajouter(self: object, element) -> None:
        """element : <T>
        ajoute l'élément au dessus de la pile"""
        element: object = Cellule_Liste(element)
        pile: object = self.__pile
        pile.ajouter(element)
    
    def retirer(self: object) -> None:
        """retire le dernier élément"""
        pile: object = self.__pile
        pile.retirer()
    
    def obtenir_element(self: object):
        """peut renvoyer n'importe quel type en fonction de l'élément"""
        pile: object = self.__pile
        dernier_element = pile.dernier_element()
        return dernier_element.lire_valeur()
    
    def hauteur(self: object) -> int:
        """renvoie la hauteur de la pile"""
        pile: object = self.__pile
        return pile.longueur_liste()
    
    def est_vide(self: object) -> bool:
        hauteur: int = self.hauteur()
        if hauteur != 0:
            return False
        return True

if __name__ == "__main__":
    pile: object = Pile("bonjour,")
    assert pile.obtenir_element() == "bonjour,", "oskour 1"
    pile.ajouter("monde!")
    assert pile.obtenir_element() == "monde!", "oskour 2"
    pile.retirer()
    assert pile.obtenir_element() ==  "bonjour,", "oskour 3"
    assert pile.hauteur() == 1, "oskour 4"
    assert pile.est_vide() == False, "oskour 5"
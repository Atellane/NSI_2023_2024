from liste_chainee import Cellule_Liste, Liste

class Pile():
    def __init__(self: object, premier_element = None) -> object:
        """premier_element : <T>"""
        if premier_element != None:
            premier_element: object = Cellule_Liste(premier_element)
            self.__pile = Liste(premier_element)
        else:
            self.__pile = Liste()
    
    def __repr__(self: object) -> str:
        pile = self.__pile
        repres: str = ""
        lenMaxLigneRepr: int = 0
        for index in range(self.hauteur()):
            repres_temp: str = f"{str(pile.cherche_element_index(index))}\n"
            len_repres_temp: int = len(repres_temp) -1
            repres += repres_temp
            if len_repres_temp > lenMaxLigneRepr:
                lenMaxLigneRepr = len_repres_temp
        repres_temp: list = repres.split("\n")
        repres_temp = repres_temp[:-1]
        repres_temp_2: str = ""
        for element in range(len(repres_temp)):
            nombre_espace: int = lenMaxLigneRepr-len(repres_temp[element])
            repres_temp_2 += "\u2502" + repres_temp[element] + " "*nombre_espace + "\u2502\n"
        repres = repres_temp_2
        repres += "\u2514" + "\u2500"*lenMaxLigneRepr + "\u2518" 
        return repres
    
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
    pile = Pile()
    print(pile)
    pile.ajouter("UwU")
    print(pile)
    pile.retirer()
    pile: object = Pile("bonjour,")
    print(pile)
    assert pile.obtenir_element() == "bonjour,", "oskour 1"
    pile.ajouter("monde!")
    print(pile)
    assert pile.obtenir_element() == "monde!", "oskour 2"
    pile.retirer()
    print(pile)
    assert pile.obtenir_element() ==  "bonjour,", "oskour 3"
    assert pile.hauteur() == 1, "oskour 4"
    assert pile.est_vide() == False, "oskour 5"
    pile.ajouter("monde!")
    print(pile)
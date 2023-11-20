"""Module de mise à disposition de l'objet carte"""
class Carte():
    __valeur: int = None
    __couleur: str =  None
    __figure: str = None
    def __init__(self: object, valeur: str, couleur: str) -> object:
        """prend une valeur (str) allant de 0 à 10 et valet, dame et roi et une couleur (pique, coeur, carreaux, trèfle)"""
        valeur.__Preparer_valeur()
        self.__valeur: int = valeur
        self.__couleur = couleur
        self.__figure = self.__Attribuer_figure(self.__valeur, self.__couleur)

    def __Preparer_valeur(self: object, valeur: str):
        match valeur.lower():
            case "valet":
                valeur = 11
                break
            case "dame":
                valeur = 12
                break
            case "roi":
                valeur = 13
                break
            default:
                int(valeur)
        return valeur
    
    def Obtenir_valeur(self: object) -> str:
        return self.__valeur + "11 -> valet, 12 -> dame, 13 -> roi"
    
    def Obtenir_couleur(self: object) -> str:
        return self.__couleur

    def Obtenir_figure(self: object) -> str:
        return self.__figure

    def Attribuer_valeur(self: object, nouvelleValeur: str) -> None:
        nouvelleValeur = self.__Preparer_valeur(nouvelleValeur)
        self.__valeur = nouvelleValeur


    
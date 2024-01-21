from noeud_arbre import Noeud
from file import File

class Arbre_Binaire():
    def __init__(self: object, racine: object) -> object:
        self.__racine: object = racine
        self.__liste_arbre: list = self.parcour_infixe()

    # TODO rebosser la représentation de l'arbre
    def __repr__(self: object) -> str:
        racine = self.__racine
        if self.sous_arbre_gauche() != None and self.sous_arbre_droite() != None:
            sous_arbre_gauche: object = self.sous_arbre_gauche()
            moitie_longueur_enfant_gauche: int = (len(str(sous_arbre_gauche)) // 2) + 1
            sous_arbre_droite: object = self.sous_arbre_droite()
            moitie_longueur_enfant_droite: int = (len(str(sous_arbre_droite)) // 2) + 1
            longueur_de_ce_noeud: int = len(str(racine.obtenir_valeur()))
            longueur_espace_noeud_flèche: int = len(str(sous_arbre_gauche)) + longueur_de_ce_noeud // 2
            longueur_espace_noeud_parent: int = longueur_espace_noeud_flèche - len(str(racine)) // 2
            return " "*moitie_longueur_enfant_gauche + "\u2199"+ " "*moitie_longueur_enfant_gauche + f"{racine.obtenir_valeur()}" \
            + " "*moitie_longueur_enfant_droite + "\u2198" + " "*moitie_longueur_enfant_droite + f"\n{str(sous_arbre_gauche)}" +  \
            " "*longueur_de_ce_noeud + f"{str(sous_arbre_droite)}"
        else:
            return racine.obtenir_valeur()
    
    def __obtenir_enfant_le_plus_a_gauche(self: object, noeud: object = None) -> object:
        if noeud == None:
            noeud = self.__racine
        while noeud.obtenir_enfant_gauche() != None:
            noeud = noeud.obtenir_enfant_gauche()
        return noeud

    def obtenir_racine(self: object) -> object:
        return self.__racine
    
    def definir_racine(self: object, racine: object) -> object:
        return self.__racine

    def arite(self: object, noeud: object = None) -> int:
        if noeud == None:
            noeud = self.__racine

        if noeud == None:
            return 0

        enfant_gauche: object = noeud.obtenir_enfant_gauche()
        enfant_droite: object = noeud.obtenir_enfant_droite()

        arite_gauche: int = self.arite(enfant_gauche)
        arite_droite: int = self.arite(enfant_droite)

        return max(arite_gauche, arite_droite, 2)  # 2 car c'est un arbre binaire

    def hauteur(self: object, noeud: object = None) -> int:
        if noeud == None:
            noeud = self.__racine

        if noeud == None:
            return 0
        
        enfant_gauche: object = noeud.obtenir_enfant_gauche()
        enfant_droite: object = noeud.obtenir_enfant_droite()

        hauteur_gauche: int = self.hauteur(noeud.obtenir_enfant_gauche())
        hauteur_droite: int = self.hauteur(noeud.obtenir_enfant_droite())

        return max(hauteur_gauche, hauteur_droite) + 1  # car  on y ajoute la racine
    
    def sous_arbre_gauche(self: object) -> object:
        racine: object = self.__racine
        if racine.obtenir_enfant_gauche() != None:
            return Arbre_Binaire(racine.obtenir_enfant_gauche())
        else:
            return None
    
    def sous_arbre_droite(self: object) -> object:
        racine: object = self.__racine
        if racine.obtenir_enfant_droite() != None:
            return Arbre_Binaire(racine.obtenir_enfant_droite())
        else:
            return None
    
    def parcour_prefixe(self: object, noeud: object = None) -> list:
        if noeud == None:
            noeud = self.__racine
        if noeud.obtenir_enfant_droite() == None and noeud.obtenir_enfant_gauche() == None:
            return [noeud]
        else:
            cellules_arbres: list = []
            cellules_arbres.append(noeud)
            sous_arbre_gauche: list = self.parcour_prefixe(noeud.obtenir_enfant_gauche())
            sous_arbre_droite: list = self.parcour_prefixe(noeud.obtenir_enfant_droite())
            cellules_arbres.append(sous_arbre_gauche)
            cellules_arbres.append(sous_arbre_droite)
            return cellules_arbres

    def parcour_infixe(self: object, noeud: object = None) -> list:
        if noeud == None:
            noeud = self.__racine

        if noeud.obtenir_enfant_gauche() == None and noeud.obtenir_enfant_droite() == None:
            return [noeud]
        else:
            cellules_arbres: list = []
            sous_arbre_gauche: list = self.parcour_infixe(noeud.obtenir_enfant_gauche())
            cellules_arbres.append(sous_arbre_gauche)
            cellules_arbres.append(noeud)
            sous_arbre_droite: list = self.parcour_infixe(noeud.obtenir_enfant_droite())
            cellules_arbres.append(sous_arbre_droite)

            return cellules_arbres

    def parcour_suffixe(self: object, noeud: object = None) -> list:
        if noeud == None:
            noeud = self.__racine

        if noeud.obtenir_enfant_gauche() == None and noeud.obtenir_enfant_droite() == None:
            return [noeud]
        else:
            cellules_arbres: list = []
            sous_arbre_gauche: list = self.parcour_suffixe(noeud.obtenir_enfant_gauche())
            cellules_arbres.append(sous_arbre_gauche)
            sous_arbre_droite: list = self.parcour_suffixe(noeud.obtenir_enfant_droite())
            cellules_arbres.append(sous_arbre_droite)
            cellules_arbres.append(noeud)

            return cellules_arbres

    def parcour_largeur(self: object) -> list:
        if self.__racine == None:
            return []

        ma_file: object = File()
        ma_file.ajouter(self.__racine)
        result: list = []

        while not ma_file.est_vide():
            current_node = ma_file.enlever()
            result.append(current_node)

            if current_node.obtenir_enfant_gauche() != None:
                ma_file.ajouter(current_node.obtenir_enfant_gauche())

            if current_node.obtenir_enfant_droite() != None:
                ma_file.ajouter(current_node.obtenir_enfant_droite())

        return result

if __name__ == "__main__":
    noeud_arbre: object = Noeud("A")
    noeud_enfant_gauche: object = Noeud("B")
    noeud_enfant_droite: object = Noeud("E")
    noeud_arbre.def_enfant_gauche(noeud_enfant_gauche)
    noeud_arbre.def_enfant_droite(noeud_enfant_droite)
    noeud_enfant_gauche_d_enfant_gauche: object = Noeud("C")
    noeud_enfant_droite_d_enfant_gauche: object = Noeud("D")
    noeud_enfant_gauche_d_enfant_droite: object = Noeud("F")
    noeud_enfant_droite_d_enfant_droite: object = Noeud("G")
    noeud_enfant_gauche.def_enfant_gauche(noeud_enfant_gauche_d_enfant_gauche)
    noeud_enfant_gauche.def_enfant_droite(noeud_enfant_droite_d_enfant_gauche)
    noeud_enfant_droite.def_enfant_gauche(noeud_enfant_gauche_d_enfant_droite)
    noeud_enfant_droite.def_enfant_droite(noeud_enfant_droite_d_enfant_droite)
    arbre: object = Arbre_Binaire(noeud_arbre)
    print(arbre.parcour_prefixe())
    noeud_arbre.def_enfant_droite(None)
    noeud_arbre.def_enfant_gauche(None)
    print(arbre.parcour_prefixe())
    noeud_arbre.def_enfant_droite(noeud_enfant_droite)
    noeud_arbre.def_enfant_gauche(noeud_enfant_gauche)
    print(arbre.parcour_prefixe())
    print(arbre.parcour_infixe())
    print(arbre.parcour_suffixe())
    print(arbre.parcour_largeur())
    print(arbre)
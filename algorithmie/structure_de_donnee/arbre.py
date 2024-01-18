from noeud_arbre import Noeud
from trouver_meme_sous_tableau import trouver_meme_dans_sous_tableau

class Arbre_Binaire():
    def __init__(self: object, racine: object) -> object:
        self.__racine: object = racine
        self.__liste_arbre: list = self.parcour_prefixe()
    
    def obtenir_racine(self: object) -> object:
        return self.__racine
    
    def definir_racine(self: object, racine: object) -> object:
        return self.__racine
    
    def parcour_prefixe(self: object, noeud: object = None) -> list:
        if noeud == None:
            noeud = self.__racine
        if noeud.obtenir_enfant_droite() == None and noeud.obtenir_enfant_gauche() == None:
            return [noeud]
        else:
            cellules_arbres: list = []
            cellules_arbres.append(noeud)
            cellules_arbres.append([])
            sous_arbre_gauche: list = self.parcour_prefixe(noeud.obtenir_enfant_gauche())
            sous_arbre_droite: list = self.parcour_prefixe(noeud.obtenir_enfant_droite())
            cellules_arbres[1].append(sous_arbre_gauche)
            cellules_arbres[1].append(sous_arbre_droite)
            return cellules_arbres

    # TODO ne fonctionne pas
    def parcour_infixe(self: object, noeud: object = None, tableau_de_ce_qu_on_a_deja: list = []) -> list:
        if noeud == None:
            noeud = self.__racine
        if not trouver_meme_dans_sous_tableau(tableau_de_ce_qu_on_a_deja, noeud.obtenir_enfant_gauche()):
            while noeud.obtenir_enfant_gauche() != None:
                noeud = noeud.obtenir_enfant_gauche()
        if noeud.obtenir_pere() == None:
            tableau_de_ce_qu_on_a_deja.append(noeud)
            return [noeud]
        else:
            tableau: list = []
            if not trouver_meme_dans_sous_tableau(tableau_de_ce_qu_on_a_deja, noeud):
                tableau_de_ce_qu_on_a_deja.append(noeud)
                tableau.append(noeud)
            if noeud.obtenir_enfant_droite() == None:
                tableau.append(self.parcour_infixe(noeud.obtenir_pere()))
            elif trouver_meme_dans_sous_tableau(tableau_de_ce_qu_on_a_deja, noeud.obtenir_enfant_droite()):
                tableau.append(self.parcour_infixe(noeud.obtenir_pere(), tableau_de_ce_qu_on_a_deja))
            else:
                tableau.append(self.parcour_infixe(noeud.obtenir_enfant_droite(), tableau_de_ce_qu_on_a_deja))
            return tableau

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
    print(arbre.parcour_prefixe()[1][0][1][1])
    print(arbre.parcour_infixe())
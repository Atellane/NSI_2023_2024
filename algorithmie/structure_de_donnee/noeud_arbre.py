class Noeud():
    __enfant_gauche: object = None
    __enfant_droite: object = None
    __pere: object = None
    
    def __init__(self: object, valeur: any = None) -> object:
        self.__valeur = valeur

    # ⇩ : U+21E9
    # ↘ : U+2198
    # ↙ : U+2199

    # TODO finir de m'occuper la présentation des espaces, sauvegarder cette représentation pour l'utiliser pour l'arbre, l'adapter à l'arbre
    def __repr__(self: object) -> str:
        return self.obtenir_valeur()
        # TODO prendre ce code et le réutiliser pour faire la représentation de l'arbre
        # if self.__enfant_gauche != None and self.__enfant_droite != None and self.__pere != None:
        #     enfant_gauche: object = self.__enfant_gauche
        #     moitie_longueur_enfant_gauche: int = len(str(enfant_gauche.obtenir_valeur())) // 2
        #     enfant_droite: object = self.__enfant_droite
        #     moitie_longueur_enfant_droite: int = len(str(enfant_droite.obtenir_valeur())) // 2
        #     longueur_de_ce_noeud: int = len(str(self.obtenir_valeur()))
        #     pere: object = self.__pere
        #     longueur_espace_noeud_flèche: int = len(str(enfant_gauche.obtenir_valeur())) + longueur_de_ce_noeud // 2
        #     longueur_espace_noeud_parent: int = longueur_espace_noeud_flèche - len(str(pere)) // 2
        #     return " "*longueur_espace_noeud_parent + f"{pere.obtenir_valeur()}\n" + " "*longueur_espace_noeud_flèche + "\u21e9\n" + " "*moitie_longueur_enfant_gauche + "\u2199"+ " "*moitie_longueur_enfant_gauche + f"{self.obtenir_valeur()}" + " "*moitie_longueur_enfant_droite + "\u2198" + " "*moitie_longueur_enfant_droite + f"\n{enfant_gauche.obtenir_valeur()}" + " "*longueur_de_ce_noeud + f"{enfant_droite.obtenir_valeur()}"
        # elif self.__enfant_gauche != None and self.__enfant_droite != None:
        #     enfant_gauche: object = self.__enfant_gauche
        #     enfant_droite: object = self.__enfant_droite
        #     return f"\u2199{self.obtenir_valeur()}\u2198\n{enfant_gauche.obtenir_valeur()}\t{enfant_droite.obtenir_valeur()}"
        # elif self.__enfant_gauche != None and self.__pere != None:
        #     enfant_gauche: object = self.__enfant_gauche
        #     pere: object = self.__pere
        #     return f"{pere.obtenir_valeur()}\n\u21e9\n{self.obtenir_valeur()}\n\u21e9\n{enfant_gauche.obtenir_valeur()}"
        # elif self.__enfant_droite != None and self.__pere != None:
        #     enfant_droite: object = self.__enfant_droite
        #     pere: object = self.__pere
        #     return f"{pere.obtenir_valeur()}\n\u21e9\n{self.obtenir_valeur()}\n\u21e9\n{enfant_droite.obtenir_valeur()}"
        # elif self.__enfant_gauche != None:
        #     enfant_gauche: object = self.__enfant_gauche
        #     return f"{self.obtenir_valeur()}\n\u21e9\n{enfant_gauche.obtenir_valeur()}"
        # elif self.__enfant_droite != None:
        #     enfant_droite: object = self.__enfant_droite
        #     return f"{self.obtenir_valeur()}\n\u21e9\n{enfant_droite.obtenir_valeur()}"
        # elif self.__pere != None:
        #     pere: object = self.__pere
        #     return f"{pere.obtenir_valeur()}\n\u21e9\n{self.obtenir_valeur()}"
        # else:
        #     return self.obtenir_valeur()


    def def_valeur(self: object, valeur: any) -> None:
        self.__valeur = valeur

    def def_enfant_gauche(self: object, enfant_gauche: object) -> None:
        if enfant_gauche != None:
            enfant_gauche.def_pere(self)
        self.__enfant_gauche = enfant_gauche
    
    def def_enfant_droite(self: object, enfant_droite: object) -> None:
        if enfant_droite != None:
            enfant_droite.def_pere(self)
        self.__enfant_droite = enfant_droite
    
    def def_pere(self: object, pere: object) -> None:
        self.__pere = pere
    
    def obtenir_valeur(self: object) -> any:
        return self.__valeur

    def obtenir_enfant_gauche(self: object) -> object:
        return self.__enfant_gauche

    def obtenir_enfant_droite(self: object) -> object:
        return self.__enfant_droite

    def obtenir_pere(self: object) -> object:
        return self.__pere

if __name__ == "__main__":
    noeud: object = Noeud("UwU")
    noeud_parent: object = Noeud("Parent_UwU")
    noeud_enfant_gauche: object = Noeud("enfant_gauche_UwU")
    noeud_enfant_droite: object = Noeud("enfant_droite_UwU")
    noeud.def_pere(noeud_parent)
    noeud.def_enfant_gauche(noeud_enfant_gauche)
    noeud.def_enfant_droite(noeud_enfant_droite)
    noeud.def_enfant_gauche(None)
    noeud.def_pere(None)
    noeud.def_enfant_droite(None)
    noeud.def_enfant_gauche(noeud_enfant_gauche)
    noeud.def_enfant_droite(noeud_enfant_droite)
    noeud.def_pere(noeud_parent)
    print(noeud)
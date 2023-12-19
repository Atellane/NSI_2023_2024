from liste_chainee import Liste, Cellule_Liste
from liste_doublement_chainee import Liste_Doublement_Chainee, Cellule_Liste_Doublement_Chainee

def concatene_liste_chainee(liste1: object, liste2: object) -> object:
    """concatene les deux listes (chainée, chainée et doublement chainée et doublement chainée) et retourne la concaténation des deux (liste chainee si deux listes chainee, sinon liste doublement chainee)"""
    if isinstance(liste1, Liste) and isinstance(liste2, Liste):
        for i in range(liste2.longueur_liste()):
            elementActuel = liste2.cherche_element_index(i)
            liste1.ajouter(elementActuel)
        return liste1
    elif isinstance(liste1, Liste_Doublement_Chainee) and isinstance(liste2, Liste):
        for i in range(liste2.longueur_liste()):
            elementActuel = liste2.cherche_element_index(i)
            elementActuel = Cellule_Liste_Doublement_Chainee(elementActuel.lire_valeur())
            liste1.ajouter(elementActuel)
        return liste1
    else:
        cellules: list = []
        for i in range(liste1.longueur_liste()):
            elementActuel = liste1.cherche_element_index(i)
            elementActuel = Cellule_Liste_Doublement_Chainee(elementActuel.lire_valeur())
            cellules.append(elementActuel)
        liste1: object = Liste_Doublement_Chainee(cellules[0])
        for i in cellules:
            liste1.ajouter(i)
        for i in range(liste2.longueur_liste()):
            elementActuel = liste2.cherche_element_index(i)
            elementActuel = Cellule_Liste_Doublement_Chainee(elementActuel.lire_valeur())
            liste1.ajouter(elementActuel)
        return liste1

if __name__ == "__main__":
    c1 = Cellule_Liste(1)
    c2 = Cellule_Liste(2)
    c3 = Cellule_Liste(1)
    lst = Liste(c1)
    lst.ajouter(c2)
    lst.ajouter(c3)
    c4 = Cellule_Liste(1)
    c5 = Cellule_Liste(2)
    c6 = Cellule_Liste(1)
    lst2 = Liste(c4)
    lst2.ajouter(c5)
    lst2.ajouter(c6)
    lst_combi = Liste(c1)
    lst_combi.ajouter(c2)
    lst_combi.ajouter(c3)
    lst_combi.ajouter(c4)
    lst_combi.ajouter(c5)
    lst_combi.ajouter(c6)
    assert concatene_liste_chainee(lst, lst2).premier_element() == lst_combi.premier_element(), "ne réussie pas à concaténer 2 liste chainée"
    assert concatene_liste_chainee(lst, lst2).dernier_element() == lst_combi.dernier_element(), "ne réussie pas à concaténer 2 liste chainée"
    c4 = Cellule_Liste_Doublement_Chainee(1)
    c5 = Cellule_Liste_Doublement_Chainee(2)
    c6 = Cellule_Liste_Doublement_Chainee(1)
    lst2 = Liste_Doublement_Chainee(c4)
    lst2.ajouter(c5)
    lst2.ajouter(c6)
    c1 = Cellule_Liste_Doublement_Chainee(1)
    c2 = Cellule_Liste_Doublement_Chainee(2)
    c3 = Cellule_Liste_Doublement_Chainee(1)
    lst_combi = Liste(c1)
    lst_combi.ajouter(c2)
    lst_combi.ajouter(c3)
    lst_combi.ajouter(c4)
    lst_combi.ajouter(c5)
    lst_combi.ajouter(c6)
    premier_element_lst = concatene_liste_chainee(lst, lst2).premier_element()
    premier_element_lst_combi = lst_combi.premier_element()
    assert premier_element_lst.lire_valeur() == premier_element_lst_combi.lire_valeur(), "ne réussie pas à concaténer 2 liste dont une chainée et l'autre doublement chainée"
    dernier_element_lst = concatene_liste_chainee(lst, lst2).dernier_element()
    dernier_element_lst_combi = lst_combi.dernier_element()
    assert dernier_element_lst.lire_valeur() == dernier_element_lst_combi.lire_valeur(), "ne réussie pas à concaténer 2 liste dont une chainée et l'autre doublement chainée"
    premier_element_lst = concatene_liste_chainee(lst2, lst).premier_element()
    assert premier_element_lst.lire_valeur() == dernier_element_lst_combi.lire_valeur(), "ne réussie pas à concaténer 2 liste dont une doublement chainée et l'autre chainée"
    dernier_element_lst = concatene_liste_chainee(lst2, lst).dernier_element()
    assert dernier_element_lst.lire_valeur() == premier_element_lst_combi.lire_valeur(), "ne réussie pas à concaténer 2 liste dont une doublement chainée et l'autre chainée"
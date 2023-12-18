from liste_chainee import Liste, Cellule_Liste
from liste_doublement_chainee import Liste_Doublement_Chainee, Cellule_Liste_Doublement_Chainee

def supprime_premiere_occurence(liste: object, valeur: int) -> bool:
    """supprimme la première occurence d'une valeur dans une liste chainée ou doublement chainée"""
    for i in range(liste.longueur_liste()):
        elementActuel: object = liste.cherche_element_index(i)
        if elementActuel.lire_valeur() == valeur:
            liste.retirer(i)
            return True
    return False

if __name__ == "__main__":
    c1 = Cellule_Liste(1)
    c2 = Cellule_Liste(2)
    c3 = Cellule_Liste(1)
    lst = Liste(c1)
    lst.ajouter(c2)
    lst.ajouter(c3)
    assert supprime_premiere_occurence(lst, 1), "ça a pas supprimer la première occurence du 1 d'une liste chainée"
    assert supprime_premiere_occurence(lst, 2), "ça a pas supprimer la première occurence du 2 d'une liste chainée"
    c1 = Cellule_Liste_Doublement_Chainee(1)
    c2 = Cellule_Liste_Doublement_Chainee(2)
    c3 = Cellule_Liste_Doublement_Chainee(1)
    lst = Liste_Doublement_Chainee(c1)
    lst.ajouter(c2)
    lst.ajouter(c3)
    assert supprime_premiere_occurence(lst, 1), "ça a pas supprimer la première occurence du 1 d'une liste doublement chainée"
    assert supprime_premiere_occurence(lst, 2), "ça a pas supprimer la première occurence du 2 d'une liste doublement chainée"
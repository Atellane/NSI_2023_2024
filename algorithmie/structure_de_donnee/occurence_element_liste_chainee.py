from liste_chainee import Liste, Cellule_Liste
from liste_doublement_chainee import Liste_Doublement_Chainee, Cellule_Liste_Doublement_Chainee

def occurence_valeur_liste_chainee(liste: object, valeur) -> int:
    """valeur peut être de n'importe quel type
    renvoie le nombre d'occurence d'un élément d'une liste chainée ou doublement chainée"""
    occurence: int = 0
    for i in range(liste.longueur_liste()):
        elementActuel: object = liste.cherche_element_index(i)
        if elementActuel.lire_valeur() == valeur:
            occurence += 1
    return occurence

if __name__ == "__main__":
    c1 = Cellule_Liste(1)
    c2 = Cellule_Liste(2)
    c3 = Cellule_Liste(1)
    lst = Liste(c1)
    lst.ajouter(c2)
    lst.ajouter(c3)
    assert occurence_valeur_liste_chainee(lst, 1) == 2, "problème comptage occurence 1 liste chainée"
    assert occurence_valeur_liste_chainee(lst, 2) == 1, "problème comptage occurence 2 liste chainée"
    c1 = Cellule_Liste_Doublement_Chainee(1)
    c2 = Cellule_Liste_Doublement_Chainee(2)
    c3 = Cellule_Liste_Doublement_Chainee(1)
    lst = Liste_Doublement_Chainee(c1)
    lst.ajouter(c2)
    lst.ajouter(c3)
    assert occurence_valeur_liste_chainee(lst, 1) == 2, "problème comptage occurence 1 liste doublement chainée"
    assert occurence_valeur_liste_chainee(lst, 2) == 1, "problème comptage occurence 2 liste doublement chainée"
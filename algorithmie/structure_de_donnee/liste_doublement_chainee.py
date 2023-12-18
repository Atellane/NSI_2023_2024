from math import inf

class Cellule_Liste_Doublement_Chainee():
    """classe basique de cellule de liste doublement chainée"""
    __valeur = None
    __suivant: hex = 0x0
    __precedent: hex = 0x0

    def __init__(self: object, valeur) -> object: # valeur peut être de n'importe quel type
        self.__valeur = valeur

    def attr_suivant(self: object, suivant: object) -> hex:
        self.__suivant = hex(id(suivant))
    
    def attr_precedent(self: object, precedent: object) -> hex:
        self.__precedent = hex(id(precedent))

    def lire_suivant(self: object) -> object:
        return self.__suivant
    
    def lire_precedent(self: object) -> object:
        return self.__precedent

    def lire_valeur(self: object): #  peut retourner n'importe quel type
        return self.__valeur
    
    def __repr__(self: object) -> str:
        return "["+str(self.__valeur)+"]->"+str(self.__suivant)

class Liste_Doublement_Chainee():
    """Classe basique de liste chainée"""
    __debut: hex = 0x0
    __fin: hex = 0x0
    __cellules: list = []

    def __init__(self: object, c: object) -> object:
        self.__debut = hex(id(c))
        self.__fin = self.__debut
        cellules = self.__cellules
        cellules.append(c)

    def __trouver_cellule(self: object, adresse_c: hex) -> object:
        for i in range(len(self.__cellules)):
            celluleActuelle: object = self.__cellules[i]
            if hex(id(celluleActuelle)) == adresse_c:
                return i
        
    def __repr__(self: object) -> str:
        return str(self.__cellules)

    def ajouter(self: object, c: object, position: int = inf) -> None:
        """Ajoute la cellule c à la place position (compter à partir à 0) et à la fin si position >= nombre de cellule ou par défaut"""
        listeDesCellules: list = self.__cellules
        if position < len(listeDesCellules) - 1:
            cellulePrecedente = listeDesCellules[position-1]
            addresseCelluleSuivante: hex = cellulePrecedente.lire_suivant()
            cellulePrecedente.attr_suivant(hex(id(c)))
            c.attr_suivant(addresseCelluleSuivante)
            listeDesCellules.insert(position, c)
        else:
            cellulePrecedente = listeDesCellules[-1]
            cellulePrecedente.attr_suivant(hex(id(c)))
            listeDesCellules.append(c)
    
    def retirer(self: object, position: int = inf) -> None:
        """Retire la cellule c à la place position (compter à partir à 0) et à la fin si position >= nombre de cellule ou par défaut"""
        listeDesCellules: list = self.__cellules
        if position < len(listeDesCellules) - 1:
            cellulePrecedente: object = listeDesCellules[position-1]
            addresseCelluleSuivante: hex = hex(id(listeDesCellules[position+1]))
            cellulePrecedente.attr_suivant(addresseCelluleSuivante)
            listeDesCellules.pop(position)
        else:
            cellulePrecedente: object = listeDesCellules[position-1]
            cellulePrecedente.attr_suivant(None)
    
    def est_vide(self: object) -> bool:
        """Renvoie True si la liste est vide, sinon, renvoie False"""
        if len(self.__cellules) == 0:
            return True
        
        return False
    
    def longueur_liste(self: object) -> int:
        """Renvoie la taille de la liste"""
        return len(self.__cellules)
    
    def premier_element(self: object) -> object:
        """Renvoie le 1er élément de la liste"""
        return self.__cellules[0]
    
    def dernier_element(self: object) -> object:
        """Renvoie le dernier élément de la liste"""
        return self.__cellules[-1]
    
    def prochain_element(self: object, c: object) -> object:
        """Renvoie la cellule suivant la cellule donnée en entrée"""
        emplacementElement = self.__trouver_cellule(hex(id(c)))
        return self.__cellules[emplacementElement+1]
    
    def element_precedent(self: object, c: object) -> object:
        """Renvoie la cellule precedent la cellule donnée en entrée"""
        emplacementElement = self.__trouver_cellule(hex(id(c)))
        return self.__cellules[emplacementElement-1]

    def cherche_element(self: object, valeur) -> int:
        """valeur <T> (n'importe quel type)
        Renvoie position 1er élément de la liste aillant pour valeur la valeur donnée en entrer, retourne -1 si l'élément n'as pas été trouvé"""
        for i in range(len(self.__cellules)):
            celluleActuelle = self.__cellules[i]
            if celluleActuelle.lire_valeur() == valeur:
                return i
        return -1

if __name__=="__main__" :
    c1 = Cellule_Liste_Doublement_Chainee(10)
    c2 = Cellule_Liste_Doublement_Chainee("A")
    c3 = Cellule_Liste_Doublement_Chainee(3.0)
    print(c1, c2, c3)
    print(hex(id(c2)))
    lst = Liste_Doublement_Chainee(c1)
    lst.ajouter(c2)
    print(lst)
    lst.ajouter(c3)
    print(lst)
    c4 = Cellule_Liste_Doublement_Chainee(5)
    lst.ajouter(c4,0)
    print(lst)
    lst.retirer(0)
    print(lst)
    assert lst.est_vide() == False, "ça a pas renvoyé false :/"
    assert lst.longueur_liste() == 3, "problème récupération longueur de la liste"
    assert lst.premier_element() == c1,"problème fonction récup 1er élément"
    assert lst.dernier_element() == c3, "probmème récupn dernier élément"
    assert lst.prochain_element(c1) == c2, "problème récupération élément suivant."
    assert lst.cherche_element("A") == 1, "problème récupération position éléments"
    assert lst.cherche_element(";)") == -1, "ça détecte quelque chose qui n'existe pas oskour"
    assert lst.element_precedent(c2) == c1, "problème récupération élément précédent."
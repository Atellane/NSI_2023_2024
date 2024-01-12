from math import inf

class Cellule_Liste():
    """classe basique de cellule de liste chainée"""
    __valeur = None
    __suivant = 0

    def __init__(self: object, valeur) -> object: # valeur peut être de n'importe quel type
        self.__valeur = valeur

    def attr_suivant(self: object, suivant) -> None:
        if isinstance(suivant, Cellule_Liste) == False:
            self.__suivant = 0
        else:
            self.__suivant = hex(id(suivant))

    def lire_suivant(self: object): # peut retourner n'importe quel type
        return self.__suivant

    def lire_valeur(self: object): #  peut retourner n'importe quel type
        return self.__valeur
    
    def __repr__(self: object) -> str:
        return "["+str(self.__valeur)+"]->"+str(self.__suivant)

class Liste():
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
            celluleSuivante: object = listeDesCellules[position]
            cellulePrecedente.attr_suivant(c)
            c.attr_suivant(celluleSuivante)
            listeDesCellules.insert(position, c)
        else:
            cellulePrecedente = listeDesCellules[-1]
            cellulePrecedente.attr_suivant(c)
            listeDesCellules.append(c)
    
    def retirer(self: object, position: int = inf) -> None:
        """Retire la cellule c à la place position (compter à partir à 0) et à la fin si position >= nombre de cellule ou par défaut"""
        listeDesCellules: list = self.__cellules
        if position < len(listeDesCellules) - 1:
            cellulePrecedente: object = listeDesCellules[position-1]
            celluleSuivante: object = listeDesCellules[position+1]
            cellulePrecedente.attr_suivant(celluleSuivante)
            listeDesCellules.pop(position)
        else:
            cellulePrecedente: object = listeDesCellules[-2]
            cellulePrecedente.attr_suivant(None)
            listeDesCellules.pop(-1)
    
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

    def cherche_element_valeur(self: object, valeur) -> int:
        """valeur <T> (n'importe quel type)
        Renvoie position 1er élément de la liste aillant pour valeur la valeur donnée en entrer, retourne -1 si l'élément n'as pas été trouvé"""
        for i in range(len(self.__cellules)):
            celluleActuelle = self.__cellules[i]
            if celluleActuelle.lire_valeur() == valeur:
                return i
        return -1
    
    def cherche_element_index(self: object, index: int) -> object:
        """Renvoie l'élément de la liste d'index 'index'"""
        try:
            return self.__cellules[index]
        except IndexError:
            print("l'index donné n'existe pas")

if __name__=="__main__" :
    c1 = Cellule_Liste(10)
    c2 = Cellule_Liste("A")
    c3 = Cellule_Liste(3.0)
    print(c1, c2, c3)
    print(hex(id(c2)))
    lst = Liste(c1)
    lst.ajouter(c2)
    print(lst)
    lst.ajouter(c3)
    print(lst)
    c4 = Cellule_Liste(5)
    lst.ajouter(c4,0)
    print(lst)
    lst.retirer(0)
    print(lst)
    assert lst.est_vide() == False, "ça a pas renvoyé false :/"
    assert lst.longueur_liste() == 3, "problème récupération longueur de la liste"
    assert lst.premier_element() == c1,"problème fonction récup 1er élément"
    assert lst.dernier_element() == c3, "probmème récupn dernier élément"
    assert lst.prochain_element(c1) == c2, "problème récupération élément suivant."
    assert lst.cherche_element_valeur("A") == 1, "problème récupération position éléments"
    assert lst.cherche_element_valeur(";)") == -1, "ça détecte quelque chose qui n'existe pas oskour"
    assert lst.cherche_element_index(1) == c2, "ne trouve pas l'élément en fonction de l'index"
    assert lst.cherche_element_index(1000) == None, "trouve un élément qui n'existe pas"
from arbre_correction import Arbre, Noeud

class ABR(Arbre):
    """Une classe arbre binaire de recherche basique"""
    def __init__(self: object, tab: list) -> object:
        """Crée un arbre binaire de recherche dont les noeuds sont contenus dans tab"""
        super().__init__(Noeud(tab.pop(0)))
        self.__racine: Noeud=self._Arbre__racine
        self.inserer_element(tab)

    def min(self: object) -> any:
        """Renvoie le plus petit élément de l'arbre"""
        r: Noeud = self.__racine
        while r.Lire_fg() != None :
            r = r.Lire_fg()
        return r.Lire_valeur()

    def max(self: object) -> any:
        """Renvoie le plus grand élément de l'arbre"""
        r = self.__racine
        while r.Lire_fd() != None :
            r = r.Lire_fd()
        return r.Lire_valeur()
    
    def tri(self: object) -> str:
        """Trie les données de l'ABR"""
        return self.infixe()
    
    def inserer_element(self: object, tab: list) -> None:
        """Insére la liste de noeud donnée dans l'arbre"""
        while len(tab)>0 :
            r = self.__racine
            cherche = True
            n = Noeud(tab.pop(0))
            while cherche :
                if n.Lire_valeur() < r.Lire_valeur() :
                    if r.Lire_fg() == None :
                        r.Attr_fg(n)
                        n.Attr_pere(r)
                        cherche = False
                    else :
                        r = r.Lire_fg()
                else:
                    if r.Lire_fd() == None :
                        r.Attr_fd(n)
                        n.Attr_pere(r)
                        cherche = False
                    else :
                        r = r.Lire_fd()
    
    def retirer_element(self: object, tab: list) -> None:
        """Retire la liste de noeud donnée de l'arbre"""
        sauvegarde: list = tab
        resultats_recherche: list[bool] = []
        while len(tab)>0 :
            r = self.__racine
            cherche = True
            n = Noeud(tab.pop(0))
            while cherche :
                if n == r :
                    r.Attr_fg(None)
                    r.Attr_fd(None)
                    pere: Noeud = r.Lire_pere()
                    if pere.Lire_fg() == r:
                        pere.Attr_fg(None)
                    else:
                        pere.Attr_fd(None)
                    r.Attr_pere(None)
                    del r
                    cherche = False
                elif n.Lire_valeur() < r.Lire_valeur():
                    r = r.Lire_fg()
                    if r == None:
                        break
                else:
                    r = r.Lire_fd()
                    if r == None:
                        break
            resultats_recherche.append(not cherche)
        index_elements_non_trouve: list[int] = []
        elements_non_trouve: list = []
        if False in resultats_recherche:
            for index in range(len(resultats_recherche)):
                if not resultats_recherche[index]:
                    index_elements_non_trouve.append(index)
            for index in index_elements_non_trouve:
                elements_non_trouve.append(sauvegarde[index])
        return elements_non_trouve
    
    # les méthodes du prof
    def sous_arbre(self, r : noeud):
        """Noeud->ABR
           Renvoie le sous-ABR issu du noeud fourni"""
        elements = super().sous_arbre(r).prefixe()
        return ABR(elements.split(" "))
    
    def inserer(self, valeur) :
        """Type->None
           Insère la valeur dans l'ABR"""
        r = self.__racine
        cherche = True
        n = noeud(valeur)
        while cherche :
            if n.Lire_valeur() < r.Lire_valeur() :
                if r.Lire_fg() == None :
                    r.Attr_fg(n)
                    n.Attr_pere(r)
                    cherche = False
                else :
                    r = r.Lire_fg()
            else:
                if r.Lire_fd() == None :
                    r.Attr_fd(n)
                    n.Attr_pere(r)
                    cherche = False
                else :
                    r = r.Lire_fd()

    def supprimer(self, valeur) :
        """int->None
           Supprime la valeur de l'ABR si elle est présente"""
        existe, n = self.recherche(valeur)
        if existe :
            p = n.Lire_pere()
            elements = super().sous_arbre(n).prefixe().split(" ")
            for i in range(len(elements)) :
                elements[i] = int(elements[i])
            elements.remove(valeur)
            if p!= None:
                if n == p.Lire_fg() :
                    p.Attr_fg(None)
                else :
                    p.Attr_fd(None)
            else :
                self.__racine = noeud(elements.pop(len(elements)//2))
                self._arbre__racine = self.__racine
            for e in elements :
                self.inserer(e)

    def recherche(self, valeur) :
        """int->boolean*Noeud
           retourne vrai si la valeur est présente dans l'ABR"""
        r = self.__racine
        trouve = False
        cherche = True
        while cherche :
            if valeur < int(r.Lire_valeur()) :
                if r.Lire_fg() == None :
                    cherche = False
                else :
                    r = r.Lire_fg()
            elif valeur > int(r.Lire_valeur()) :
                if r.Lire_fd() == None :
                    cherche = False
                else :
                    r = r.Lire_fd()
            else : 
                trouve = True
                cherche = False
        if not trouve :
            r = None
        return trouve, r
            

if __name__ == "__main__":
    print([10,2,5,12,15,20,1,3,7,25])
    a = ABR([10,2,5,12,15,20,1,3,7,25])
    print(a)
    print(a.tri())
    print(a.min())
    print(a.max())
    a.repr_graphique()
    a.inserer_element([100,1000])
    a.repr_graphique()
    a.retirer_element([100, 1000])
    a.repr_graphique()
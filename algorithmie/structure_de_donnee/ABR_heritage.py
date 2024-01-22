from arbre_fini import arbre, noeud

class ABR(Arbre):
    """ Une classe arbre binaire de recherche basique"""
    def __init__(self, tab):
        """noeud->arbre
            Crée un arbre binaire de recherche dont les noeuds sont contenus dans tab"""
        #self.__racine = noeud(tab.pop(0))
        super().__init__(noeud(tab.pop(0)))
        self.__racine=self._Arbre__racine
        while len(tab)>0 :
            r = self.__racine
            cherche = True
            n = noeud(tab.pop(0))
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

    def tri(self):
        """None->String
            trie les données de l'ABR"""
        return self.infixe()

    def min(self):
        r = self.__racine
        while r.Lire_fg() != None :
            r = r.Lire_fg()
        return r.Lire_valeur()

    def max(self):
        r = self.__racine
        while r.Lire_fd() != None :
            r = r.Lire_fd()
        return r.Lire_valeur()

if __name__ == "__main__":
    print([10,2,5,12,15,20,1,3,7,25])
    a = ABR([10,2,5,12,15,20,1,3,7,25])
    print(a)
    print(a.tri())
    print(a.min())
    print(a.max())
    a.repr_graphique()
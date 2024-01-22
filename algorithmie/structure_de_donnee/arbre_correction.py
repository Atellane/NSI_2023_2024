import pydot

class noeud:
    """Une classe définissant le noeud d'un arbre"""

    def __init__(self, valeur):
        """Type->noeud
            Constructeur de la classe noeud. renvoie un objet noeud qui contient valeur"""
        self.__pere = None
        self.__fg = None
        self.__fd = None
        self.__valeur = valeur

    def __repr__(self):
        """None->String
            Surcharge de la fonction appelée par print pour l'affichage"""
        if self.__pere == None :
            pere = "Aucun"
        else:
            pere = self.__pere.Lire_valeur()
        if self.__fg == None :
            fg = "Aucun"
        else:
            fg = self.__fg.Lire_valeur()
        if self.__fd == None :
            fd = "Aucun"
        else:
            fd = self.__fd.Lire_valeur()    
        return "  "+str(pere)+"\n"+str(fg)+"-"+str(self.__valeur)+"-"+str(fd)

    #Attribuer une valeur à un attribut
    def Attr_pere(self, pere):
        """noeud->None
            Attribut le père pere au noeud appelant"""
        self.__pere = pere

    def Attr_fg(self, fg):
        """noeud->None
            Attribut le fils gauche fg au noeud appelant"""
        self.__fg = fg

    def Attr_fd(self, fd):
        """noeud->None
            Attribut le fils droit fd au noeud appelant"""
        self.__fd = fd

    def Attr_valeur(self, valeur):
        """Type->None
            Attribut une valeur au noeud appelant"""
        self.__valeur = valeur

    #Obtenir un attribut
    def Lire_pere(self):
        """None->noeud
            Renvoie le père au noeud appelant"""
        return self.__pere

    def Lire_fg(self):
        """None->noeud
            Renvoie le fils gauche au noeud appelant"""
        return self.__fg

    def Lire_fd(self):
        """None->noeud
            Renvoie le fils droit au noeud appelant"""
        return self.__fd

    def Lire_valeur(self):
        """None->Type
            Renvoie la valeur du noeud appelant"""
        return self.__valeur


class arbre:
    """ Une classe arbre basique"""
    def __init__(self, r):
        """noeud->arbre
            Crée un arbre de racine r"""
        self.__racine = r

    def __repr__(self):
        """None->String
            Retourne la chaîne servant pour l'affichage de l'arbre"""
        if self.__racine.Lire_fd()==None and self.__racine.Lire_fg()==None :
            return str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fd()==None :
            return "("+str(self.sous_arbre(self.__racine.Lire_fg()))+")<-"+str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fg()==None : 
            return str(self.__racine.Lire_valeur())+"->("+str(self.sous_arbre(self.__racine.Lire_fd()))+")"
        else :
            return "("+str(self.sous_arbre(self.__racine.Lire_fg()))+")<-"+str(self.__racine.Lire_valeur())+"->("+str(self.sous_arbre(self.__racine.Lire_fd()))+")"

    def ajouter(self, pere, n, position="g"):
        """noeud*noeud*String->None
            Ajoute le noeud n à l'arbre appelant en fils du noeud pere. Si position est "g" c'est un fils
            gauche, sinon un fils droit. Par défaut c'est un fils gauche."""
        if position == "g" :
            pere.Attr_fg(n)
            n.Attr_pere(pere)
        else :
            pere.Attr_fd(n)
            n.Attr_pere(pere)

    def sous_arbre(self, r):
        return arbre(r)

    def Lire_racine(self):
        return self.__racine
    
    def len(self):
        """None->String
            Renvoie la taille de l'arbre"""
        if self.__racine.Lire_fd()==None and self.__racine.Lire_fg()==None :
            return 1
        elif self.__racine.Lire_fd()==None :
            return 1 + self.sous_arbre(self.__racine.Lire_fg()).len()
        elif self.__racine.Lire_fg()==None : 
            return 1 + self.sous_arbre(self.__racine.Lire_fd()).len()
        else :
            return 1+ self.sous_arbre(self.__racine.Lire_fg()).len() + self.sous_arbre(self.__racine.Lire_fd()).len()
        
    
    def prefixe(self):
        """None->String
            Renvoie la chaîne correspndant au parcours préfixe de l'arbre appelant"""
        if self.__racine.Lire_fd()==None and self.__racine.Lire_fg()==None :
            return str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fd()==None :
            return str(self.__racine.Lire_valeur()) + " " + self.sous_arbre(self.__racine.Lire_fg()).prefixe()
        elif self.__racine.Lire_fg()==None : 
            return str(self.__racine.Lire_valeur()) + " " + self.sous_arbre(self.__racine.Lire_fd()).prefixe()
        else :
            return str(self.__racine.Lire_valeur()) + " " + self.sous_arbre(self.__racine.Lire_fg()).prefixe() + " " + self.sous_arbre(self.__racine.Lire_fd()).prefixe()
        

    def infixe(self):
        """None->String
            Renvoie la chaîne correspndant au parcours infixe de l'arbre appelant"""
        if self.__racine.Lire_fd()==None and self.__racine.Lire_fg()==None :
            return str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fd()==None :
            return self.sous_arbre(self.__racine.Lire_fg()).infixe() + " " + str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fg()==None : 
            return str(self.__racine.Lire_valeur()) + " " + self.sous_arbre(self.__racine.Lire_fd()).infixe()
        else :
            return self.sous_arbre(self.__racine.Lire_fg()).infixe() + " " + str(self.__racine.Lire_valeur()) + " " + self.sous_arbre(self.__racine.Lire_fd()).infixe()

    def suffixe(self):
        """None->String
            Renvoie la chaîne correspndant au parcours suffixe de l'arbre appelant"""
        if self.__racine.Lire_fd()==None and self.__racine.Lire_fg()==None :
            return str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fd()==None :
            return self.sous_arbre(self.__racine.Lire_fg()).suffixe() + " " + str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fg()==None : 
            return self.sous_arbre(self.__racine.Lire_fd()).suffixe() + " " + str(self.__racine.Lire_valeur())
        else :
            return self.sous_arbre(self.__racine.Lire_fg()).suffixe() + " " + self.sous_arbre(self.__racine.Lire_fd()).suffixe() + " " + str(self.__racine.Lire_valeur())

    def largeur(self):
        """None->String
            Renvoie la chaîne correspndant au parcours en largeur de l'arbre appelant"""
        File = [self.__racine]
        s = ""
        while len(File) > 0 :
            noeud = File[0]
            if noeud.Lire_fg() != None :
                File.append(noeud.Lire_fg())
            if noeud.Lire_fd() != None :
                File.append(noeud.Lire_fd())
            s += str(noeud.Lire_valeur()) + " "
            File.pop(0)
        return s

    def DFS(self, valeur) :
        pass

    def BFS(self, valeur) :
        pass

    def repr_graphique(self) :
        graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="yellow")
        File = [self.__racine]
        graph.add_node(pydot.Node(File[0].Lire_valeur(), shape="circle"))
        s = ""
        while len(File) > 0 :
            noeud = File[0]
            if noeud.Lire_fg() != None :
                File.append(noeud.Lire_fg())
                graph.add_node(pydot.Node(File[-1].Lire_valeur(), shape="circle"))
                graph.add_edge(pydot.Edge(File[0].Lire_valeur(), File[-1].Lire_valeur(), color="blue"))
            if noeud.Lire_fd() != None :
                File.append(noeud.Lire_fd())
                graph.add_node(pydot.Node(File[-1].Lire_valeur(), shape="circle"))
                graph.add_edge(pydot.Edge(File[0].Lire_valeur(), File[-1].Lire_valeur(), color="blue"))
            s += str(noeud.Lire_valeur()) + " "
            File.pop(0)
            graph.write_png("output.png")
        return s


if __name__ == "__main__":
    a = arbre(noeud(5))
    a.ajouter(a.Lire_racine(),noeud(10))
    a.ajouter(a.Lire_racine(), noeud(12), position="d")
    a.ajouter(a.Lire_racine().Lire_fg(), noeud(15), position="d")
    a.ajouter(a.Lire_racine().Lire_fg(), noeud(20), position="g")
    a.ajouter(a.Lire_racine().Lire_fd(), noeud(16), position="d")
    print("père :\n",a.Lire_racine())
    print("fils :\n", a.Lire_racine().Lire_fg())
    print(a)
    print(a.prefixe())
    print(a.infixe())
    print(a.suffixe())
    print(a.largeur())
    a.repr_graphique()
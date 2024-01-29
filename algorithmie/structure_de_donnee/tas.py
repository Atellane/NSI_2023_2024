from arbre_fini import arbre, noeud

class Tas(arbre):
    def __init__(self, tab, bool = True):
        if bool :
            super().__init__(noeud(tab.pop(0)))
            self.__racine = self._arbre__racine
            self.__last = ""
            while len(tab)>0:
                self.ajouter(tab.pop(0))
        else : 
            super().__init__(tab)
            self.__racine = self._arbre__racine
            self.__last = ""

    def tamisage(self):
        """None ->None
           Tamise le tas. 
        """
        m = self.__min__()
        #print("min du tas:", self, "est :", m.Lire_valeur())
        self.__echange__(m)
        #print("après échange:", self)
        if self.__racine.Lire_fg() != None :
            sag = self.sous_tas(self.__racine.Lire_fg())
            sag.tamisage()
        if self.__racine.Lire_fd() != None :
            sad = self.sous_tas(self.__racine.Lire_fd())
            sad.tamisage()
        #print("après tamisage, le Tas vaut", self)


    def ajouter(self, val):
        """ Type->None
            Ajoute la valeur val au tas, puis le tamise pour s'assurer de la stabilité de la structure"""
        #print(self.__last)
        print("Ajout de la valeur numéro :", self.len())
        n=noeud(val)
        r=self.__racine
        pos = self.__last
        if pos =="":
            n.Attr_pere(self.__racine)
            r.Attr_fg(n)
            self.__last="g"
        elif pos=="g":
            n.Attr_pere(r)
            r.Attr_fd(n)
            self.__last = "d"
        elif pos=="d":
            r = r.Lire_fg()
            n.Attr_pere(r)
            r.Attr_fg(n)
            self.__last="gg"
        else :
            #print("ancien :", self.__last)
            while not(pos=="g" or pos=="d") :
                chemin = pos[0]
                pos=pos[1:]
                if chemin == "g":
                    r= r.Lire_fg()
                else:
                    r= r.Lire_fd()
            if pos=="g":
                n.Attr_pere(r)
                r.Attr_fd(n)
                self.__last = self.__last[:-1] + "d"
            else :
                chemin = ""
                chemin_bis = ""
                prec = r
                r = r.Lire_pere()
                if prec == r.Lire_fg() :
                    chemin = "g" + chemin
                    r = r.Lire_fd()
                    chemin_bis += "d"
                    n.Attr_pere(r)
                    r.Attr_fg(n)
                    chemin += "d"
                    self.__last = self.__last[:-len(chemin)]
                    chemin_bis +="g"
                    self.__last+= chemin_bis
                else : 
                    if r != self.__racine :
                        chemin = "d"
                    while (prec == r.Lire_fd()) and (r != self.__racine):
                        prec = r
                        r = r.Lire_pere()
                        chemin = "d" + chemin
                        #print("chemin remontée : ",chemin)
                    if r != self.__racine:
                        r = r.Lire_fd()
                        chemin = "g" + chemin
                        chemin_bis = "d"
                    elif prec == r.Lire_fg():
                        r = r.Lire_fd()
                        chemin = chemin[1:]
                        chemin = "gd" + chemin
                        chemin_bis = "d"
                    else :
                        chemin = ""
                        chemin_bis = ""
                    while r.Lire_fg() != None :
                        r = r.Lire_fg()
                        chemin_bis += "g"
                    chemin_bis += "g"
                    n.Attr_pere(r)
                    r.Attr_fg(n)
                    self.__last = self.__last[:-len(chemin)]
                    self.__last+= chemin_bis
        #print("Tas avant tamisage :", self)
        #print(self.__last)
        self.tamisage() 
        #print("tamisage fini", self)  

    def __echange__(self, min):
        """ noeud -> None
            Echange la racine du tas/sous-tas avec le noeud min.
        """
        r = self.__racine
        if min != r :
            pere = r.Lire_pere()
            if min.Lire_pere() == r :
                r.Attr_pere(min)
            else :
                r.Attr_pere(min.Lire_pere())
            min.Attr_pere(pere)
            if pere != None :
                if pere.Lire_fd() == r :
                    pere.Attr_fd(min)
                else :
                    pere.Attr_fg(min)
            fd_r = r.Lire_fd()
            fg_r = r.Lire_fg()
            fd_min = min.Lire_fd()
            fg_min = min.Lire_fg()
            if r.Lire_pere() == min :
                if fd_r == min :
                    min.Attr_fd(r)
                    r.Attr_fd(fd_min)
                    min.Attr_fg(fg_r)
                    r.Attr_fg(fg_min)
                    if fg_r != None :
                        fg_r.Attr_pere(min)
                else :
                    min.Attr_fg(r)
                    r.Attr_fg(fg_min)
                    min.Attr_fd(fd_r)
                    r.Attr_fd(fd_min)
                    if fd_r != None :
                        fd_r.Attr_pere(min)
            else :
                fd_r.Attr_pere(min)
                fg_r.Attr_pere(min)
                min.Attr_fd(fd_r)
                r.Attr_fd(fd_min)
                min.Attr_fg(fg_r)
                r.Attr_fg(fg_min)
                pere = r.Lire_pere()
                if pere.Lire_fd() == min :
                    pere.Attr_fd(r)
                else :
                    pere.Attr_fg(r)
            self.__racine = min
            self._arbre__racine = min
            #print("tas nouveau :", self)

    def sous_tas(self, r):
        return Tas(r, False)
    
    def __min__(self):
        """None -> Noeud
           Retourne le noeud de valeur minimale du tas.
        """
        min = self.__racine
        if min.Lire_fg() == None and min.Lire_fd() == None:
            return min
        elif min.Lire_fg() == None :
            sad = self.sous_tas(min.Lire_fd())
            msad = sad.__min__()
            if min.Lire_valeur() > msad.Lire_valeur() :
                return msad
            else :
                return min
        elif min.Lire_fd() == None :
            sag = self.sous_tas(min.Lire_fg())
            msag = sag.__min__()
            if min.Lire_valeur() > msag.Lire_valeur() :
                return msag
            else :
                return min
        else :
            sad = self.sous_tas(min.Lire_fd())
            msad = sad.__min__()
            sag = self.sous_tas(min.Lire_fg())
            msag = sag.__min__()
            if min.Lire_valeur() > msad.Lire_valeur() :
                if msad.Lire_valeur() > msag.Lire_valeur() :
                    return msag
                else :
                    return msad
            else :
                if min.Lire_valeur() > msag.Lire_valeur() :
                    return msag
                else :
                    return min
                
    def rechercher(self, valeur) :
        """Type->Bool
            Renvoie vrai si la valeur est dans le tas"""
        if str(valeur) in self.prefixe().split(" ") :
            r : noeud = self.__racine
            trouve = False
            if r.Lire_valeur() == valeur :
                trouve = True
            else :
                if r.Lire_fg() != None :
                    trouve = self.sous_tas(r.Lire_fg()).rechercher(valeur)
                if ((r.Lire_fd() != None) and (not trouve)):
                    trouve = self.sous_tas(r.Lire_fd()).rechercher(valeur)
            return trouve
        else : 
            return False
        
    def supprimer(self, valeur) :
        """Type->None
            Supprime la valeur du tas"""
        if self.rechercher(valeur) :
            liste_noeuds = self.prefixe().split(" ")
            liste_noeuds.remove(str(valeur))
            self.__racine = noeud(int(liste_noeuds.pop(0)))
            self._arbre__racine = self.__racine
            self.__last = ""
            for val in liste_noeuds :
                val = int(val)
                self.ajouter(val) 

def Tri_par_tas(T) :
    """List[Type]->None
        Tri le tableau fourni à l'aide d'un tas"""
    tri = []
    tas = Tas(T)
    while tas.len()>1 :
        racine = tas.Lire_racine().Lire_valeur()
        tri.append(racine)
        tas.supprimer(racine)
    racine = tas.Lire_racine().Lire_valeur()
    tri.append(racine)
    return tri
            

if __name__ == "__main__" :
    Tab = [10,2,5,12,15,20,1,3,7,25]
    T = Tas(Tab)
    print(Tab)
    print(T)
    T.repr_graphique("T.png")
    print(T.rechercher(2))
    print(T.rechercher(17))
    T.supprimer(1)
    T.repr_graphique()
    Tab = [10,2,5,12,15,20,1,3,7,25]
    print(Tri_par_tas(Tab))
    # from random import randint
    # tab = []
    # for _ in range(1000) :
    #     j = randint(0,10000)
    #     if not (j in tab) :
    #         tab.append(j)
    # print(tab)    
    # T2 = Tas(tab)
    # print(T2)
    # T2.repr_graphique()
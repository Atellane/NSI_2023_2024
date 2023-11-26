"""Module de mise à disposition de l'objet carte"""

class Carte() :
    __valeur = 0
    __couleur = ""
    __figure = ""

    __dico_valeur = {"As" : 1, "2" : 2,
                       "3" : 3, "4" : 4,
                       "5" : 5, "6" : 6,
                       "7" : 7, "8" : 8,
                       "9" : 9, "10" : 10,
                       "Valet" : 11,
                       "Dame" : 12,
                       "Roi" : 13}
    
    __dico_retour_valeur = {1 : "As", 2 : "2",
                       3 : "3", 4 : "4",
                       5 : "5", 6 : "6",
                       7 : "7", 8 : "8",
                       9 : "9", 10 : "10",
                       11 : "Valet",
                       12 : "Dame",
                       13 : "Roi"}

    def __init__(self, valeur, couleur) :
        
        self.__valeur = self.__dico_valeur[valeur]
        self.__couleur = couleur
        self.__Attrib_figure()

    def __Attrib_figure(self):
        self.__figure = str(self.__dico_retour_valeur[self.__valeur]) + " de " + self.__couleur

    def __repr__(self) : 
       return self.__figure
    
    def Affiche_valeur(self) :
        return self.__dico_retour_valeur[self.__valeur]
    
    def Affiche_couleur(self) :
        return self.__couleur
    
    def Affiche_figure(self) :
        return self.__figure
    
    def Attr_valeur(self, valeur) :
        self.__valeur = self.__dico_valeur[valeur]
        self.__Attrib_figure()

    def Attr_couleur(self, couleur) :
        self.__couleur = couleur
        self.__Attrib_figure()
 

if __name__ == "__main__" :
    macarte = Carte("Dame", "pique")
    print(macarte)
    macarte.Attr_valeur("As")
    print(macarte)
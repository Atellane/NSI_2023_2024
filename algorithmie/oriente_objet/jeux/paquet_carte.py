from carte import Carte
from random import shuffle
from random import randint as rnd

class Paquet_Cartes:
    """Définit un jeu de carte caractérisé par le paquet de ses cartes"""

    __paquet = []
    __Nombre = 0

    def __init__(self, n):
        """int->Paquet_Cartes
            Crée un paquet de carte du nombre de cartes indiqué, pour les valeurs 32 et 52 paquet classique, sinon paquet aléatoire"""
        self.__Nombre = n
        if self.__Nombre == 32:
            self.__paquet.append(Carte("As", "Carreau"))
            self.__paquet.append(Carte("As", "Coeur"))
            self.__paquet.append(Carte("As", "Pique"))
            self.__paquet.append(Carte("As", "Trèfle"))
            for i in range(7, 11):
                self.__paquet.append(Carte(str(i), "Carreau"))
                self.__paquet.append(Carte(str(i), "Coeur"))
                self.__paquet.append(Carte(str(i), "Pique"))
                self.__paquet.append(Carte(str(i), "Trèfle"))
            self.__paquet.append(Carte("Valet", "Carreau"))
            self.__paquet.append(Carte("Valet", "Coeur"))
            self.__paquet.append(Carte("Valet", "Pique"))
            self.__paquet.append(Carte("Valet", "Trèfle"))
            self.__paquet.append(Carte("Dame", "Carreau"))
            self.__paquet.append(Carte("Dame", "Coeur"))
            self.__paquet.append(Carte("Dame", "Pique"))
            self.__paquet.append(Carte("Dame", "Trèfle"))
            self.__paquet.append(Carte("Roi", "Carreau"))
            self.__paquet.append(Carte("Roi", "Coeur"))
            self.__paquet.append(Carte("Roi", "Pique"))
            self.__paquet.append(Carte("Roi", "Trèfle"))
        elif self.__Nombre == 52:
            self.__paquet.append(Carte("As", "Carreau"))
            self.__paquet.append(Carte("As", "Coeur"))
            self.__paquet.append(Carte("As", "Pique"))
            self.__paquet.append(Carte("As", "Trèfle"))
            for i in range(2, 11):
                self.__paquet.append(Carte(str(i), "Carreau"))
                self.__paquet.append(Carte(str(i), "Coeur"))
                self.__paquet.append(Carte(str(i), "Pique"))
                self.__paquet.append(Carte(str(i), "Trèfle"))
            self.__paquet.append(Carte("Valet", "Carreau"))
            self.__paquet.append(Carte("Valet", "Coeur"))
            self.__paquet.append(Carte("Valet", "Pique"))
            self.__paquet.append(Carte("Valet", "Trèfle"))
            self.__paquet.append(Carte("Dame", "Carreau"))
            self.__paquet.append(Carte("Dame", "Coeur"))
            self.__paquet.append(Carte("Dame", "Pique"))
            self.__paquet.append(Carte("Dame", "Trèfle"))
            self.__paquet.append(Carte("Roi", "Carreau"))
            self.__paquet.append(Carte("Roi", "Coeur"))
            self.__paquet.append(Carte("Roi", "Pique"))
            self.__paquet.append(Carte("Roi", "Trèfle"))
        else:
            n = 0
            while n < self.__Nombre:
                valeur = rnd(1,13)
                couleur = rnd(1,4)
                if valeur == 1:
                    valeur = "As"
                elif valeur <11:
                    valeur = str(valeur)
                elif valeur == 11:
                    valeur = "Valet"
                elif valeur == 12:
                    valeur = "Dame"
                else:
                    valeur = "Roi"
                if couleur == 1:
                    couleur = "Carreau"
                elif couleur == 2:
                    couleur = "Coeur"
                elif  couleur == 3:
                    couleur = "Pique"
                else:
                    couleur = "Trèfle"
                c = Carte(valeur, couleur)
                if not (c in self.__paquet):
                    self.__paquet.append(c)
                    n += 1
        
    
    def Obtenir_Nombre_Carte(self):
        """None->int
           Renvoie le nombre de cartes dans le paquet"""
        return self.__Nombre

    def Obtenir_Cartes(self):
        """None->List[Cartes]
           Renvoie un tableau des cartes du paquet"""
        return self.__paquet

    def Battre_Cartes(self):
        """None->None
           Mélange les différentes cartes du paquet"""
        shuffle(self.__paquet)

    def Tirer_Carte(self):
        """None->Carte
           Fournit la première carte du paquet et la retire du paquet"""
        carte = self.__paquet.pop()
        self.__Nombre -=1
        return carte

if __name__ == "__main__":
    paquet_test = Paquet_Cartes(52)
    print(paquet_test.Obtenir_Nombre_Carte())
    paquet = paquet_test.Obtenir_Cartes()
    cartes = [paquet[i].Obtenir_Figure() for i in range(paquet_test.Obtenir_Nombre_Carte())]
    print(cartes)
    paquet_test.Battre_Cartes()
    paquet = paquet_test.Obtenir_Cartes()
    print(paquet)
    print(paquet_test.Tirer_Carte())
    print(paquet_test.Obtenir_Cartes())
                    
from pile import Pile

# ne fonctionne pas, la première boucle while s'exécute à l'infini, je ne comprend pas pourquoi
def permutation_circulaire(pile: object, nombreDeDecalage: int) -> None:
    """prend en paramètre une pile et un nombre n de décalage et décale la case du haut de la pile vers le bas n fois"""
    reste_pile: object = Pile()
    a = 0
    for i in range(nombreDeDecalage):
        
        premier_element = pile.obtenir_element() # <T>
        pile.retirer()
        while not pile.est_vide():
            print(pile, "\tDÉBUT")
            reste_pile.ajouter(pile.obtenir_element())
            print(reste_pile, "\tRESTE PILE")
            pile.retirer()
            print(pile, "\tFIN")
        pile.ajouter(premier_element)
        while not reste_pile.est_vide():
            pile.ajouter(reste_pile.obtenir_element())
            reste_pile.retirer()

pile = Pile(0)
pile.ajouter(2)
pile.ajouter(5)
pile.ajouter("UwU")
print(pile)
permutation_circulaire(pile, 2)
print(pile)
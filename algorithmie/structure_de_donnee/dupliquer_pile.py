from pile import Pile

# ne fonctionne plus, il dois y avoir un problème dans la manière où je retire les éléments de la pile
def duppliquer_pile(pile: Pile) -> Pile:
    pile_temp: Pile = Pile()
    pile_retour: Pile = Pile()
    while not pile.est_vide():
        pile_temp.ajouter(pile.obtenir_element())
        pile.retirer()
    while not pile_temp.est_vide():
        pile.ajouter(pile_temp.obtenir_element())
        pile_retour.ajouter(pile_temp.obtenir_element())
        pile_temp.retirer()
    return pile_retour

if __name__ == "__main__":
    pile = Pile("UwU")
    print(pile)
    print(duppliquer_pile(pile))
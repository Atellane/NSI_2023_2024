def dichotomie(tableau: list, valeur: int) -> bool:
    debutIntervalleRecherche = 0
    finIntervalleRecherche = len(tableau) - 1
    
    while debutIntervalleRecherche <= finIntervalleRecherche:
        positionDansTableau = (debutIntervalleRecherche + finIntervalleRecherche) // 2
        
        if tableau[positionDansTableau] == valeur:
            # on a trouvé valeur
            return True
        elif tableau[positionDansTableau] < valeur:
            debutIntervalleRecherche = positionDansTableau + 1
        else:
            finIntervalleRecherche = positionDansTableau - 1
    
    # on a debutIntervalleRecherche > finIntervalleRecherche (pas possible, ça veut donc dire qu'on a rien trouvé)
    return False
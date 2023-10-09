def positionLettrePreBoyerMoore(motif: str) -> dict:
    """prépare le ditionaire avec le motif et la psotion qui corespond, exemple : Ulysse -> {"U": 1, "l": 2, "y": 3, "s": 4, "s": 5, "e": 6}"""
    dictMotif: dict = {}
    longueurMotif: int = len(motif)
    for i in range(0, longueurMotif-1):
        dictMotif[motif[i]] = longueurMotif-i
    return dictMotif

def algoBoyerMoore(motif: str, texte: str) -> list:
    """recherche motif dans texte"""
    longueurMotif: int = len(motif)
    longueurTexte: int = len(texte)
    positionDansLeTexte: int = m-1
    positionLettre: dict = positionLettrePreBoyerMoore(motif)
    positions: list = []
    while positionDansLeTexte < longueurTexte:
        i = longueurTexte
        while i > 0 and texte[positionDansLeTexte-longueurTexte+i] == motif[i]:
            i -= 1
        if i == 0:
            positions.append(positionDansLeTexte)
            positionDansLeTexte += 1
        else if texte[positionDansLeTexte] in positionLettre:
            positionDansLeTexte += positionLettre[texte[positionDansLeTexte]]
        else:
            positionDansLeTexte += longueurTexte
    return positions

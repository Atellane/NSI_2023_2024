def trouver_meme_dans_sous_tableau(tableau, caractere):
    est_trouve: bool = False
    for element in tableau:
        if est_trouve == False:
            if isinstance(element, list):
                est_trouve = trouver_meme_dans_sous_tableau(element, caractere)
            else:
                est_trouve = (element == caractere)
    return est_trouve


if __name__ == "__main__":
    tableau = ["a", ["b", ["c"]]]
    print(trouver_meme_dans_sous_tableau(tableau, "b"))
    print(trouver_meme_dans_sous_tableau(tableau, "c"))
    print(trouver_meme_dans_sous_tableau(tableau, "UwU"))
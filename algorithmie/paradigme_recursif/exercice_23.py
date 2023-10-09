def minList(liste: list, indice: int) -> int:
    if indice == 0:
        print(liste, indice)
        return liste[indice]
    else:
        print(liste, indice)
        return min(minList(liste, indice-1), liste[indice])

liste: list = [1,2]

print("toto")
print(minList(liste, len(liste)-1))
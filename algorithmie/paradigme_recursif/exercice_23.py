def minList(liste: list, indice: int) -> int:
    if indice == 0:
        return liste[indice]
    else:
        return min(minList(liste, indice-1), liste[indice])

"""
996 - 1 = exec réel, récurivité 993 car 995 - (premier appel de la fonction + dernier appel qui renvoie une valeur et non pas une instanciation de notre fonction)
= 995 - 2 = 993
"""
liste: list = [i for i in range(996)]

print("toto")
print(minList(liste, len(liste)-1))
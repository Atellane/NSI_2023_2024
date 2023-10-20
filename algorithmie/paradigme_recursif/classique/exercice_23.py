def minList(liste: list, indice: int) -> int:
    if indice == 0:
        return liste[indice]
    else:
        return min(minList(liste, indice-1), liste[indice])

if __name__ == "__main__":
    tab: list = []
    for i in range(999):
        tab.append(i)

    minList(tab, len(tab)/2)
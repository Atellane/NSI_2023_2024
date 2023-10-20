from sys import path
path.append("..")

from classique.exercice_23 import minList
from random import randint

def minListButBetter(laListe: list, indice: int = -1) -> int:
    lenLaListe: int = round(len(laListe)/2)
    debutListe: list = laListe[lenLaListe:]
    finListe: list = laListe[:lenLaListe]
    minDebutListe: int = minList(debutListe, len(debutListe)-1)
    minFinListe: int = minList(finListe, len(finListe)-1)
    if minDebutListe <= minFinListe:
        return minDebutListe
    else:
        return minFinListe

def createAnArray() -> list:
    while True:
        try:
            nombreDElementDansTableau: int = int(input("Combien voulez-vous d'élément dans votre tableau ?\n"))
            valeurMAxPossible: int = int(input("Quel doit être la valeur max possible dans vorte tableau ?\n"))
            valeurMinPossible: int = int(input("Quel doit être la valeur min possible dans vorte tableau ?\n"))
            if valeurMinPossible >= valeurMAxPossible:
                raise ValueError("le minimum ne peut pas être supèrieur ou égal au maximum.")
            break
        except ValueError as error:
            if error == None:
                print("Seuls les entiers sont acceptés.")
            else:
                print(error)

    monTableau: list = []
    for _ in range(nombreDElementDansTableau):
        monTableau.append(randint(valeurMinPossible, valeurMAxPossible))

    return monTableau

if __name__ == "__main__":
    tableauExemple: list = createAnArray()
    print(minListButBetter(tableauExemple, len(tableauExemple)-1))
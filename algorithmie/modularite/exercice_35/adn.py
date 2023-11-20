"""
permet de lire et de modifier un fichier .fasta
"""
from random import randint
from re import findall
BASE_COMP: dict = {
    "A": "T",
    "T": "C",
    "G": "C",
    "C": "G"
}

def lit_fasta(fastaName: str) -> list:
    """
    récupère la liste de séquence adn présente dans un fichier
    """
    sequenceAdn: list = []
    with open(fastaName, "r") as fichier:
        for ligne in fichier:
            if ligne[0] != ">":
                sequenceAdn.append(ligne.strip())
    return sequenceAdn

def seq_alea(tailleSequenceAdn: int) -> str:
    """
    génère une séquence ADN aléatoire
    """
    base: list = list(BASE_COMP.keys())
    sequenceAdn: str = ""
    for i in range(tailleSequenceAdn):
        lettre: str = base[randint(0, len(base)-1)]
        sequenceAdn += lettre
    return sequenceAdn


def comp_inv(sequenceAdn: str) -> str:
    """
    prend en argument une séquence ADN et renvoie sa séquence complèmentaire 
    """
    sequenceAdnCompInv: str = ""
    for lettre in sequenceAdn:
        sequenceAdnCompInv += BASE_COMP[lettre]
    return sequenceAdnCompInv

def prop_gc(sequenceAdn: str) -> float:
    """
    prend en argument une séquence ADN et renvoie la proportion GC (G (Guanine) C (Cytosine)) par rapport au nombre total de base (A, T, G, C)
    """
    motifC: str = r'(?i)(C+)'  # (?i) pour ne pas tenir compte de si c'est une majuscule ou une minuscule, [c]+ pour correspondre à une séquence de 'c'
    occurencesC: int = len(findall(motifC, sequenceAdn))
    print(occurencesC)
    motifG: str = r'(?i)(G+)'
    occurencesG: int = len(findall(motifG, sequenceAdn))
    print(occurencesG)
    occurencesGC: int = occurencesC + occurencesG
    print(occurencesGC)
    propGC: float = occurencesGC/len(sequenceAdn)
    return propGC

if __name__ == "__main__":
    sequencesAdn: list = lit_fasta("adn.fasta")
    print(sequencesAdn)
    sequenceAdnAlea: str = seq_alea(6)
    print(sequenceAdnAlea)
    compSequenceAdnAlea: str = comp_inv(sequenceAdnAlea)
    print(BASE_COMP)
    print(compSequenceAdnAlea)
    proportionGC: float = prop_gc(compSequenceAdnAlea)
    print(proportionGC)
class File:
    __liste =[]

    def __init__(self):
        self.__liste = []
    
    def ajouter(self, valeur):
        self.__liste.append(valeur)

    def enlever(self):
        return self.__liste.pop(0)
    
    def longueur(self):
        return len(self.__liste)
    
    def est_vide(self):
        return len(self.__liste) == 0

    def __repr__(self):
        s = "\u2503"
        ssup = "\u250f"
        sinf = "\u2517"
        for x in self.__liste:
            ssup += len(str(x))*"\u2501" + "\u2533"
            sinf += len(str(x))*"\u2501" + "\u253B"
            s += str(x) + "\u2503"
        if self.__liste != []:
            ssup = ssup[:-1]
            sinf = sinf[:-1]
            s = s[:-1]
        ssup += "\u2513"
        sinf += "\u251B"
        s += "\u2503"
        return ssup + "\n" + s + "\n" + sinf

if __name__ == "__main__":
    f = File()
    print(f)
    f.ajouter(5)
    f.ajouter("A")
    f.ajouter("qdsvkjfh")
    print(f)
    f.enlever()
    print(f)
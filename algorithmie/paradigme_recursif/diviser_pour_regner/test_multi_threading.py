from threading import Thread
from time import time
def miaou():
    miaouuuuuuu: int = 2
    for i in range(99999999):
        miaouuuuuuu = miaouuuuuuu**i

def graou():
    graouuuuuuu: int = 2
    for i in range(99999999):
        graouuuuuuu = graouuuuuuu**(-i)

debut: int = time()
mrawww: object = Thread(target=miaou)
mrawww.run()
grawwww: object = Thread(target=graou)
grawwww.run()
fin: int = time()
temps: int = fin - debut
print(temps)

debut = time()
miaou()
graou()
fin = time()
temps = fin - debut
print(temps)
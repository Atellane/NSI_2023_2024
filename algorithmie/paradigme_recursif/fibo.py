def fibonacci(termeDeLaSuite: int) -> int:
    if ((termeDeLaSuite == 0) or (termeDeLaSuite==1)):
        return 1
    else:
        return fibonacci(termeDeLaSuite - 1) + fibonacci(termeDeLaSuite - 2)

n: int = None
while n == None:
    try:
        n=int(input("quelle terme de la suite de fibonnaci voulez-vous calculer ?"))
    except ValueError:
        print("seul les entiers sont accepter")

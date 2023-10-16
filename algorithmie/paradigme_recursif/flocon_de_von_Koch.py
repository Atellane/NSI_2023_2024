import turtle

# Fonction pour dessiner une ligne droite avec la longueur donnée
def ligne_koch(longueur, n):
    if n == 0:
        turtle.forward(longueur)
    else:
        longueur /= 3.0
        ligne_koch(longueur, n - 1)
        turtle.left(60)
        ligne_koch(longueur, n - 1)
        turtle.right(120)
        ligne_koch(longueur, n - 1)
        turtle.left(60)
        ligne_koch(longueur, n - 1)

# Fonction pour dessiner un flocon de Koch complet
def flocon_koch(longueur, n):
    for _ in range(3):
        ligne_koch(longueur, n)
        turtle.right(120)
    print("done !")

# Initialisation de Turtle
turtle.speed(0)  # Ajuster la vitesse si nécessaire
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

# Appel de la fonction pour dessiner le flocon de Koch
longueur_cote = 300
n_iterations = 4  # Augmenter le nombre d'itérations pour un flocon plus complexe
flocon_koch(longueur_cote, n_iterations)

# Maintien ouverte la fenêtre Turtle
turtle.done()
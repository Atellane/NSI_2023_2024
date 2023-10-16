from tkinter import *
from time import sleep


def palet(n, col, pos):
    nb = nb_palets.get()
    canvas.create_rectangle((50+(col-1)*250+(n-1)*10*(10/nb), 500-(pos-1)*(380/nb)), (250+(col-1)*250-(n-1)*10*(10/nb),
                                                                                      500-pos*(380/nb)), fill="red")


def interface():
    sleep(0.1)
    canvas.delete("all")
    canvas.create_line((10, 500), (790, 500), fill="brown", width=5)
    canvas.create_line((150, 500), (150, 100), fill="brown", width=5)
    canvas.create_line((400, 500), (400, 100), fill="brown", width=5)
    canvas.create_line((650, 500), (650, 100), fill="brown", width=5)
    hauteur = 1
    for i in Tiges[0]:
        palet(i, 1, hauteur)
        hauteur += 1
    hauteur = 1
    for i in Tiges[1]:
        palet(i, 2, hauteur)
        hauteur += 1
    hauteur = 1
    for i in Tiges[2]:
        palet(i, 3, hauteur)
        hauteur += 1
    canvas.pack()
    canvas.update()


def hanoi(d, a, p, n):
    global Tiges
    if n == 2:
        Tiges[p].append(Tiges[d].pop())
        interface()
        Tiges[a].append(Tiges[d].pop())
        interface()
        Tiges[a].append(Tiges[p].pop())
        interface()
    else:
        hanoi(d, p, a, n-1)
        Tiges[a].append(Tiges[d].pop())
        hanoi(p, a, d, n-1)


def hanoi_go():
    global Tiges
    n = nb_palets.get()
    Tiges= [[i for i in range(1, n + 1)], [], []]
    hanoi(0, 2, 1, n)

def switch():
    print(nb_palets["state"])
    nb_palets["state"] = DISABLED
    print(nb_palets["state"])
    hanoi_go()
    nb_palets["state"] = NORMAL

Tiges = [[], [], []]
fenetre = Tk()
cadre = Frame(fenetre, width=800, height=700, borderwidth=1)
cadre.pack()
label_cadre = Label(cadre, text="Résolution des tours de hanoï")
label_cadre.pack()
canvas = Canvas(cadre, background="blue", width=800, height=600)
canvas.pack()
cadre_btn = Frame(fenetre)
cadre_btn.pack()
btn_go = Button(cadre_btn, text="résolution", command=switch)
btn_quitter = Button(cadre_btn, text="quitter", command=fenetre.quit)
nb_palets = Scale(cadre_btn, orient="horizontal", from_=1, to_=20)
nb_palets.grid(column=0, row=0)
btn_go.grid(column=1, row=0)
btn_quitter.grid(column=2, row=0)
interface()
fenetre.mainloop()
import os, sys, pygame
from threading import Thread
from random import shuffle
from pygame_textinput import TextInputVisualizer
from get import get_info, get_my_ip
from send import send_info

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
GREEN: tuple = (0, 100, 0)
WHITE: tuple = (255, 255, 255)
BLACK: tuple = (0, 0, 0)

# Paramètres de la fenêtre
screen: pygame.Surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

# Font pour le texte
font: pygame.font.Font = pygame.font.Font(None, 36)


def draw_text(text: str, font: pygame.font.Font, color: tuple, x: int, y: int) -> None:
    text_surface: pygame.Surface = font.render(text, True, color)
    text_rect: pygame.Rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def wait_for_someone_to_initialize_the_game() -> None:
    connection: tuple = get_info()
    my_hand: list = connection[1].rsplit(", ")
    for index_card, card in enumerate(my_hand):
        my_hand[index_card] = get_cards_from_their_names([card])[0]
    connection = get_info()
    discard_pile: list = [get_cards_from_their_names([connection[1]])[0]]
    play([connection[0]], False, my_hand, discard_pile)

def draw_a_card(deck: list) -> dict:
    card: dict = deck.pop(-1)
    return card

def create_a_card(name: str, image: pygame.surface.Surface) -> dict:
    return {"name": name, "image": image}

def get_card_images_names() -> list:
    # Chemin du répertoire courant
    directory: str = os.getcwd()

    # Liste tous les fichiers du répertoire courant
    files: list = os.listdir(directory)
    temp: list = []
    # Affiche les noms des fichiers
    for file in files:
        if (".png" in file) and (not ("UNO-Front.png" == file))  and (not ("pygame_tiny.png" == file)) and (not ("back_uno_card.png" == file)):
            if (not ("zero" in file)) and (not ("changement_de_couleur.png" == file)) and (not ("plus_quatre.png") == file) and (not ("back_uno_card.png" == file)):
                for _ in range(2):
                    temp.append(file)
            elif (not ("zero" in file)) and (not ("back_uno_card.png" == file)):
                for _ in range(4):
                    temp.append(file)
            else:
                temp.append(file)

    return temp

def get_cards_from_their_names(cards: list) -> list:
    deck: list = []
    name = cards[0]
    if ("plus quatre" in cards[0]) and (not "plus quatre" == cards[0]):
        temp = cards[0].split(" ")[:-1]
        temp[-1] = " " + temp[-1]
        cards[0] = "".join(temp)
    elif ("changement de couleur" in cards[0]) and (not "changement de couleur" == cards[0]):
        temp = cards[0].split(" ")[:-1]
        cards[0] = ""
        for i in temp:
            cards[0] += f"{i} "
        cards[0] = cards[0][:-1]
            
    if "_" in cards[0]:
        for card in cards:
            deck.append(create_a_card(card.replace("_", " ").replace(".png", ""), pygame.image.load(card)))
    else:
        for card in cards:
            deck.append(create_a_card(name, pygame.image.load(card.replace(" ", "_")+".png"))) 
    return deck

def get_my_hand(deck: list) -> list:
    my_hand: list = []
    for i in range(7):
        my_hand.append(deck.pop(0))
    return my_hand

def get_ip() -> str:
    running: bool = True
    text_input: TextInputVisualizer = TextInputVisualizer()

    while running:
        screen.fill(BLACK)  # Définir l'arrière-plan en noir
        draw_text("Entrez l'ip de vos adversaires, espacez chaque ip d'un espace (max 9 ip) :", font, WHITE, SCREEN_WIDTH // 2 - 100, 50)
        button_text: str = f"Attendre qu'un-e autre joueur-euse se connecte. (Votre ip : {get_my_ip()})"
        button_width: int = font.size(button_text)[0] + 20  # Ajoutez un padding de 20 pixels
        button_height: int = font.size(button_text)[1] + 20  # Ajoutez un padding de 20 pixels
        button_x: int = (SCREEN_WIDTH - button_width) // 2

        button: pygame.Rect = pygame.Rect(button_x, 250, button_width, button_height)

        if button.collidepoint(pygame.mouse.get_pos()):
            if click:
                screen.fill(BLACK)
                draw_text("Veuillez patientez...", font, WHITE, SCREEN_WIDTH // 2 - 100, 50)
                wait_for_someone_to_initialize_the_game()
        
        pygame.draw.rect(screen, (255, 0, 0), button)


        draw_text(button_text, font, BLACK, button_x + button_width // 2, 250 + button_height // 2)

        click: bool = False
        events: list = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Récupérer l'adresse IP saisie par l'utilisateur
                    ip_address: str = text_input.value
                    return ip_address  # Retourner l'adresse IP saisie par l'utilisateur
                    # Réinitialiser la saisie
                    text_input.clear_text()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        # Mettre à jour la saisie de texte
        text_input.update(events)
        # Récupérer la surface de la saisie de texte
        text_surface: pygame.Surface = text_input.surface
        # Créer une surface pour l'arrière-plan blanc de la zone de texte
        text_background: pygame.Surface = pygame.Surface((text_surface.get_width(), text_surface.get_height()))
        text_background.fill(WHITE)
        # Afficher l'arrière-plan blanc de la zone de texte sur l'écran
        screen.blit(text_background, (SCREEN_WIDTH // 2 - 100, 150))
        # Afficher la saisie de texte sur l'écran par-dessus l'arrière-plan blanc
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - 100, 150))

        pygame.display.update()
        pygame.time.Clock().tick(30)

def main_menu() -> None:
    running = True
    while running:
        screen.fill(BLACK)
        draw_text("Menu Principal", font, WHITE, SCREEN_WIDTH // 2, 50)
        
        mx, my = pygame.mouse.get_pos()

        button_1_text: str = "Commencer une partie"
        button_2_text: str = "Quitter"
        button_width_1: int = font.size(button_1_text)[0] + 20  # Ajoutez un padding de 20 pixels
        button_height_1: int = font.size(button_1_text)[1] + 20  # Ajoutez un padding de 20 pixels
        button_x_1: int = (SCREEN_WIDTH - button_width_1) // 2
        button_width_2: int = font.size(button_2_text)[0] + 20  # Ajoutez un padding de 20 pixels
        button_height_2: int = font.size(button_2_text)[1] + 20  # Ajoutez un padding de 20 pixels
        button_x_2: int = (SCREEN_WIDTH - button_width_2) // 2

        button_1: pygame.Rect = pygame.Rect(button_x_1, 150, button_width_1, button_height_1)
        button_2: pygame.Rect = pygame.Rect(button_x_2, 250, button_width_2, button_height_2)
        if button_1.collidepoint((mx, my)):
            if click:
                ip_address: str = get_ip()
                print(f"L'/Les adresse-s ip renseignée-s est/sont \"{ip_address}\".")
                ip_address: list = ip_address.rsplit(" ")
                if len(ip_address) > 9:
                    raise Exception("9 joueurs au maximum peuvent participer, merci de ne renseigner que 9  ip au max")
                if ip_address == [""]:
                    raise Exception("Tu dois rentrer au moins 1 ip.")
                play(ip_address)
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (0, 255, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        draw_text(button_1_text, font, BLACK, button_x_1 + button_width_1 // 2, 150 + button_height_1 // 2)
        draw_text(button_2_text, font, BLACK, button_x_2 + button_width_2 // 2, 250 + button_height_2 // 2)

        click: bool = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        pygame.time.Clock().tick(60)

def do_a_turn(my_hand: list, discard_pile: list) -> dict:
    buttons: list = []
    sc_cards: list = []
    # Parcourir chaque carte dans la main du joueur
    for i, card in enumerate(my_hand):
        # Créer un bouton cliquable pour chaque carte
        sc_cards.append(pygame.Surface((50 + i * 120, SCREEN_HEIGHT - 200)))
        sc_cards[i].set_alpha(0)
        sc_cards[i].fill(WHITE)
        button_rect = pygame.Rect(50 + i * 120, SCREEN_HEIGHT - 200, 100, 150)  # Position et taille du bouton
        button = {"screen": sc_cards[i] ,"rect": button_rect, "card": card}
        buttons.append(button)
    
    sc_cards.append(pygame.Surface((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.75)))
    sc_cards[-1].set_alpha(255)
    sc_cards[-1].fill(WHITE)
    button_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5, 100, 50)
    button = {"screen": sc_cards[-1], "rect": button_rect, "card": {"name": "Piocher"}}
    buttons.append(button)

    # Boucle principale pour le rendu et l'interaction avec les boutons
    running = True
    while running:

        draw_text("Piocher", font, BLACK, button["rect"].centerx, button["rect"].centery)
        
        # Afficher "C'est ton tour" en haut au centre de l'écran
        draw_text("C'est ton tour", font, WHITE, SCREEN_WIDTH // 2, 50)

        # Afficher les cartes dans la main du joueur
        for button in buttons:
            pygame.draw.rect(button["screen"], WHITE, button["rect"])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        if button["card"]["name"] == "Piocher":
                            # Si l'utilisateur demande à piocher, renvoyer Piocher
                            return button["card"]["name"]
                        elif "plus quatre" in button["card"]["name"] or "changement de couleur" in button["card"]["name"]:
                            my_hand.remove(button["card"])
                            discard_pile.append(button["card"])
                            # Si c'est une carte spéciale, demander à l'utilisateur de choisir une couleur
                            color_choice = choose_color()
                            # Insérer la couleur choisie au début du nom de la carte
                            button["card"]["name"] += (" " + color_choice)
                            # Renvoyer le nom de la carte
                            return button["card"]
                        elif (discard_pile[-1]["name"].split(" ")[0] == button["card"]["name"].split(" ")[0]) or discard_pile[-1]["name"].split(" ")[-1] == button["card"]["name"].split(" ")[-1]: # vérifie si chiffre ou couleur identique
                            discard_pile.append(button["card"])
                            my_hand.remove(button["card"])
                            return button["card"]
                        else:
                            draw_text("Sélection invalide", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.25)


def choose_color() -> str:
    # Initialisation des couleurs
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    # Définition des boutons de couleur
    color_buttons = [
        {"color": BLUE, "text": "Bleu", "rect": pygame.Rect(250, 350, 100, 50)},
        {"color": GREEN, "text": "Vert", "rect": pygame.Rect(450, 350, 100, 50)},
        {"color": RED, "text": "Rouge", "rect": pygame.Rect(250, 400, 100, 50)},
        {"color": YELLOW, "text": "Jaune", "rect": pygame.Rect(450, 400, 100, 50)}
    ]

    # Boucle principale pour le rendu et l'interaction avec les boutons
    running = True
    while running:
        screen.fill(GREEN)
        for button in color_buttons:
            pygame.draw.rect(screen, button["color"], button["rect"])
            draw_text(button["text"], font, BLACK, button["rect"].centerx, button["rect"].centery)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in color_buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        return button["text"].lower()  # Renvoyer le nom de la couleur sélectionnée

def draw_my_hand(my_hand: list) -> None:
    # Dessine la main du joueur sur l'écran
    hand_size = len(my_hand)
    if hand_size > 0:
        # Calcule l'espace horizontal entre les cartes
        space_between_cards = min(120, (SCREEN_WIDTH - 100) // hand_size)
        # Calcule la taille maximale pour chaque carte en fonction de l'espace disponible
        max_card_width = space_between_cards - 10  # 10 pixels de marge entre les cartes
        max_card_height = int(max_card_width * 1.4)  # Ratio hauteur-largeur typique pour une carte

        # Dessine chaque carte dans la main du joueur
        for i, card in enumerate(my_hand):
            card_image = card["image"]
            # Redimensionne l'image de la carte à la taille maximale calculée
            card_image = pygame.transform.scale(card_image, (max_card_width, max_card_height))
            card_rect = card_image.get_rect()
            # Positionne les cartes horizontalement
            card_rect.x = 50 + i * space_between_cards
            # Positionne les cartes verticalement
            card_rect.y = SCREEN_HEIGHT - card_rect.height - 50
            screen.blit(card_image, card_rect)
    else:
        # Si la main du joueur est vide, dessine un message
        draw_text("Votre main est vide", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

def draw_discard_pile(discard_pile: list) -> None:
    # Dessine la pile de défausse sur l'écran
    if discard_pile:
        # Calcule la taille maximale pour chaque carte en fonction de l'espace disponible
        # Calcule l'espace horizontal entre les cartes
        space_between_cards = min(120, (SCREEN_WIDTH - 100))
        # Calcule la taille maximale pour chaque carte en fonction de l'espace disponible
        max_card_width = space_between_cards - 10  # 10 pixels de marge entre les cartes
        max_card_height = int(max_card_width * 1.4)  # Ratio hauteur-largeur typique pour une carte

        # Dessine la dernière carte dans pile de défausse
        card_image = discard_pile[-1]["image"]
        # Redimensionne l'image de la carte à la taille maximale calculée
        card_image = pygame.transform.scale(card_image, (max_card_width, max_card_height))
        card_rect = card_image.get_rect()
        # Positionne les cartes horizontalement
        card_rect.x = SCREEN_WIDTH  // 2
        # Positionne les cartes verticalement
        card_rect.y = SCREEN_HEIGHT // 2
        screen.blit(card_image, card_rect)
    else:
        # Si la pile de défausse est vide, dessine un message
        draw_text("Pile de défausse vide", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

def end_screen(message: str):
    screen.fill(GREEN)
    draw_text(message, font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

def play(ip_list: list, initialized_the_game: bool=True, my_hand: list=[], discard_pile: list=[]) -> None:
    if initialized_the_game and my_hand == []:
        deck: list = get_cards_from_their_names(get_card_images_names())
        hands: list = []
        shuffle(deck)
        for ip in ip_list:
            hand: list = get_my_hand(deck)
            hand_name: str = ""
            for card in hand:
                hand_name += f"{card['name']}, "
            hand_name = hand_name[:-2]
            message: str = f"{hand_name}"
            send_info(ip, message)
        my_hand: list = get_my_hand(deck)
        discard_pile.append(draw_a_card(deck))
        for ip in ip_list:
            send_info(ip, discard_pile[-1]["name"])
            
    running: bool = True
    skip_ip: bool = False
    while running:
        screen.fill(GREEN)

        draw_discard_pile(discard_pile)
        draw_my_hand(my_hand)
        pygame.display.update()

        if not initialized_the_game:
            ip, message = get_info()
            if "draw card" in message:
                print("uwu")
                cards = message.split(", ")[1:]
                cards = get_cards_from_their_names(cards)
                for card in cards:
                    my_hand.append(card)
            elif (not ("it's your turn" in message)) and (not ("won" in message)):
                discard_pile = [get_cards_from_their_names([message])[0]]
            elif "won" in message:
                end_screen(message)
            else:
                if len(my_hand) == 0:
                    send_info(ip, " won")
                card_played = do_a_turn(my_hand, discard_pile)
                
                screen.fill(GREEN)
                draw_discard_pile(discard_pile)
                draw_my_hand(my_hand)
                pygame.display.update()
                if card_played == "Piocher":
                    send_info(ip, card_played)
                else:
                    discard_pile =  [card_played]
                    send_info(ip, card_played['name'])
        else:   
            screen.fill(GREEN)
            draw_discard_pile(discard_pile)
            draw_my_hand(my_hand)
            pygame.display.update()
            
            if not skip_ip:
                if len(my_hand) == 0:
                    my_ip: str = get_my_ip()
                    for ip in ip_list:
                        send_info(ip, f"{my_ip} won")
                
                card_played = do_a_turn(my_hand, discard_pile)

                if card_played == "Piocher":
                    my_hand.append(draw_a_card(deck))
                elif "plus deux" in card_played or "plus quatre" in card_played:
                    skip_ip = True
                    if "plus deux" in card_played:
                        for i in range(2):
                            send_info(ip_list[0], "draw card, "+draw_a_card(deck)["name"])
                    else:
                        for i in range(4):
                            send_info(ip_list[0], "draw card, "+draw_a_card(deck)["name"])
                    discard_pile.append(card_played)
                    for ip in ip_list:
                        send_info(ip, card_played["name"])
                elif "changement de sens" in card_played:
                    ip_list.reverse()
                    discard_pile.append(card_played)
                    for ip in ip_list:
                        send_info(ip, card_played["name"])
                elif "interdiction de jouer" in card_played:
                    skip_ip = True
                    discard_pile.append(card_played)
                    for ip in ip_list:
                        send_info(ip, card_played["name"])
                else:
                    discard_pile.append(card_played)
                    for ip in ip_list:
                        send_info(ip, card_played["name"])
                        
                if len(deck) == 0:
                    temp = discard_pile.pop(-1)
                    deck = discard_pile[::-1]
                    discard_pile = [temp]
                    for ip in ip_list:
                        send_info(ip, discard_pile[0]["name"])
            else:
                skip_ip = False
            
            for index, ip in enumerate(ip_list):
                if len(deck) == 0:
                    temp = discard_pile.pop(-1)
                    deck = discard_pile[::-1]
                    discard_pile = [temp]
                    for ip in ip_list:
                        send_info(ip, discard_pile[0]["name"])

                if skip_ip:
                    skip_ip = False
                else:
                    send_info(ip, "it's your turn")
                    ip_r, message = get_info()
                    if message == " won":
                        message = ip_r + " " + message
                        for ip_2 in ip_list:
                            send_info(ip_2, message)
                    elif "plus deux" in message or "plus quatre" in message:
                        skip_ip = True
                        if index+1 <= len(ip_list)-1:
                            if "plus deux" in message:
                                for i in range(2):
                                    send_info(ip_list[index+1], "draw card, "+draw_a_card(deck)["name"])
                            else:
                                for i in range(4):
                                    send_info(ip_list[index+1], "draw card, "+draw_a_card(deck)["name"])
                        else:
                            if "plus deux" in message:
                                for i in range(2):
                                    my_hand.append(draw_a_card(deck))
                            else:
                                for i in range(4):
                                    my_hand.append(draw_a_card(deck))
                        discard_pile.append(get_cards_from_their_names([message])[0])
                        for ip_2 in ip_list:
                            send_info(ip_2, message)
                    elif "changement de sens" in message:
                        ip_list.reverse()
                        discard_pile.append(get_cards_from_their_names([message])[0])
                        for ip_2 in ip_list:
                            send_info(ip_2, message)
                    elif "interdiction de jouer" in message:
                        skip_ip = True
                        discard_pile.append(get_cards_from_their_names([message])[0])
                        for ip_2 in ip_list:
                            send_info(ip_2, message)
                    elif not message == "Piocher":
                        discard_pile.append(get_cards_from_their_names([message])[0])
                        for ip_2 in ip_list:
                            send_info(ip_2, message)
                    else:
                        message = "draw card, " + draw_a_card(deck)["name"]
                        send_info(ip_r, message)
                    if len(deck) == 0:
                        temp = discard_pile.pop(-1)
                        deck = discard_pile[::-1]
                        discard_pile = [temp]
                        for ip in ip_list:
                            send_info(ip, discard_pile[0]["name"])

main_menu()
pygame.quit()
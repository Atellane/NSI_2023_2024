# TODO développer la fonction play pour qu'elle prenne en charge l'envoie de cartes au prochain joueur quand un +2 est joué
import os, sys, pygame
from random import shuffle
from pygame_textinput import TextInputVisualizer

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
    my_hand: list = connection[1].rsplit(" ")
    for index_card, card in enumerate(my_hand):
        my_hand[index_card] = get_cards_from_their_names([card])[0]
    play([connection[0]], False, my_hand)

def draw_a_card(deck: list) -> dict:
    card: dict = deck.pop(0)
    return card

def is_it_my_turn() -> (bool, str):
    connection: tuple = get_info()
    if "it's your turn" == connection[1]:
        return (connection[0], True)
    else:
        return (None, False)

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

def get_cards_from_their_names(cards: list[str]) -> list:
    deck: list = []
    for card in cards:
        deck.append(create_a_card(card.replace("_", " ").replace(".png", ""), pygame.image.load(card)))
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
        draw_text("Rentrez l'ip de vos adversaires, espacez chaque ip d'un espace (max 9 ip) :", font, WHITE, SCREEN_WIDTH // 2 - 100, 50)
        button_text: str = "Attendre qu'un-e autre joueur-euse se connecte."
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

def play(ip_list: list, initialized_the_game: bool=True, my_hand: list=[]) -> None:
    discard_pile: list = []
    if initialized_the_game and my_hand == []:
        deck: list = get_cards_from_their_names(get_card_images_names())
        hands: list = []
        shuffle(deck)
        for ip in ip_list:
            hand: list = get_my_hand(deck)
            hand_name: str = ""
            for card in hand:
                hand_name += f" {card['name']}"
            hand_name = hand_name[1:]
            message: str = f"{hand_name}"
            send_info(ip, message)
        my_hand: list = get_my_hand(deck)
    running: bool = True
    while running:
        screen.fill(GREEN)

        if not initialized_the_game:
            ip, message = get_info()
            if (not (message == "it's your turn")) and  (not ("won" in message)):
                if "draw card" in message:
                    cards = message.split(", ")[:1]
                    cards = get_cards_from_their_names(cards)
                    for card in cards:
                        my_hand.append(card)
                else:
                    discard_pile = [get_cards_from_their_names([message])[0]]
            elif "won" in message:
                end_screen(message)
            else:
                card_played = do_a_turn()
                if len(my_hand) == 0:
                    send_info(ip, " won")
                if card_played == None:
                    send_info(ip, card_played)
                    card: str = get_info()[1]
                    my_hand.append(get_cards_from_their_names([card])[0])
                else:
                    discard_pile =  [card_played]
                    send_info(ip, card_played['name'])
        else:
            card_played = do_a_turn()
            if not (card_played == None):
                discard_pile.append(card_played)
            else:
                my_hand.append(draw_a_card(deck))
            
            if len(deck) == 0:
                temp = discard_pile.pop(-1)
                deck = discard_pile[::-1]
                discard_pile = [temp]
                for ip in ip_list:
                    send_info(ip, discard_pile[0]["name"])

            for index, ip in enumerate(ip_list):
                send_info(ip, "it's your turn")
                ip_r, message: str = get_info()
                if message == " won":
                    message = ip_r + message
                    for ip_2 in ip_list:
                        send_info(ip_2, message)
                elif not message == None:
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
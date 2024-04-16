import sys, pygame
from pygame_textinput import TextInputVisualizer

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paramètres de la fenêtre
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

# Font pour le texte
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def get_ip():
    running = True
    text_input = TextInputVisualizer()

    while running:
        screen.fill(BLACK)  # Définir l'arrière-plan en noir
        draw_text("Rentrez l'ip de vos adversaires, espacez chaque ip d'un espace (max 9 ip) :", font, WHITE, SCREEN_WIDTH // 2 - 100, 50)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Récupérer l'adresse IP saisie par l'utilisateur
                    ip_address = text_input.value
                    return ip_address  # Retourner l'adresse IP saisie par l'utilisateur
                    # Réinitialiser la saisie
                    text_input.clear_text()
        
        # Mettre à jour la saisie de texte
        text_input.update(events)
        # Récupérer la surface de la saisie de texte
        text_surface = text_input.surface
        # Créer une surface pour l'arrière-plan blanc de la zone de texte
        text_background = pygame.Surface((text_surface.get_width(), text_surface.get_height()))
        text_background.fill(WHITE)
        # Afficher l'arrière-plan blanc de la zone de texte sur l'écran
        screen.blit(text_background, (SCREEN_WIDTH // 2 - 100, 150))
        # Afficher la saisie de texte sur l'écran par-dessus l'arrière-plan blanc
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - 100, 150))

        pygame.display.update()
        pygame.time.Clock().tick(30)

def main_menu():
    running = True
    while running:
        screen.fill(BLACK)
        draw_text("Menu Principal", font, WHITE, SCREEN_WIDTH // 2, 50)
        
        mx, my = pygame.mouse.get_pos()

        button_1_text = "Commencer une partie"
        button_2_text = "Quitter"
        button_width_1 = font.size(button_1_text)[0] + 20  # Ajoutez un padding de 20 pixels
        button_height_1 = font.size(button_1_text)[1] + 20  # Ajoutez un padding de 20 pixels
        button_x_1 = (SCREEN_WIDTH - button_width_1) // 2
        button_width_2 = font.size(button_2_text)[0] + 20  # Ajoutez un padding de 20 pixels
        button_height_2 = font.size(button_2_text)[1] + 20  # Ajoutez un padding de 20 pixels
        button_x_2 = (SCREEN_WIDTH - button_width_2) // 2

        button_1 = pygame.Rect(button_x_1, 150, button_width_1, button_height_1)
        button_2 = pygame.Rect(button_x_2, 250, button_width_2, button_height_2)
        if button_1.collidepoint((mx, my)):
            if click:
                ip_address = get_ip()
                print(f"L'/Les adresse-s ip renseignée-s est/sont \"{ip_address}\".")
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (0, 255, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        draw_text(button_1_text, font, BLACK, button_x_1 + button_width_1 // 2, 150 + button_height_1 // 2)
        draw_text(button_2_text, font, BLACK, button_x_2 + button_width_2 // 2, 250 + button_height_2 // 2)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        pygame.time.Clock().tick(60)

main_menu()
pygame.quit()

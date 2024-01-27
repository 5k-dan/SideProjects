import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kung Fu Fighter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load player character image
player_image = pygame.image.load("player_character.png").convert_alpha()
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 4, HEIGHT // 2)

# Load opponent character image
opponent_image = pygame.image.load("opponent_character.png").convert_alpha()
opponent_rect = opponent_image.get_rect()
opponent_rect.center = (3 * WIDTH // 4, HEIGHT // 2)

# Load fireball image
fireball_image = pygame.image.load("fireball.png").convert_alpha()
fireball_rect = fireball_image.get_rect()
fireball_rect.center = (0, 0)  # Initial position outside the screen

# Load earth wall image
earth_wall_image = pygame.image.load("earth_wall.png").convert_alpha()
earth_wall_rect = earth_wall_image.get_rect()
earth_wall_rect.center = (-100, -100)  # Initial position outside the screen

# Player movement speed
player_speed = 3

# Fireball and earth wall speed
skill_speed = 5

# Health
player_health = 100
opponent_health = 100

# Fonts
font = pygame.font.SysFont(None, 40)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player 1 movement controls (WASD)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed

    # Player 2 movement (controlled by CPU)
    # Ensure opponent moves away from the player
    if player_rect.x < opponent_rect.x:
        opponent_rect.x += player_speed // 2
    elif player_rect.x > opponent_rect.x:
        opponent_rect.x -= player_speed // 2
    if player_rect.y < opponent_rect.y:
        opponent_rect.y += player_speed // 2
    elif player_rect.y > opponent_rect.y:
        opponent_rect.y -= player_speed // 2

    # Boundary checking to keep players within the screen
    player_rect.x = max(0, min(WIDTH - player_rect.width, player_rect.x))
    player_rect.y = max(0, min(HEIGHT - player_rect.height, player_rect.y))
    opponent_rect.x = max(0, min(WIDTH - opponent_rect.width, opponent_rect.x))
    opponent_rect.y = max(0, min(HEIGHT - opponent_rect.height, opponent_rect.y))

    # Player 1 skills
    if keys[pygame.K_r]:
        # Shoot fireball
        fireball_rect.center = player_rect.center

    if keys[pygame.K_t]:
        # Summon earth wall
        earth_wall_rect.center = player_rect.center

    # Update fireball and earth wall positions
    if fireball_rect.centerx > 0:
        fireball_rect.x += skill_speed
        # Check collision with opponent
        if fireball_rect.colliderect(opponent_rect):
            opponent_health -= 10  # Decrease opponent health on hit
            fireball_rect.center = (0, 0)  # Reset fireball position
            if opponent_health <= 0:
                # Opponent defeated
                text = font.render("Duke WINS!!", True, GREEN)
                screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
                pygame.display.update()
                pygame.time.delay(2000)  # Display message for 2 seconds
                pygame.quit()
                sys.exit()

    if earth_wall_rect.centerx > 0:
        # Check collision with fireball
        if fireball_rect.colliderect(earth_wall_rect):
            fireball_rect.center = (0, 0)  # Destroy fireball
        # Check collision with player
        if player_rect.colliderect(earth_wall_rect):
            player_health -= 5  # Decrease player health if attacked while wall is up
            if player_health <= 0:
                # Player defeated
                text = font.render("Duke LOSES!!", True, RED)
                screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
                pygame.display.update()
                pygame.time.delay(2000)  # Display message for 2 seconds
                pygame.quit()
                sys.exit()

    # Draw health bars
    pygame.draw.rect(screen, RED, (20, 20, player_health, 20))
    pygame.draw.rect(screen, RED, (WIDTH - 220, 20, opponent_health, 20))

    # Clear the screen
    screen.fill(WHITE)

    # Draw players and skills
    screen.blit(player_image, player_rect)
    screen.blit(opponent_image, opponent_rect)
    if fireball_rect.centerx > 0:
        screen.blit(fireball_image, fireball_rect)
    if earth_wall_rect.centerx > 0:
        screen.blit(earth_wall_image, earth_wall_rect)

    # Update the display
    pygame.display.update()

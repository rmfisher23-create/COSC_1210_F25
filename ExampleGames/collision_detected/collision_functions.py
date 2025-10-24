# c4_functions.py
import os
import pygame
import config_c4

def draw_circle(screen, x, y, num):
    """Draw sprite centered at (x, y); fall back to circle if no image."""
    if num == 1:
        pygame.draw.circle(screen, config_c4.PLAYER_COLOR1, (int(x), int(y)), config_c4.PLAYER_RADIUS)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), config_c4.PLAYER_RADIUS, 2)
    else:
         pygame.draw.circle(screen, config_c4.PLAYER_COLOR2, (int(x), int(y)), config_c4.PLAYER_RADIUS)
         pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), config_c4.PLAYER_RADIUS, 2)


def show_game_over(screen):
    """Draw a Game Over box in the center of the screen."""
    font = pygame.font.Font(None, 72)  # default font, large size
    text = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = text.get_rect(center=(config_c4.WIDTH // 2, config_c4.HEIGHT // 2))

    # Draw a semi-transparent dark box behind the text
    box_width = text_rect.width + 40
    box_height = text_rect.height + 40
    box_surface = pygame.Surface((box_width, box_height))
    box_surface.set_alpha(180)  # transparency
    box_surface.fill((0, 0, 0))
    box_rect = box_surface.get_rect(center=text_rect.center)

    # Blit box then text
    screen.blit(box_surface, box_rect)
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Pause to let player see the message
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False


                

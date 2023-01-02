import pygame

WIDTH, HEIGHT = 1000, 1000

pygame.init()
pygame.display.set_caption("Planet Simulation")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont("comicsans", 16)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
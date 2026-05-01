import pygame

pygame.init()
pygame.display.set_caption("Planet Simulation")

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = WIN.get_size()

PLANET_RADIUS_SCALE = 0.6
MIN_PLANET_RADIUS = 2

FONT = pygame.font.SysFont("comicsans", 16)

COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "YELLOW": (255, 255, 0),
    "BLUE": (100, 149, 237),
    "RED": (188, 39, 50),
    "DARK_GREY": (80, 78, 81),
    "ORANGE": (255, 165, 0),
    "LIGHT_BROWN": (210, 180, 140),
    "LIGHT_BLUE": (173, 216, 230),
    "LIGHT_CYAN": (224, 255, 255),
    "LIGHT_GREY": (211, 211, 211)
}

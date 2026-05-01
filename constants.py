import pygame
from Planet import Planet

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

sun = Planet(
        name="Sun", 
        x=0, 
        y=0, 
        radius=30, 
        color=COLORS.get("YELLOW"), 
        mass=1.98892 * 10**30
    )
sun.isSun = True

mercury = Planet(
        name="Mercury", 
        x=0.387 * Planet.AU, 
        y=0, 
        radius=8, 
        color=COLORS.get("DARK_GREY"), 
        mass=0.330 * 10**24
    )
mercury.y_vel = -47.4 * 1000

venus = Planet(
        name="Venus", 
        x=0.723 * Planet.AU, 
        y=0, 
        radius=14, 
        color=COLORS.get("WHITE"), 
        mass=4.8685 * 10**24
    )
venus.y_vel = -35.02 * 1000

earth = Planet(
        name="Earth", 
        x=-1 * Planet.AU, 
        y=0, 
        radius=16, 
        color=COLORS.get("BLUE"), 
        mass=5.9742 * 10**24
    )
earth.y_vel = 29.783 * 1000

mars = Planet(
        name="Mars", 
        x=-1.524 * Planet.AU, 
        y=0, 
        radius=12, 
        color=COLORS.get("RED"), 
        mass=0.639 * 10**24
    )
mars.y_vel = 24.077 * 1000

asteroid_belt = Planet(
        name="Asteroid Belt", 
        x=-2.8 * Planet.AU, 
        y=0, 
        radius=10, 
        color=COLORS.get("LIGHT_GREY"), 
        mass=0.0001 * 10**24
    )
asteroid_belt.y_vel = 17.88 * 1000

jupiter = Planet(
        name="Jupiter", 
        x=-5.203 * Planet.AU, 
        y=0, 
        radius=20, 
        color=COLORS.get("ORANGE"), 
        mass=1898 * 10**24
    )
jupiter.y_vel = 13.06 * 1000

saturn = Planet(
        name="Saturn", 
        x=-9.539 * Planet.AU, 
        y=0, 
        radius=18, 
        color=COLORS.get("LIGHT_BROWN"), 
        mass=568 * 10**24
    )
saturn.y_vel = 9.69 * 1000

neptune = Planet(
        name="Neptune", 
        x=-30.06 * Planet.AU, 
        y=0, 
        radius=18, 
        color=COLORS.get("LIGHT_BLUE"), 
        mass=102 * 10**24
    )
neptune.y_vel = 5.43 * 1000

uranus = Planet(
        name="Uranus", 
        x=-19.18 * Planet.AU, 
        y=0, 
        radius=18, 
        color=COLORS.get("LIGHT_CYAN"), 
        mass=86.8 * 10**24
    )
uranus.y_vel = 6.81 * 1000

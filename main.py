import pygame

from display_config import COLORS, WIN
from simulation_constants import INITIAL_ZOOM, MAX_ZOOM, MIN_ZOOM, ZOOM_STEP
from solar_system import all_bodies, sun


def main():
    run = True
    clock = pygame.time.Clock()
    zoom = INITIAL_ZOOM

    planets = all_bodies

    while run:
        clock.tick(60)
        WIN.fill(COLORS.get("BLACK"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0: # scroll up
                    zoom = min(MAX_ZOOM, zoom + ZOOM_STEP)
                elif event.y < 0: # scroll down
                    zoom = max(MIN_ZOOM, zoom - ZOOM_STEP)

        for planet in planets:
            planet.update_position(planets)

        center_x, center_y = (sun.x, sun.y)
        for planet in planets:
            if not planet.isSun:
                planet.draw(WIN, center_x, center_y, zoom)

        # Draw the sun last to ensure it remains on top of other planets.
        sun.draw(WIN, center_x, center_y, zoom)
        pygame.display.update()


main()

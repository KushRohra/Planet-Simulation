from Planet import Planet
from constants import *

def main():
    run = True
    clock = pygame.time.Clock()
    zoom = 10.0
    min_zoom = 0.08
    max_zoom = 20.0

    sun = Planet("Sun", 0, 0, 30, COLORS.get("YELLOW"), 1.98892 * 10**30)
    sun.isSun = True

    mercury = Planet("Mercury", 0.387 * Planet.AU, 0, 8, COLORS.get("DARK_GREY"), 0.330 * 10**24)
    mercury.y_vel = -47.4 * 1000

    venus = Planet("Venus", 0.723 * Planet.AU, 0, 14, COLORS.get("WHITE"), 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    earth = Planet("Earth", -1 * Planet.AU, 0, 16, COLORS.get("BLUE"), 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000

    mars = Planet("Mars", -1.524 * Planet.AU, 0, 12, COLORS.get("RED"), 0.639 * 10**24)
    mars.y_vel = 24.077 * 1000

    jupiter = Planet("Jupiter", -5.203 * Planet.AU, 0, 20, COLORS.get("ORANGE"), 1898 * 10**24)
    jupiter.y_vel = 13.06 * 1000

    saturn = Planet("Saturn", -9.539 * Planet.AU, 0, 18, COLORS.get("LIGHT_BROWN"), 568 * 10**24)
    saturn.y_vel = 9.69 * 1000

    neptune = Planet("Neptune", -30.06 * Planet.AU, 0, 18, COLORS.get("LIGHT_BLUE"), 102 * 10**24)
    neptune.y_vel = 5.43 * 1000

    uranus = Planet("Uranus", -19.18 * Planet.AU, 0, 18, COLORS.get("LIGHT_CYAN"), 86.8 * 10**24)
    uranus.y_vel = 6.81 * 1000

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, neptune, uranus]

    while run:
        clock.tick(60)
        WIN.fill(COLORS.get("BLACK"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: # scroll up
                    zoom = min(max_zoom, zoom + 0.1)
                elif event.button == 5: # scroll down
                    zoom = max(min_zoom, zoom - 0.1)
            
        for planet in planets:
            planet.update_position(planets)

        center_x, center_y = sun.x, sun.y
        for planet in planets:
            planet.draw(WIN, center_x, center_y, zoom)
        pygame.display.update()
    

main()
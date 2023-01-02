from Planet import Planet
from constants import *

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.isSun = True

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 0.330 * 10**24)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 0.639 * 10**24)
    mars.y_vel = 24.077 * 1000

    planets = [sun, mercury, venus, earth, mars]

    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
 
        pygame.display.update()
    
    pygame.quit()

main()
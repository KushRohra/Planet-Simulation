from constants import *

def main():
    run = True
    clock = pygame.time.Clock()
    zoom = 10.0
    min_zoom = 0.08
    max_zoom = 20.0

    planets = [sun, mercury, venus, earth, mars, asteroid, jupiter, saturn, neptune, uranus, pluto]

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
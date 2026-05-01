import math
import pygame

from display_config import WIDTH, HEIGHT, PLANET_RADIUS_SCALE, MIN_PLANET_RADIUS, FONT, COLORS

class Planet:
    AU = 149.6e6 * 1000 # distance in meters
    G = 6.67428e-11
    SCALE = (min(WIDTH, HEIGHT) * 0.42) / (30.06 * AU)
    TIMESTEP = 3600 * 24 * 1 # 1 day
    
    def __init__(self, name, x, y, radius, color, mass, image = None):
        self.x = x
        self.y = y
        self.name = name
        scaled_radius = int(radius * PLANET_RADIUS_SCALE)
        self.radius = scaled_radius if scaled_radius >= MIN_PLANET_RADIUS else MIN_PLANET_RADIUS
        self.color = color
        self.mass = mass
        self.image = image
        self.scaled_image = None

        if self.image is not None:
            image_size = max(2, self.radius * 2) * 2
            self.scaled_image = pygame.transform.smoothscale(self.image, (image_size, image_size))
            print(f"For planet name: {self.name}, original radius: {radius}, scaled radius: {self.radius}, image size: {image_size}")

        self.orbit = []
        self.isSun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def scaleDistance(self, dimension, zoom):
        return dimension * self.SCALE * zoom

    def draw(self, win, center_x, center_y, zoom):
        x = self.scaleDistance(self.x - center_x, zoom) + WIDTH / 2
        y = self.scaleDistance(self.y - center_y, zoom) + HEIGHT / 2
        center_pos = (int(x), int(y))

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                orbit_x, orbit_y = point
                orbit_x = self.scaleDistance(orbit_x - center_x, zoom) + WIDTH / 2
                orbit_y = self.scaleDistance(orbit_y - center_y, zoom) + HEIGHT / 2
                updated_points.append((orbit_x, orbit_y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        if not self.isSun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, COLORS.get("WHITE"))
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
            planet_name_text = FONT.render(self.name, 1, COLORS.get("WHITE"))
            win.blit(planet_name_text, (x - distance_text.get_width()/2, y - distance_text.get_height()))

        if self.scaled_image is not None:
            image_rect = self.scaled_image.get_rect(center=center_pos)
            win.blit(self.scaled_image, image_rect)
        else:
            pygame.draw.circle(win, self.color, center_pos, self.radius)

    def forceOfAttractionBetweenPlanets(self, other):
        otherX, otherY = other.x, other.y
        selfX, selfY = self.x, self.y
        distanceX = otherX - selfX
        distanceY = otherY  - selfY
        distance = math.sqrt(distanceX ** 2 + distanceY ** 2)

        if other.isSun:
            self.distance_to_sun = distance

        force = (self.G * self.mass * other.mass) / (distance ** 2)
        theta = math.atan2(distanceY, distanceX)
        forceY = math.sin(theta) * force
        forceX = math.cos(theta) * force

        return forceX, forceY

    def update_position(self, planets):
        totalFx = totalFy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.forceOfAttractionBetweenPlanets(planet)
            totalFx += fx
            totalFy += fy
        
        self.x_vel += totalFx / self.mass * self.TIMESTEP
        self.y_vel += totalFy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

from constants import *
import math

class Planet:
    AU = 149.6e6 * 1000 # distance in meters
    G = 6.67428e-11
    SCALE = (min(WIDTH, HEIGHT) * 0.42) / (30.06 * AU)
    TIMESTEP = 3600 * 24 * 7 # 7 days
    
    def __init__(self, name, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.name = name
        scaled_radius = int(radius * PLANET_RADIUS_SCALE)
        self.radius = scaled_radius if scaled_radius >= MIN_PLANET_RADIUS else MIN_PLANET_RADIUS
        self.color = color
        self.mass = mass

        self.orbit = []
        self.isSun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def scaleDistance(self, dimension):
        return dimension * self.SCALE

    def draw(self, win):
        x = self.scaleDistance(self.x) + WIDTH / 2
        y = self.scaleDistance(self.y) + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        if not self.isSun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, COLORS.get("WHITE"))
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
            planet_name_text = FONT.render(self.name, 1, COLORS.get("WHITE"))
            win.blit(planet_name_text, (x - distance_text.get_width()/2, y - distance_text.get_height()))

        pygame.draw.circle(win, self.color, (x, y), self.radius)

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

from display_config import *
from Planet import Planet
from utils import load_image_for_planet

sun = Planet(
        name="Sun", 
        x=0, 
        y=0, 
        radius=30, 
        color=COLORS.get("YELLOW"), 
        mass=1.98892 * 10**30,
        image=load_image_for_planet("Sun", "./images/sun.jpeg")
    )
sun.isSun = True

mercury = Planet(
        name="Mercury", 
        x=0.387 * Planet.AU, 
        y=0, 
        radius=8, 
        color=COLORS.get("DARK_GREY"), 
        mass=0.330 * 10**24,
        image=load_image_for_planet("Mercury", "./images/mercury.jpeg")
    )
mercury.y_vel = -47.4 * 1000

venus = Planet(
        name="Venus", 
        x=0.723 * Planet.AU, 
        y=0, 
        radius=14, 
        color=COLORS.get("WHITE"), 
        mass=4.8685 * 10**24,
        image=load_image_for_planet("Venus", "./images/venus.jpeg")
    )
venus.y_vel = -35.02 * 1000

earth = Planet(
        name="Earth", 
        x=-1 * Planet.AU, 
        y=0, 
        radius=16, 
        color=COLORS.get("BLUE"), 
        mass=5.9742 * 10**24,
        image=load_image_for_planet("Earth", "./images/earth.jpeg")
    )
earth.y_vel = 29.783 * 1000

mars = Planet(
        name="Mars", 
        x=-1.524 * Planet.AU, 
        y=0, 
        radius=12, 
        color=COLORS.get("RED"), 
        mass=0.639 * 10**24,
        image=load_image_for_planet("Mars", "./images/mars.jpeg")
    )
mars.y_vel = 24.077 * 1000

asteroid = Planet(
        name="Asteroid", 
        x=-2.8 * Planet.AU, 
        y=0, 
        radius=10, 
        color=COLORS.get("LIGHT_GREY"), 
        mass=0.0001 * 10**24,
        image=load_image_for_planet("Asteroid", "./images/asteroid.jpeg")
    )
asteroid.y_vel = 17.88 * 1000

jupiter = Planet(
        name="Jupiter", 
        x=-5.203 * Planet.AU, 
        y=0, 
        radius=20, 
        color=COLORS.get("ORANGE"), 
        mass=1898 * 10**24,
        image=load_image_for_planet("Jupiter", "./images/jupiter.jpeg")
    )
jupiter.y_vel = 13.06 * 1000

saturn = Planet(
        name="Saturn", 
        x=-9.539 * Planet.AU, 
        y=0, 
        radius=18, 
        color=COLORS.get("LIGHT_BROWN"), 
        mass=568 * 10**24,
        image=load_image_for_planet("Saturn", "./images/saturn.jpeg")
    )
saturn.y_vel = 9.69 * 1000

neptune = Planet(
        name="Neptune", 
        x=-30.06 * Planet.AU, 
        y=0, 
        radius=18, 
        color=COLORS.get("LIGHT_BLUE"), 
        mass=102 * 10**24,
        image=load_image_for_planet("Neptune", "./images/neptune.jpeg")
    )
neptune.y_vel = 5.43 * 1000

uranus = Planet(
        name="Uranus", 
        x=-19.18 * Planet.AU, 
        y=0, 
        radius=18, 
        color=COLORS.get("LIGHT_CYAN"), 
        mass=86.8 * 10**24,
        image=load_image_for_planet("Uranus", "./images/uranus.jpeg")
    )
uranus.y_vel = 6.81 * 1000

pluto = Planet(
        name="Pluto", 
        x=-39.48 * Planet.AU, 
        y=0, 
        radius=10, 
        color=COLORS.get("LIGHT_GREY"), 
        mass=0.013 * 10**24,
        image=load_image_for_planet("Pluto", "./images/pluto.jpeg")
    )
pluto.y_vel = 4.74 * 1000

# Balance initial linear momentum so the Sun does not drift away from the system.
orbiting_bodies = [mercury, venus, earth, mars, asteroid, jupiter, saturn, neptune, uranus, pluto]
total_px = sum(body.mass * body.x_vel for body in orbiting_bodies)
total_py = sum(body.mass * body.y_vel for body in orbiting_bodies)
sun.x_vel = -total_px / sun.mass
sun.y_vel = -total_py / sun.mass

# Add a shared drift velocity to move the full solar system together through space.
SOLAR_SYSTEM_DRIFT_VX = 0
SOLAR_SYSTEM_DRIFT_VY = 230 * 1000

all_bodies = [sun] + orbiting_bodies
for body in all_bodies:
    body.x_vel += SOLAR_SYSTEM_DRIFT_VX
    body.y_vel += SOLAR_SYSTEM_DRIFT_VY
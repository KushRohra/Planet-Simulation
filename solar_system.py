import math
import random

from Planet import Planet
from display_config import COLORS
from simulation_constants import (
    ASTEROID_COUNT,
    ASTEROID_MASS_RANGE,
    ASTEROID_NAME_PREFIX,
    ASTEROID_ORBITAL_RADIUS_RANGE_AU,
    ASTEROID_RADIUS_RANGE,
    ASTEROID_SPEED_VARIATION,
    EARTH_NAME,
    JUPITER_NAME,
    MARS_NAME,
    MERCURY_NAME,
    NEPTUNE_NAME,
    OUTER_PLANET_NAMES,
    PLANET_IMAGE_PATHS,
    PLUTO_NAME,
    SATURN_NAME,
    SOLAR_SYSTEM_DRIFT_VX,
    SOLAR_SYSTEM_DRIFT_VY,
    SUN_NAME,
    URANUS_NAME,
    VENUS_NAME,
)
from utils import load_image_for_planet

# name, orbital_radius_in_AU, visual_radius, color_key, mass_kg, initial_y_velocity_mps
PLANET_SPECS = [
    (MERCURY_NAME, 0.387, 8, "DARK_GREY", 0.330 * 10**24, -47.4 * 1000),
    (VENUS_NAME, 0.723, 14, "WHITE", 4.8685 * 10**24, -35.02 * 1000),
    (EARTH_NAME, -1.0, 16, "BLUE", 5.9742 * 10**24, 29.783 * 1000),
    (MARS_NAME, -1.524, 12, "RED", 0.639 * 10**24, 24.077 * 1000),
    (JUPITER_NAME, -5.203, 20, "ORANGE", 1898 * 10**24, 13.06 * 1000),
    (SATURN_NAME, -9.539, 18, "LIGHT_BROWN", 568 * 10**24, 9.69 * 1000),
    (NEPTUNE_NAME, -30.06, 18, "LIGHT_BLUE", 102 * 10**24, 5.43 * 1000),
    (URANUS_NAME, -19.18, 18, "LIGHT_CYAN", 86.8 * 10**24, 6.81 * 1000),
    (PLUTO_NAME, -39.48, 10, "LIGHT_GREY", 0.013 * 10**24, 4.74 * 1000),
]


def _create_planet(name, x, y, radius, color_key, mass):
    return Planet(
        name=name,
        x=x,
        y=y,
        radius=radius,
        color=COLORS.get(color_key),
        mass=mass,
        image=load_image_for_planet(name, PLANET_IMAGE_PATHS[name]),
    )


def _create_asteroid(name, x, y, radius, mass):
    return Planet(
        name=name,
        x=x,
        y=y,
        radius=radius,
        color=COLORS.get("LIGHT_GREY"),
        mass=mass,
        image=load_image_for_planet(name, PLANET_IMAGE_PATHS[ASTEROID_NAME_PREFIX]),
    )


def build_solar_system():
    sun = _create_planet(SUN_NAME, 0, 0, 30, "YELLOW", 1.98892 * 10**30)
    sun.isSun = True

    major_planets = []
    for name, orbital_radius_au, radius, color_key, mass, initial_y_vel in PLANET_SPECS:
        planet = _create_planet(name, orbital_radius_au * Planet.AU, 0, radius, color_key, mass)
        planet.y_vel = initial_y_vel
        major_planets.append(planet)

    planet_by_name = {planet.name: planet for planet in major_planets}

    asteroid_belt = []
    min_orbit_au, max_orbit_au = ASTEROID_ORBITAL_RADIUS_RANGE_AU
    min_radius, max_radius = ASTEROID_RADIUS_RANGE
    min_mass, max_mass = ASTEROID_MASS_RANGE
    min_speed_factor, max_speed_factor = ASTEROID_SPEED_VARIATION

    for i in range(ASTEROID_COUNT):
        orbital_radius = random.uniform(min_orbit_au, max_orbit_au) * Planet.AU
        theta = random.uniform(0, 2 * math.pi)

        asteroid_x = orbital_radius * math.cos(theta)
        asteroid_y = orbital_radius * math.sin(theta)

        circular_speed = math.sqrt(Planet.G * sun.mass / orbital_radius)
        speed = circular_speed * random.uniform(min_speed_factor, max_speed_factor)

        asteroid_name = f"{ASTEROID_NAME_PREFIX}_{i}"
        asteroid = _create_asteroid(
            asteroid_name,
            asteroid_x,
            asteroid_y,
            random.randint(min_radius, max_radius),
            random.uniform(min_mass, max_mass),
        )
        asteroid.x_vel = -speed * math.sin(theta)
        asteroid.y_vel = speed * math.cos(theta)
        asteroid.is_asteroid = True
        asteroid_belt.append(asteroid)

    inner_planets = [planet_by_name[name] for name in (MERCURY_NAME, VENUS_NAME, EARTH_NAME, MARS_NAME)]
    outer_planets = [planet_by_name[name] for name in OUTER_PLANET_NAMES]

    orbiting_bodies = inner_planets + asteroid_belt + outer_planets

    total_px = sum(body.mass * body.x_vel for body in orbiting_bodies)
    total_py = sum(body.mass * body.y_vel for body in orbiting_bodies)
    sun.x_vel = -total_px / sun.mass
    sun.y_vel = -total_py / sun.mass

    all_bodies = [sun] + orbiting_bodies
    for body in all_bodies:
        body.x_vel += SOLAR_SYSTEM_DRIFT_VX
        body.y_vel += SOLAR_SYSTEM_DRIFT_VY

    return {
        "sun": sun,
        "inner_planets": inner_planets,
        "outer_planets": outer_planets,
        "asteroid_belt": asteroid_belt,
        "orbiting_bodies": orbiting_bodies,
        "all_bodies": all_bodies,
    }


SOLAR_SYSTEM = build_solar_system()

sun = SOLAR_SYSTEM["sun"]
inner_planets = SOLAR_SYSTEM["inner_planets"]
outer_planets = SOLAR_SYSTEM["outer_planets"]
asteroid_belt = SOLAR_SYSTEM["asteroid_belt"]
orbiting_bodies = SOLAR_SYSTEM["orbiting_bodies"]
all_bodies = SOLAR_SYSTEM["all_bodies"]

# Compatibility aliases for existing imports.
mercury, venus, earth, mars = inner_planets
jupiter, saturn, neptune, uranus, pluto = outer_planets

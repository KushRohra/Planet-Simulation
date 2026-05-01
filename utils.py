import pygame

def load_image_for_planet(planet_name, image_path):
    try:
        return pygame.image.load(image_path)
        # return pygame.transform.scale(image, size)
    except Exception as e:
        print(f"Error loading image for {planet_name}: {e}")
        return None
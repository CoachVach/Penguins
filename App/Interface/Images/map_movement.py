import pygame


def move_map_with_keys(keys, map):
    if keys[pygame.K_UP]:
        map.y += 1
    elif keys[pygame.K_DOWN]:
        map.y -= 1
    elif keys[pygame.K_LEFT]:
        map.x += 1
    elif keys[pygame.K_RIGHT]:
        map.x -= 1
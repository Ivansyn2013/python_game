import pygame, controls
from gun import Gun
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption('Space defeance')
    bg_color = (255, 255, 255)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update_screen(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets)



run()

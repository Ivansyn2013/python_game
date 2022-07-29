import pygame
import sys
from bulletts import Bullet

def events(screen,gun,bullets):
    """ take events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # move right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
        #move left
            if event.key == pygame.K_LEFT:
                gun.mleft = True
            #bullet start
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)


        elif event.type == pygame.KEYUP:
            #movee right
            if event.key == pygame.K_RIGHT:
                gun.mright = False
                #move left
            if event.key == pygame.K_LEFT:
                gun.mleft = False

def update_screen (bg_color, screen, gun, bullets):
    ''' update of screnn and gun'''
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

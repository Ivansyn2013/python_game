import pygame
import sys

def events(gun):
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


        #move rigth
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            if event.key == pygame.K_LEFT:
                gun.mleft = False



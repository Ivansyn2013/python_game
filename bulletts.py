import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        ''' create bullet in gun place'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,5,5)
        self.color = 0,0,0
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)


    def update(self):
        ''' move bullet up'''

        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw bullet'''

        pygame.draw.rect(self.screen, self.color, self.rect)



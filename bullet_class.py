import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load,velocity,weight,dmg):
        super().__init__()
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.v = velocity
        self.weight = weight
        self.dmg = dmg

    def move(self):
        self.rect.x += self.v[0]
        self.rect.y += self.v[1]
        self.v[1]-= self.weight

    def hit_check(self,targets):
        for t in targets:
            if self.collideobjects(t):
                return t
        self.kill()
import pygame,math

class Sword(pygame.sprite.Sprite):
    '''
    def __init__(self, startX,startY,width,height,image_load):
        super().__init__()
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.surf = pygame.surface(width,height)
    '''
        
    def __init__(self,player,width,height,image_load):
            super(Sword, self).__init__()
            self.surf = pygame.transform.smoothscale(image_load.convert(), (width, height))
            self.rect = self.surf.get_rect(center=(player.rect.x, player.rect.y))
            self.angle = 0
            self.change_angle = 0

    # THE MAIN ROTATE FUNCTION
    def process(self,player):
        self.rect.x = player.rect.x + player.rect.width
        self.rect.y = player.rect.y + player.rect.height/2
        mousePos = pygame.mouse.get_pos()
        run = (self.rect.x + mousePos[0])/2  
        rise = (self.rect.y + mousePos[1])/2
        if rise != 0:
            self.angle = math.atan(run/rise)
            
        self.surf = pygame.transform.rotate(self.surf, self.angle)
        self.rect = self.surf.get_rect(center=self.rect.center)

'''
    # Move for keypresses
    def move(self, li):
        self.change_angle = 0
        if li[K_LEFT]:
            self.change_angle = 10
        elif li[K_RIGHT]:
            self.change_angle = -10
        self.rot()
'''

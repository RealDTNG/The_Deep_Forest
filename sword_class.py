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
            self.img = image_load.convert_alpha()
            self.img = pygame.transform.scale(self.img, (width, height))
            self.angle = 50
            self.change_angle = 0
            self.w = width
            self.h = height

    def update(self,player,screen):#fix sword rotation logic
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > player.rect.x + player.rect.width/2: 
            self.x = player.rect.x + player.rect.width
        else:
            self.x = player.rect.x
        self.y = player.rect.y + player.rect.height/2
        self.origin=[self.x,self.y]
        
        run = self.x - mousePos[0]
        rise = self.y - mousePos[1]
        if run != 0:
            self.angle = -math.degrees(math.atan(rise/run))+90
            if mousePos[0] < player.rect.x + player.rect.width/2:
                self.angle += 180
                if run <= 0:
                     self.angle -= self.angle
            elif run > 0:
                 self.angle -= self.angle
        print(self.angle)
        image_rect = self.img.get_rect(topleft = (self.origin[0] , self.origin[1]))
        offset_center_to_pivot = pygame.math.Vector2(self.origin) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)
        rotated_image_center = (self.origin[0] - rotated_offset.x, self.origin[1] - rotated_offset.y)
        self.image = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.image.get_rect(center = rotated_image_center)
        screen.blit(self.image, self.rect)

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

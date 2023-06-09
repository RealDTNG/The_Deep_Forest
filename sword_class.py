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
        
    def __init__(self,width,height,image_load,slash_width,slash_height,image_stab,damage):
            super(Sword, self).__init__()
            self.surf = pygame.transform.smoothscale(image_load.convert(), (width, height))
            self.img = image_load.convert_alpha()
            self.img = pygame.transform.scale(self.img, (width, height))
            self.imgstab = image_stab.convert_alpha()
            self.imgstab = pygame.transform.scale(self.imgstab, (slash_width, slash_height))
            self.fliped_img = pygame.transform.flip(self.img, True, False)
            self.fliped_stab = pygame.transform.flip(self.imgstab, True, False)
            self.angle = 50
            self.stab = False
            self.stabtime = 0
            self.stab_CD = 0
            self.dmg = damage
            self.w = width
            self.h = height

    def update(self,player):
        if self.stabtime > 0:
            self.stabtime -= 1
        else:
            self.stab = False

        if pygame.mouse.get_pressed(num_buttons=3)[0] and self.stab_CD < 0 :
            self.stab = True
            self.stabtime = 10
            self.stab_CD = 40
            self.stabangle = self.angle
        self.stab_CD -= 1
        
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > player.rect.x + player.rect.width/2: 
            self.x = player.rect.x + player.rect.width*(11/12)
        else:
            self.x = player.rect.x + player.rect.width*(1/12)
        self.y = player.rect.y + player.rect.height*(8/15)
        self.origin=[self.x,self.y]
        self.pivot = [10,10]
        
        self.run = self.x - mousePos[0]
        rise = self.y - mousePos[1]
        if self.run != 0:
            self.angle = -math.degrees(math.atan(rise/self.run))+90
            if (mousePos[0] < player.rect.x + player.rect.width/2 and self.run > 0) or self.run > 0:
                self.angle += -180
        #print(self.angle)
        if not self.stab:
            image_rect = self.img.get_rect(topleft = (self.origin[0] - self.pivot[0] , self.origin[1] - self.pivot[1]))
            offset_center_to_pivot = pygame.math.Vector2(self.origin) - image_rect.center
            rotated_offset = offset_center_to_pivot.rotate(-self.angle)
            rotated_image_center = (self.origin[0] - rotated_offset.x, self.origin[1] - rotated_offset.y)
            self.image = pygame.transform.rotate(self.img, self.angle)
        else:
            image_rect = self.imgstab.get_rect(topleft = (self.origin[0] , self.origin[1]))
            offset_center_to_pivot = pygame.math.Vector2(self.origin) - image_rect.center
            rotated_offset = offset_center_to_pivot.rotate(-self.stabangle)
            rotated_image_center = (self.origin[0] - rotated_offset.x, self.origin[1] - rotated_offset.y)
            if self.angle <= -90  and self.angle >= -270:
                self.rect.y += -250
                self.image = pygame.transform.rotate(self.fliped_stab, self.stabangle)
            else:
                self.image = pygame.transform.rotate(self.imgstab, self.stabangle)
        self.rect = self.image.get_rect(center = rotated_image_center)
        
    
    def draw(self, screen):
        try:
            screen.blit(self.image, self.rect)
        except:
            pass

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

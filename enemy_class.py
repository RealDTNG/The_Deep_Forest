import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load,img_dmg,health,agro_range):
        super().__init__()
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.agro_range = agro_range
        self.w = width
        self.h = height
        self.imgld = image_load
        self.imgdmg = img_dmg
        self.hp = health
        self.movey = 0
        
    def move(self,barriers,player):
        self.image = pygame.transform.scale(self.imgld, (self.w, self.h)).convert_alpha()
        
        if ((player.rect.x + player.rect.width/2 - (self.rect.x + self.w))**2 + (player.rect.y + player.rect.height/2 - (self.rect.y + self.h))**2)**(1/2) <= self.agro_range:
            self.movex = 2(player.rect.x-self.rect.x)/abs(player.rect.x-self.rect.x)
        
        self.rect.x += self.movex

        if self.rect.colliderect(b.rect for b in barriers):
            self.rect.x -= self.movex

        self.movey+=1
        
        self.rect.y += self.movey
        
        for b in barriers:
            if self.rect.colliderect(b.rect):
                self.y = b.rect.y + self.h

    def hit(self,dmg):
        self.hp -= dmg
        self.image = pygame.transform.scale(self.imgdmg, (self.w, self.h)).convert_alpha()
        if self.hp <= 0:
            return True
        else:
            return False
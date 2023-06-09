import pygame, random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load,img_dmg,health,agro_range,speed,damage):
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
        self.movex = 0
        self.speed = speed
        self.hlt = False
        self.dmg = damage
        
    def move(self,barriers,player):
        self.image = pygame.transform.scale(self.imgld, (self.w, self.h)).convert_alpha()
        
        if ((player.rect.x + player.rect.width/2 - (self.rect.x + self.w/2))**2 + (player.rect.y + player.rect.height/2 - (self.rect.y + self.h))**2)**(1/2) <= self.agro_range:
            if (self.rect.x + self.w/2) == (player.rect.x + player.rect.width/2):
                self.movex = 0
            else:
                self.movex = self.speed*(player.rect.x + player.rect.width/2 - self.rect.x - self.w/2)/abs(player.rect.x + player.rect.width/2 - self.rect.x - self.w/2)
        
        self.rect.x += self.movex

        for b in barriers:
            while pygame.sprite.collide_mask(self,b):
                self.rect.x -= self.movex/abs(self.movex)

        self.movey+=1
        
        self.rect.y += self.movey
        
        for b in barriers:
            reverse_dir = self.movey/abs(self.movey)
            while pygame.sprite.collide_mask(self,b):
                self.rect.y -= reverse_dir
                self.movey = 0

    def hit(self,sword):
        if not self.hlt:
            self.hp -= sword.dmg
            self.image = pygame.transform.scale(self.imgdmg, (self.w, self.h)).convert_alpha()
            if self.hp <= 0:
                self.kill()
                heals = 0
                for i in range(self.hp):
                    rannum = random.randint(1,5)
                    if rannum == 1:
                        heals += 1
                return [True, heals]
        return [False]

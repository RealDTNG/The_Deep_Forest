import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load,img_dmg,health,double_jump_unlock):
        super().__init__()
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.w = width
        self.h = height
        self.imgld = image_load
        self.imgdmg = img_dmg
        self.hp = health
        self.movey = 0
        if double_jump_unlock:
            self.jump = 2
            self.jumpcount = 2
        else:
            self.jump = 1
            self.jumpcount = 1
        
    def move(self,barriers):
        self.image = pygame.transform.scale(self.imgld, (self.w, self.h)).convert_alpha()
        keyvalu = {True : 1, False: 0}
        key_input = pygame.key.get_pressed()
        
        self.movex = int((-0.5*(keyvalu[key_input[pygame.K_LEFT]]+keyvalu[key_input[pygame.K_a]])**2)+(1.5*(keyvalu[key_input[pygame.K_LEFT]]+keyvalu[key_input[pygame.K_a]])))*-2 + ((-0.5*(keyvalu[key_input[pygame.K_RIGHT]]+keyvalu[key_input[pygame.K_d]])**2)+(1.5*(keyvalu[key_input[pygame.K_RIGHT]]+keyvalu[key_input[pygame.K_d]])))*2
        self.rect.x += self.movex
        
        if self.rect.colliderect(b for b in barriers):
            self.rect.x -= self.movex

        self.movey+=1

        if key_input[pygame.K_SPACE] and self.jump >0:
            self.movey -= 10
            self.jump -= 1
        
        self.rect.y += self.movey
        
        for b in barriers:
            if self.rect.colliderect(b):
                self.y = b.rect.y + self.h
                self.jump+=self.jumpcount

    def hit(self,dmg):
        self.hp -= dmg
        self.image = pygame.transform.scale(self.imgdmg, (self.w, self.h)).convert_alpha()
        if self.hp <= 0:
            return True
        else:
            return False
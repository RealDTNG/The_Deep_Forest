import pygame

class Player(pygame.sprite.Sprite):
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
        self.movex = 0
        if double_jump_unlock:
            self.jump = 2
            self.jumpcount = 2
        else:
            self.jump = 1
            self.jumpcount = 1
        self.jump_CD = 0
        
    def move(self,keys,keybinds,barriers):
        self.image = pygame.transform.scale(self.imgld, (self.w, self.h)).convert_alpha()
        keyvalu = {True : 1, False: 0}
        key_input = pygame.key.get_pressed()
        
        if self.movex >4:
            self.movex-=1
        elif self.movex < -4:
            self.movex+=1
        if key_input[keys[keybinds['RIGHT']]] or key_input[keys[keybinds['LEFT']]]:
            self.movex += 1*(keyvalu[key_input[keys[keybinds['RIGHT']]]]-keyvalu[key_input[keys[keybinds['LEFT']]]])
            self.rect.x += self.movex
        else:
            if self.movex != 0:
                self.movex -= self.movex/abs(self.movex)
        
        for b in barriers:
            if pygame.sprite.collide_mask(self,b):
                self.rect.x -= self.movex

        self.movey += 1

        self.jump_CD -= 1
        if key_input[keys[keybinds['JUMP']]] and self.jump >0 and self.jump_CD <=0:
            self.movey = -22
            self.jump -= 1
            self.jump_CD = 20
        
        self.rect.y += self.movey
        
        for b in barriers:
            if pygame.sprite.collide_mask(self,b):
                if self.movey >0:
                    self.rect.y = b.rect.y - self.h
                    self.jump=self.jumpcount
                else:
                    self.rect.y = b.rect.y + b.rect.height
                self.movey = 0

        if key_input[keys[keybinds['CROUCH']]]:
            pass

    def hit(self,dmg):
        self.hp -= dmg
        self.image = pygame.transform.scale(self.imgdmg, (self.w, self.h)).convert_alpha()
        if self.hp <= 0:
            return True
        else:
            return False
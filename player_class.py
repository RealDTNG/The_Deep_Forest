import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load,img_dmg,health,double_jump_unlock):
        super().__init__()
        self.player = pygame.transform.scale(pygame.image.load('Imgs/Player.png'),(width,height)).convert_alpha()
        self.fliped_player = pygame.transform.flip(self.player, True, False)
        self.image = self.player
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.w = width
        self.h = height
        self.imgld = image_load
        self.imgdmg = img_dmg
        self.hp = health
        self.movey = 0
        self.movex = 0
        self.happend_once = False
        if double_jump_unlock:
            self.jump = 2
            self.jumpcount = 2
        else:
            self.jump = 1
            self.jumpcount = 1
        self.jump_CD = 0
        
    def update(self,keys,keybinds,barriers):
        keyvalu = {True : 1, False: 0}
        key_input = pygame.key.get_pressed()
        mousepos = pygame.mouse.get_pos() 
         
        if self.rect.x < mousepos[0]:
            self.image = self.player
            self.mask  = pygame.mask.from_surface(self.image)  
        elif self.rect.x > mousepos[0]:
            self.image =  self.fliped_player
            self.mask  = pygame.mask.from_surface(self.image)  
            
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
            while pygame.sprite.collide_mask(self,b):
                self.rect.x -= self.movex/abs(self.movex)

        self.movey += 1

        self.jump_CD -= 1
        if key_input[keys[keybinds['JUMP']]] and self.jump >0 and self.jump_CD <=0:
            self.movey = -22
            self.jump -= 1
            self.jump_CD = 20
        
        self.rect.y += self.movey
        
        if key_input[keys[keybinds['CROUCH']]]:
            if not self.happend_once:
                self.rect.y += self.h/2
                self.happend_once = True
            self.image = pygame.transform.scale(self.image, (self.w, self.h/2)).convert_alpha()
            self.mask  = pygame.mask.from_surface(self.image)
            x,y = self.rect.x,self.rect.y
            self.rect = self.image.get_rect(topleft=(x,y))
        else:
            if self.happend_once:
                self.happend_once = False
            self.image = pygame.transform.scale(self.image, (self.w, self.h)).convert_alpha()
            self.mask  = pygame.mask.from_surface(self.image)
            x,y = self.rect.x,self.rect.y
            self.rect = self.image.get_rect(topleft=(x,y))

        for b in barriers:
            if self.movey > 0:
                collidetype= 'up'
            else:
                collidetype = 'down'
            while pygame.sprite.collide_mask(self,b):
                if collidetype == 'up':
                    self.rect.y -= 1
                    self.jump=self.jumpcount
                else:
                    self.rect.y += 1
                self.movey = 0

    def hit(self,dmg):
        self.hp -= dmg
        self.image = pygame.transform.scale(self.imgdmg, (self.w, self.h)).convert_alpha()
        if self.hp <= 0:
            return True
        else:
            return False
        
    def draw(self, screen):
        try:
            screen.blit(self.image, self.rect)
        except:
            pass
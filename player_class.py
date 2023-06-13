import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load,img_dmg,img_crouch,img_jump,img_walk,health,maxhealth,double_jump_unlock,sprint_unlock,max_stamina = 0,stamina = 100):
        super().__init__()
        self.player = pygame.transform.scale(image_load,(width,height)).convert_alpha()
        self.fliped_player = pygame.transform.flip(self.player, True, False)
        self.player_crouching = pygame.transform.scale(img_crouch,(width,height)).convert_alpha()
        self.fliped_player_crouching = pygame.transform.flip(self.player_crouching, True, False)
        self.player_jumping = pygame.transform.scale(img_jump,(width,height)).convert_alpha()
        self.fliped_player_jumping = pygame.transform.flip(self.player_jumping, True, False)
        self.walk = pygame.transform.scale(img_walk,(width,height)).convert_alpha()
        self.fliped_walk = pygame.transform.flip(self.walk, True, False)
        self.walk_count = 0
        self.walking = False
        self.image = self.player
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.w = width
        self.h = height
        self.imgld = image_load
        self.imgdmg = img_dmg
        self.hp = health
        self.maxhp = maxhealth
        self.movey = 0
        self.movex = 0
        self.direction = "left"
        self.happend_once = False
        if double_jump_unlock:
            self.jump = 2
            self.jumpcount = 2
        else:
            self.jump = 1
            self.jumpcount = 1
        self.jump_CD = 0
        self.sprint_unlock = sprint_unlock
        self.max_stamina = max_stamina
        self.stamina = stamina
        
    def update(self,keys,keybinds,barriers):
        keyvalu = {True : 1, False: 0}
        key_input = pygame.key.get_pressed()
        mousepos = pygame.mouse.get_pos() 
        
        if self.movex > 5:
            self.movex-=2
        elif self.movex < -5:
            self.movex+=2
        elif self.movex > 4:
            self.movex-=1
        elif self.movex < -4:
            self.movex+=1
        if key_input[keys[keybinds['RIGHT']]] or key_input[keys[keybinds['LEFT']]]:
            self.walk_count += 1
            self.movex += (keyvalu[key_input[keys[keybinds['RIGHT']]]]-keyvalu[key_input[keys[keybinds['LEFT']]]]) 
            if key_input[keys[keybinds['SPRINT']]] and self.stamina > 4 and self.sprint_unlock:
                if self.movex != 0:
                    self.movex = 10*self.movex/abs(self.movex)
                    self.stamina -= 5
            
        else:
            if self.stamina < self.max_stamina:
                self.stamina += 1
            if self.movex != 0:
                self.movex -= self.movex/abs(self.movex)

        self.rect.x += self.movex
        
        self.grounded = False
        
        for b in barriers:
            while pygame.sprite.collide_mask(self,b):
                if self.movey < 0:
                    self.rect.y += 3
                else:
                    if self.grounded == False:
                        if self.direction == "right":
                            self.image = self.player
                            self.mask  = pygame.mask.from_surface(self.image) 
                        elif self.direction == "left":
                            self.image = self.fliped_player
                            self.mask  = pygame.mask.from_surface(self.image)
                    self.rect.y -= 1
                    self.movey = 0
                    self.jump=self.jumpcount
                    self.grounded = True

        for b in barriers:
            while pygame.sprite.collide_mask(self,b):
                if self.movex == 0:
                    break
                else:
                    self.rect.x -= self.movex

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
            if self.rect.x < mousepos[0]:
                self.image = self.player_crouching
                self.mask  = pygame.mask.from_surface(self.image)  
            elif self.rect.x > mousepos[0]:
                self.image = self.fliped_player_crouching
                self.mask  = pygame.mask.from_surface(self.image)
            x,y = self.rect.x,self.rect.y
            self.rect = self.image.get_rect(topleft=(x,y))
        else:
            if self.happend_once:
                self.rect.y -= self.h/2
                self.happend_once = False
            if self.rect.x + self.rect.w/2 < mousepos[0]:
                if self.direction == "left":
                    self.image = self.player
                    self.mask  = pygame.mask.from_surface(self.image) 
                self.direction = "right"
                if self.walk_count >= 20:
                    if self.walking == False:
                        self.walk_count = 0
                        self.image = self.walk
                        self.walking = True
                        self.mask  = pygame.mask.from_surface(self.image)
                    else:
                        self.walk_count = 0
                        self.image = self.player
                        self.walking = False
                        self.mask  = pygame.mask.from_surface(self.image)  
            else:
                if self.direction == "right":
                    self.image = self.fliped_player
                    self.mask  = pygame.mask.from_surface(self.image)
                self.direction = "left"
                if self.walk_count >= 20:
                    if self.walking == False:
                        self.walk_count = 0
                        self.walking = True
                        self.image = self.fliped_walk
                        self.mask  = pygame.mask.from_surface(self.image)
                    else:
                        self.walk_count = 0
                        self.walking = False
                        self.image = self.fliped_player
                        self.mask  = pygame.mask.from_surface(self.image)
            x,y = self.rect.x,self.rect.y
            self.rect = self.image.get_rect(topleft=(x,y))
        
        if not self.grounded:
            if self.rect.x < mousepos[0]:
                self.image = self.player_jumping
                self.mask  = pygame.mask.from_surface(self.image)  
            elif self.rect.x > mousepos[0]:
                self.image = self.fliped_player_jumping
                self.mask  = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect(topleft=(x,y))

    def draw_health_bar(self, surface, position, sizeHP, sizeStam, color_border, color_background, color_health, color_stamina):
        pygame.draw.rect(surface, color_background, (*position, *sizeHP))
        pygame.draw.rect(surface, color_border, (*position, *sizeHP), 2)
        innerPosHP  = (position[0]+2, position[1]+2)
        innerSizeHP = (int((sizeHP[0]-4) * (self.hp/self.maxhp)), sizeHP[1]-4)
        pygame.draw.rect(surface, color_health, (*innerPosHP, *innerSizeHP))
        if self.sprint_unlock:
            pygame.draw.rect(surface, color_background, (*(position[0],position[1]+sizeHP[1]), *sizeStam))
            pygame.draw.rect(surface, color_border, (*(position[0],position[1]+sizeHP[1]), *sizeStam), 2)
            innerPosStam  = (position[0]+2, position[1]+sizeHP[1]+2)
            innerSizeStam = (int((sizeStam[0]-4) * (self.stamina/self.max_stamina)), sizeStam[1]-4)
            pygame.draw.rect(surface, color_stamina, (*innerPosStam, *innerSizeStam))

    def hit(self,enemy):
        self.hp -= enemy.dmg
        self.image = pygame.transform.scale(self.imgdmg, (self.w, self.h)).convert_alpha()
        self.movey = -10
        try:
            self.movex = 25*((self.rect.x+self.rect.w-enemy.rect.x-enemy.rect.width)/abs(self.rect.x+self.rect.w-enemy.rect.x-enemy.rect.width))
        except:
            self.movex = -25
        if self.hp <= 0:
            return True
        else:
            return False
        
    def draw(self, screen):
        try:
            screen.blit(self.image, self.rect)
        except:
            pass
    
    def back(self):
        self.rect.x -= self.movex
        
    def return_stats(self):
        return self.movex,self.movey,self.hp,self.stamina
    

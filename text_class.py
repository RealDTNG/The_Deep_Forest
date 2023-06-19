import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, Text='[Sample text]', font_size=84, font_type='Squarely.ttf', onclickFunction=None, onePress=False):
        pygame.font.init()
        self.font = pygame.font.Font(font_type, font_size)
        super().__init__() 
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font_type = font_type
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.text = str(Text)
        
        self.buttonSurf = self.font.render(self.text, True, (255, 255, 255))
        
        self.width = self.buttonSurf.get_width()
        self.height = self.buttonSurf.get_height()

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect((self.x-(self.width/2)),(self.y-(self.height/2)), self.width, self.height)

        

        self.alreadyPressed = False
    
    def update_text(self,text):
        self.text = str(text)
        self.buttonSurf = self.font.render(self.text,True,(255,255,255))

    def process(self,window,none = (255,255,25), hover = (255,255,255), click = (255,255,255)):
        mousePos = pygame.mouse.get_pos()
        
        self.font = pygame.font.Font(self.font_type, self.font_size)
        self.buttonSurf = self.font.render(self.text, True, none)
        self.width = self.buttonSurf.get_width()
        self.height = self.buttonSurf.get_height()
        self.buttonRect = pygame.Rect((self.x-(self.width/2)),(self.y-(self.height/2)), self.width, self.height)
        if self.buttonRect.collidepoint(mousePos):
            self.font = pygame.font.Font(self.font_type, (self.font_size+7))
            self.buttonSurf = self.font.render(self.text, True, hover)
            self.width = self.buttonSurf.get_width()
            self.height = self.buttonSurf.get_height()
            self.buttonRect = pygame.Rect((self.x-(self.width/2)),(self.y-(self.height/2)), self.width, self.height)
            
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurf = self.font.render(self.text, True, click)

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False
        #self.buttonSurface.blit(self.buttonSurf, [self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        window.blit(self.buttonSurf, ((self.x-(self.width/2)),(self.y-(self.height/2))))

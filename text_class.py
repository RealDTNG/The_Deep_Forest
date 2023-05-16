import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, Text='[Sample text]', font_size=84, font_type='Squarely.ttf'):
        pygame.font.init()
        self.font = pygame.font.Font(font_type, font_size)
        super().__init__() 
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(Text, True, (255, 255, 255))

        self.alreadyPressed = False
    
    def update_text(self,text):
        self.buttonSurf = self.font.render(text,True,(255,255,255))

    def process(self,window):

        #self.buttonSurface.blit(self.buttonSurf, [self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2])
        window.blit(self.buttonSurf, (self.x,self.y))
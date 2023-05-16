"""
Dawson Hoyle + Dylan Baker
2D Platformer, Name:TBD
Start: 5/16/2023     End: N/A

Dawson To Do List;
    - Start/Menu
    - Database
    - Animations
    - Ability Unlock
    - Level Design
    - Game Map
    - Game Ending
    - Bug Fixing/ Testing
    
Dylan To Do List;
    - Menu Settings
    - Resolution
    - Sprites
    - Camera
    - Sound
    - Test Map
    - Game Map
    - Game Ending
    - Bug Fixing/ Testing


"""

import pygame as pg, sys,img
from button_class import Button


pg.init()
game_state = '__menu__'
FPS = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 900
WINDOW = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.HWSURFACE)
pg.display.set_caption("Game")

btn_start = Button(30, 300, 300, 100, 'Start')

def display():
    WINDOW.fill((255,255,255)) #White background

    pg.Surface.blit(WINDOW,img.menu_backdrop,(0,0))
   

while True:
    display()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
  

    pg.display.update() #update the display
    fpsClock.tick(FPS) #speed of redraw
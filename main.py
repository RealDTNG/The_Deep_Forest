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
from text_class import Text


pg.init()
FPS = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 900
WINDOW = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.HWSURFACE)
pg.display.set_caption("Game")


game_state = 'menu'
menu_optn = "main"
curent_font = 3
fonts = {1:'texts\menu_main.ttf',2:'texts\menu_sec.ttf',3:'texts\extra.ttf'}
the_font = pg.font.Font(fonts[curent_font],140)


#v-------------------Button Functions-------------------v

def start():
    global game_state, menu_optn
    menu_optn = "start"


def how_to_play():
    global menu_optn
    menu_optn = "htp"


def settings():
    global menu_optn
    menu_optn = "settings"
    
def return_to_main():
    global menu_optn
    menu_optn = "main"


def close_program():
    pg.quit()
    sys.exit()
    
#^-------------------Button Functions-------------------^

#v-----------------------Buttons------------------------v

game_text = the_font.render("The Deep Forest", True, (133, 69, 9))
curent_font = 1
start_text = Text((WINDOW_WIDTH/2),350,"Start",70,fonts[curent_font],start)
how_to_play_text = Text((WINDOW_WIDTH/2),450,"How To Play",70,fonts[curent_font],how_to_play)
settings_text = Text((WINDOW_WIDTH/2),550,"Settings",70,fonts[curent_font],settings)
exit_text = Text((WINDOW_WIDTH/2),650,"Exit To Desktop",70,fonts[curent_font],close_program)

#^-----------------------Buttons------------------------^

def display():
    global game_state, menu_optn
    WINDOW.fill((255,255,255)) #White background

    if game_state == "menu":
        pg.Surface.blit(WINDOW,img.menu_backdrop,(0,0))
        if menu_optn == "main":
            temp_width = game_text.get_width()
            temp_height = game_text.get_height()
            WINDOW.blit(game_text, ((WINDOW_WIDTH/2)-(temp_width/2),200-(temp_height/2)))
            start_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
            how_to_play_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
            settings_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
            exit_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
        elif menu_optn == "htp":
            pass
        elif menu_optn == "settings":
            pass
    
   

while True:
    display()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close_program()
  

    pg.display.update() #update the display
    fpsClock.tick(FPS) #speed of redraw
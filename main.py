"""
Dawson Hoyle + Dylan Baker
2D Platformer, Name: The Deep Forest
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
#v---------------------Imports------------------------v

import pygame as pg, sys, img, data_functions
from button_class import Button
from text_class import Text

#^---------------------Imports------------------------^

pg.init()
data_functions
connection = data_functions.create_connection('player_save_data.db')
FPS = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 900
WINDOW = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.HWSURFACE)
pg.display.set_caption("The Deep Forest")


game_state = 'menu'
menu_optn = "main"
current_font = 1
fonts = {1:'texts\menu_main.ttf',2:'texts\menu_sec.ttf',3:'texts\extra.ttf'}
the_font = pg.font.Font(fonts[current_font],140)
keys = {"~":pg.K_BACKQUOTE,1:pg.K_1,2:pg.K_2,3:pg.K_3,4:pg.K_4,5:pg.K_5,6:pg.K_6,7:pg.K_7,8:pg.K_8,9:pg.K_9,0:pg.K_0,
        "-":pg.K_MINUS,"=":pg.K_EQUALS,"BACKSPACE":pg.K_BACKSPACE,"TAB":pg.K_TAB,"Q":pg.K_q,"W":pg.K_w,"E":pg.K_e,
        "R":pg.K_r,"T":pg.K_t,"Y":pg.K_y,"U":pg.K_u,"I":pg.K_i,"O":pg.K_o,"P":pg.K_p,"[":pg.K_LEFTBRACKET,"]":pg.K_RIGHTBRACKET,
        "BACKSLASH":pg.K_BACKSLASH,"CAPS LOCK":pg.K_CAPSLOCK,"A":pg.K_a,"S":pg.K_s,"D":pg.K_d,"F":pg.K_f,"G":pg.K_g,"H":pg.K_h,
        "J":pg.K_j,"K":pg.K_k,"L":pg.K_l,";":pg.K_SEMICOLON,"'":pg.KSCAN_APOSTROPHE,"LEFT SHIFT":pg.K_LSHIFT,"Z":pg.K_z,"X":pg.K_x,
        "C":pg.K_c,"V":pg.K_v,"B":pg.K_b,"N":pg.K_n,"M":pg.K_m,",":pg.K_COMMA,".":pg.K_PERIOD,"SLASH":pg.K_SLASH,
        "RIGHT SHIFT":pg.K_RSHIFT,"LEFT CTRL":pg.K_LCTRL,"LEFT ALT":pg.K_LALT,"SPACE":pg.K_SPACE,"RIGHT ALT":pg.K_RALT,
        "RIGHT CTRL":pg.K_RCTRL}
keybinds = {"LEFT":"A","RIGHT":"D","JUMP":"SPACE","CROUCH":"LEFT CTRL","SPRINT":"LEFT SHIFT"}

#v-------------------Button Functions-------------------v

def start():
    global game_state, menu_optn, save_datas, current_font, the_font
    current_font = 2
    the_font = pg.font.Font(fonts[current_font],50)
    
    menu_optn = "start"
    
    save_datas = data_functions.select_db(connection,"Player_Save_Info").fetchall()
    htp_text.append(the_font.render("Use WASD to move.", True, (117, 61, 8)))

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

current_font = 2

start_text = Text((WINDOW_WIDTH/2),350,"Start",70,fonts[current_font],start)
how_to_play_text = Text((WINDOW_WIDTH/2),450,"How To Play",70,fonts[current_font],how_to_play)
settings_text = Text((WINDOW_WIDTH/2),550,"Settings",70,fonts[current_font],settings)
exit_text = Text((WINDOW_WIDTH/2),650,"Exit To Desktop",70,fonts[current_font],close_program)
return_text = Text(125,60,"Return",70,fonts[current_font],return_to_main)

current_font = 1
the_font = pg.font.Font(fonts[current_font],140)
htp_title_text = the_font.render("How To Play", True, (117, 61, 8))

current_font = 2
the_font = pg.font.Font(fonts[current_font],50)

htp_text = []

htp_text.append(the_font.render(f"Use {keybinds['LEFT']} to move left and {keybinds['RIGHT']} to move right", True, (117, 61, 8)))
htp_text.append(the_font.render(f"Press {keybinds['JUMP']} to jump.", True, (117, 61, 8)))
htp_text.append(the_font.render(f"Press {keybinds['CROUCH']} to crouch.", True, (117, 61, 8)))
htp_text.append(the_font.render(f"Move the mouse to aim your weapon.", True, (117, 61, 8)))
htp_text.append(the_font.render(f"Use LEFT CLICK to attack with your weapon.", True, (117, 61, 8)))
htp_text.append(the_font.render(f"Press {keybinds['SPRINT']} to sprint.", True, (117, 61, 8)))

kb_text =[]

kb_text.append(the_font.render("Left:", True, (117, 61, 8)))
kb_text.append(the_font.render("Right:", True, (117, 61, 8)))
kb_text.append(the_font.render("Jump:", True, (117, 61, 8)))
kb_text.append(the_font.render("Crouch:", True, (117, 61, 8)))

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
            temp_width2 = htp_title_text.get_width()
            temp_height2 = htp_title_text.get_height()
            WINDOW.blit(htp_title_text, ((WINDOW_WIDTH/2)-(temp_width2/2),200-(temp_height2/2)))
            for i,t in enumerate(htp_text):
                temp_width_htp_text = t.get_width()
                temp_height_htp_text = t.get_height()
                WINDOW.blit(t, ((WINDOW_WIDTH/2)-(temp_width_htp_text/2),350+i*60-(temp_height_htp_text/2)))
            return_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
        elif menu_optn == "settings":
            for i,t in enumerate(kb_text):
                WINDOW.blit(t, (200,350+i*60))
            return_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
        elif menu_optn == "start":
            return_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
   

while True:
    display()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close_program()
  

    pg.display.update() #update the display
    fpsClock.tick(FPS) #speed of redraw
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
from wall_class import Barrier
from player_class import Player
from enemy_class import Enemy
from bullet_class import Bullet

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

#v-----------------------Variables-----------------------v

game_state = 'menu'
menu_optn = "main"
current_font = 1
count = 0
load_time = 0
loading_text = "Loading"
fonts = {1:'texts\menu_main.ttf',2:'texts\menu_sec.ttf',3:'texts\extra.ttf'}
the_font = pg.font.Font(fonts[current_font],140)
keys = {"~":pg.K_BACKQUOTE,"1":pg.K_1,"2":pg.K_2,"3":pg.K_3,"4":pg.K_4,"5":pg.K_5,"6":pg.K_6,"7":pg.K_7,"8":pg.K_8,"9":pg.K_9,
        "0":pg.K_0,"-":pg.K_MINUS,"=":pg.K_EQUALS,"BACKSPACE":pg.K_BACKSPACE,"TAB":pg.K_TAB,"Q":pg.K_q,"W":pg.K_w,"E":pg.K_e,
        "R":pg.K_r,"T":pg.K_t,"Y":pg.K_y,"U":pg.K_u,"I":pg.K_i,"O":pg.K_o,"P":pg.K_p,"[":pg.K_LEFTBRACKET,"]":pg.K_RIGHTBRACKET,
        "BACKSLASH":pg.K_BACKSLASH,"CAPS LOCK":pg.K_CAPSLOCK,"A":pg.K_a,"S":pg.K_s,"D":pg.K_d,"F":pg.K_f,"G":pg.K_g,"H":pg.K_h,
        "J":pg.K_j,"K":pg.K_k,"L":pg.K_l,";":pg.K_SEMICOLON,"'":pg.KSCAN_APOSTROPHE,"LEFT SHIFT":pg.K_LSHIFT,"Z":pg.K_z,"X":pg.K_x,
        "C":pg.K_c,"V":pg.K_v,"B":pg.K_b,"N":pg.K_n,"M":pg.K_m,",":pg.K_COMMA,".":pg.K_PERIOD,"SLASH":pg.K_SLASH,
        "RIGHT SHIFT":pg.K_RSHIFT,"LEFT CTRL":pg.K_LCTRL,"LEFT ALT":pg.K_LALT,"SPACE":pg.K_SPACE,"RIGHT ALT":pg.K_RALT,
        "RIGHT CTRL":pg.K_RCTRL}
unkeys = dict([reversed(i) for i in keys.items()])
keybinds = {"LEFT":"A","RIGHT":"D","JUMP":"SPACE","CROUCH":"LEFT CTRL","SPRINT":"LEFT SHIFT"}
choosing_key=[False]

#^-----------------------Variables-----------------------^

#v-------------------Button Functions-------------------v

def start():
    global game_state, menu_optn, save_datas, current_font, the_font, save_num, save_hp, save_time
    current_font = 2
    the_font = pg.font.Font(fonts[current_font],50)
    
    menu_optn = "start"
    
    save_num = []
    save_time = []
    save_hp = []
    save_datas = data_functions.select_db(connection,"Player_Save_Info").fetchall()
    for id in save_datas:
            save_num.append(the_font.render(f"Save {id[1]}", True, (130, 93, 14)))
            save_time.append(the_font.render(f"Play Time: [{id[2]}s]", True, (130, 93, 14)))
            save_hp.append(the_font.render(f"Current Health: [{id[3]}]", True, (130, 93, 14)))
        

def how_to_play():
    global menu_optn
    menu_optn = "htp"

def settings():
    global menu_optn
    menu_optn = "settings"

def key_change_left():
    global choosing_key
    left_key_btn.update_text('press new binding')
    choosing_key=[True,'LEFT',left_key_btn]

def key_change_right():
    global choosing_key
    right_key_btn.update_text('press new binding')
    choosing_key=[True,'RIGHT',right_key_btn]

def key_change_jump():
    global choosing_key
    jump_key_btn.update_text('press new binding')
    choosing_key=[True,'JUMP',jump_key_btn]

def key_change_crouch():
    global choosing_key
    crouch_key_btn.update_text('press new binding')
    choosing_key=[True,'CROUCH',crouch_key_btn]

def load_game():
    global wall_group,player_group,enemy_group
    wall_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    wall_group.add(Barrier(0,700,1440,200,img.grass))

def return_to_main():
    global menu_optn
    menu_optn = "main"

def draw_rect_alpha(surface, color, rect):
    shape_surf = pg.Surface(pg.Rect(rect).size, pg.SRCALPHA)
    pg.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def close_program():
    pg.quit()
    sys.exit()
    
#^-------------------Button Functions-------------------^


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

left_key_btn = Text(500,375,keybinds['LEFT'],50,fonts[current_font],key_change_left)
right_key_btn = Text(500,435,keybinds['RIGHT'],50,fonts[current_font],key_change_right)
jump_key_btn = Text(500,495,keybinds['JUMP'],50,fonts[current_font],key_change_jump)
crouch_key_btn = Text(500,555,keybinds['CROUCH'],50,fonts[current_font],key_change_crouch)

def display():
    global game_state, menu_optn, current_save, count, load_time, loading_text, choosing_key, htp_text, wall_group
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
            
            
            left_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
            right_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
            jump_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
            crouch_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
            if choosing_key[0]:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        key_name = pg.key.name(event.key)
                        if key_name.upper() in keys:
                            keybinds[choosing_key[1]] = key_name.upper()
                            choosing_key[2].update_text(keybinds[choosing_key[1]])
                            #v-------------reset htp------------v
                            htp_text = []
                            htp_text.append(the_font.render(f"Use {keybinds['LEFT']} to move left and {keybinds['RIGHT']} to move right", True, (117, 61, 8)))
                            htp_text.append(the_font.render(f"Press {keybinds['JUMP']} to jump.", True, (117, 61, 8)))
                            htp_text.append(the_font.render(f"Press {keybinds['CROUCH']} to crouch.", True, (117, 61, 8)))
                            htp_text.append(the_font.render(f"Move the mouse to aim your weapon.", True, (117, 61, 8)))
                            htp_text.append(the_font.render(f"Use LEFT CLICK to attack with your weapon.", True, (117, 61, 8)))
                            htp_text.append(the_font.render(f"Press {keybinds['SPRINT']} to sprint.", True, (117, 61, 8)))
                            #^-------------reset htp------------^
                            choosing_key = [False]
                            break

        elif menu_optn == "start":
            mousePos = pg.mouse.get_pos()
            for i,t in enumerate(save_time):
                if i == 0:
                    temp_saves_width1 = t.get_width()
                    temp_x = ((-20+(20*i))+(WINDOW_WIDTH/4)+(WINDOW_WIDTH/4)*i)
                    if temp_saves_width1 < 350:
                        rec1x = 350
                    else:
                        rec1x = temp_saves_width1
                    
                    if  mousePos[0] > (temp_x-(rec1x/2)) and mousePos[0] < (temp_x + rec1x/2) and mousePos[1] > 375 and mousePos[1] < 580:
                        if pg.mouse.get_pressed(num_buttons=3)[0]:
                            rec1 = draw_rect_alpha(WINDOW, (161, 161, 161, 160), (temp_x-(rec1x/2), 375, rec1x, 205))
                            current_save = "1"
                            pg.time.delay(750)
                            game_state = "playing"
                            load_game()
                        else:
                            rec1 = draw_rect_alpha(WINDOW, (161, 161, 161, 100), (temp_x-(rec1x/2), 375, rec1x, 205))
                    WINDOW.blit(t, (temp_x-(temp_saves_width1/2),450))
            for i,t in enumerate(save_time):
                if i == 1:
                    temp_saves_width2 = t.get_width()
                    temp_x = ((-20+(20*i))+(WINDOW_WIDTH/4)+(WINDOW_WIDTH/4)*i)
                    if temp_saves_width2 < 350:
                        rec2x = 350
                    else:
                        rec2x = temp_saves_width2
                    if  mousePos[0] > (temp_x-(rec2x/2)) and mousePos[0] < (temp_x + rec2x/2) and mousePos[1] > 375 and mousePos[1] < 580:
                        if pg.mouse.get_pressed(num_buttons=3)[0]:
                            rec2 = draw_rect_alpha(WINDOW, (161, 161, 161, 160), (temp_x-(rec2x/2), 375, rec2x, 205))
                            current_save = "2"
                            pg.time.delay(750)
                            game_state = "playing"
                            load_game()
                        else:
                            rec2 = draw_rect_alpha(WINDOW, (161, 161, 161, 100), (temp_x-(rec2x/2), 375, rec2x, 205))
                    WINDOW.blit(t, (temp_x-(temp_saves_width2/2),450))
            for i,t in enumerate(save_time):
                if i == 2:
                    temp_saves_width3 = t.get_width()
                    temp_x = ((-20+(20*i))+(WINDOW_WIDTH/4)+(WINDOW_WIDTH/4)*i)
                    
                    if temp_saves_width2 < 350:
                        rec3x = 350
                    else:
                        rec3x = temp_saves_width2
                    if  mousePos[0] > (temp_x-(rec3x/2)) and mousePos[0] < (temp_x + rec3x/2) and mousePos[1] > 375 and mousePos[1] < 580:
                        if pg.mouse.get_pressed(num_buttons=3)[0]:
                            rec3 = draw_rect_alpha(WINDOW, (161, 161, 161, 160), (temp_x-(rec3x/2), 375, rec3x, 205))
                            current_save = "3"
                            pg.time.delay(750)
                            game_state = "playing"
                            load_game()
                        else:
                            rec3 = draw_rect_alpha(WINDOW, (161, 161, 161, 100), (temp_x-(rec3x/2), 375, rec3x, 205))
                    WINDOW.blit(t, (temp_x-(temp_saves_width3/2) ,450))
            for i,t in enumerate(save_num):
                temp_saves_width = t.get_width()
                WINDOW.blit(t, (((-20+(20*i))+(WINDOW_WIDTH/4)+(WINDOW_WIDTH/4)*i)-(temp_saves_width/2),375))
            for i,t in enumerate(save_hp):
                temp_saves_width = t.get_width()
                WINDOW.blit(t, (((-20+(20*i))+(WINDOW_WIDTH/4)+(WINDOW_WIDTH/4)*i)-(temp_saves_width/2),525))
            return_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
    elif game_state == "playing":
        load_time += 1
        count += 1
        pg.Surface.blit(WINDOW,img.menu_backdrop,(0,0))
        if load_time <= 300:
            if count >= 40:
                if loading_text == "Loading":
                    loading_text = "Loading."
                elif loading_text == "Loading.":
                    loading_text = "Loading.."
                elif loading_text == "Loading..":
                    loading_text = "Loading..."
                elif loading_text == "Loading...":
                    loading_text = "Loading"
                count = 0
            load_text = the_font.render(loading_text,True,(117, 61, 8))
            load_temp_width = load_text.get_width()
            current_save_text = the_font.render(f"Save {current_save}", True, (117, 61, 8))
            save_temp_width = current_save_text.get_width()
            WINDOW.blit(load_text,((WINDOW_WIDTH/2)-(load_temp_width/2),450))
            WINDOW.blit(current_save_text,((WINDOW_WIDTH/2)-(save_temp_width/2),300))
        else:
            wall_group.draw(WINDOW)

        
            
   

while True:
    display()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close_program()
  

    pg.display.update() #update the display
    fpsClock.tick(FPS) #speed of redraw
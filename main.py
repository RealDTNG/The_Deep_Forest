"""
Dawson Hoyle + Dylan Baker
2D Platformer, Name: The Deep Forest
Start: 5/16/2023     End: N/A

Dawson To Do List;
    - Start/Menu                >DONE
    - Database                  >DONE
    - Animations                >GOOD ENOUGH
    - Ability Unlock            >DONE
    - Level Design              >WIP
    - Game Map                  >
    - Game Ending               >
    - Bug Fixing/ Testing       >
    
Dylan To Do List;   
    - Menu Settings             >DONE
    - Resolution                >DONE
    - Sprites                   >GOOD ENOUGH
    - Sound                     >
    - Test Map                  >DONE
    - Game Map                  >
    - Game Ending               >
    - Bug Fixing/ Testing       >
    
    
                         ---MAP---   

         L4-1 - L4-2 - L4-3    L3-1 - L3-2 - L3-3
           |      |      |      |      |      |
         L4-4 - L4-5 - L4-6 -- L3-4 - L3-5 - L3-6
           |      |      |      |      |      |
         L4-7 - L4-8 - L4-9    L3-7 - L3-8 - L3-9
                  |                    |
                  |                    |
         L1-1 - L1-2 - L1-4    L2-1 - L2-2 - L2-4
           |      |      |      |      |      |
T1-T2 -- L1-4 - L1-5 _ L1-6 -- L2-4 - L2-5 _ L2-6
           |      |      |      |      |      |
         L1-7 - L1-8 - L1-9    L2-7 - L2-8 - L2-9
                  |
                  |
                LB-1
         

"""
#v---------------------Imports------------------------v

import pygame as pg, data_functions as data, sys, Imgs.img as img, random, math # pip install pygame
from button_class import Button
from text_class import Text
from wall_class import Barrier
from player_class import Player
from enemy_class import Enemy
from bullet_class import Bullet
from sword_class import Sword
from spritesheet import spritesheet
#^---------------------Imports------------------------^

pg.init()
data
connection = data.create_connection('game_data.db')
FPS = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 900
WINDOW = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.SCALED | pg.RESIZABLE | pg.NOFRAME, vsync=1)
pg.display.set_caption("The Deep Forest")

#v-----------------------Variables-----------------------v

game_state = 'menu'
menu_optn = "main"
current_font = 1
count = 0
load_time = 0
pause = False
pause_delay = 40
loading_text = "Loading"
prev_location = "T1"
img.imgs()
wall_group = pg.sprite.Group()
player_group = pg.sprite.Group()
tool_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
grass_group = pg.sprite.Group()
heal_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
grass_loop = 680
slash_unlocking = False
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
saved_keys = data.select_db(connection,"Keybinds").fetchall()
for id in saved_keys:
    keybinds = {"LEFT":id[1],"RIGHT":id[2],"JUMP":id[3],"CROUCH":id[4],"SPRINT":id[6],"ATTACK":id[5]}
choosing_key=[False]

#^-----------------------Variables-----------------------^

#v-------------------Button Functions-------------------v


def start():
    global game_state, menu_optn, save_datas, current_font, the_font, save_num, save_hp, save_time, save1_data, save2_data, save3_data
    current_font = 2
    the_font = pg.font.Font(fonts[current_font],50)
    menu_optn = "start"
    
    save_num = []
    save_time = []
    save_hp = []
    save_datas = data.select_db(connection,"Player_Save_Info").fetchall()
    '''              SAVE NUM         PLAY TIME           HP             MAX HP          DMG MULT         LOCATION        SLASH UNLOC     SPRINT UNLOC      DJUMP UNLOC      SHOOT UNLOC      '''
    save1_data = [save_datas[0][1],save_datas[0][2],save_datas[0][3],save_datas[0][4],save_datas[0][5],save_datas[0][6],save_datas[0][7],save_datas[0][8],save_datas[0][9],save_datas[0][10]]
    save2_data = [save_datas[1][1],save_datas[1][2],save_datas[1][3],save_datas[1][4],save_datas[1][5],save_datas[1][6],save_datas[1][7],save_datas[1][8],save_datas[1][9],save_datas[1][10]]
    save3_data = [save_datas[2][1],save_datas[2][2],save_datas[2][3],save_datas[2][4],save_datas[2][5],save_datas[2][6],save_datas[2][7],save_datas[2][8],save_datas[2][9],save_datas[2][10]]
    for id in save_datas:
            save_num.append(the_font.render(f"Save {id[1]}", True, (130, 93, 14)))
            save_time.append(the_font.render(f"Play Time: [{id[2]}s]", True, (130, 93, 14)))
            save_hp.append(the_font.render(f"Current Health: [{id[3]}]", True, (130, 93, 14)))


def save_location(save_num):
    global save1_data,save2_data,save3_data
    if save_num == 1:
        data.update(connection,"Player_Save_Info","P_Loc",active_save_info[5],save1_data[5])
    elif save_num == 2:
        data.update(connection,"Player_Save_Info","P_Loc",active_save_info[5],save2_data[5])
    elif save_num == 3:
        data.update(connection,"Player_Save_Info","P_Loc",active_save_info[5],save3_data[5])


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


def key_change_attack():
    global choosing_key
    attack_key_btn.update_text('press new binding')
    choosing_key=[True,'ATTACK',attack_key_btn]


def key_change_sprint():
    global choosing_key
    sprint_key_btn.update_text('press new binding')
    choosing_key=[True,'SPRINT',sprint_key_btn]


def make_grass():
    global grass_group, grass_loop
    while grass_loop <= 840:
        grass_sprite1,grass_sprite2,grass_sprite3,grass_sprite4,grass_sprite5,grass_sprite6 = pg.sprite.Sprite(),pg.sprite.Sprite(),pg.sprite.Sprite(),pg.sprite.Sprite(),pg.sprite.Sprite(),pg.sprite.Sprite()
        grass_sprite1.image,grass_sprite2.image,grass_sprite3.image,grass_sprite4.image,grass_sprite5.image,grass_sprite6.image = img.grass,img.grass,img.grass,img.grass,img.grass,img.grass
        grass_sprite1.rect = grass_sprite1.image.get_rect().move(-238,grass_loop)
        grass_group.add(grass_sprite1)
        grass_sprite2.rect = grass_sprite2.image.get_rect().move(50,grass_loop)
        grass_group.add(grass_sprite2)
        grass_sprite3.rect = grass_sprite3.image.get_rect().move(338,grass_loop)
        grass_group.add(grass_sprite3)
        grass_sprite4.rect = grass_sprite4.image.get_rect().move(626,grass_loop)
        grass_group.add(grass_sprite4)
        grass_sprite5.rect = grass_sprite5.image.get_rect().move(914,grass_loop)
        grass_group.add(grass_sprite5)
        grass_sprite6.rect = grass_sprite6.image.get_rect().move(1202,grass_loop)
        grass_group.add(grass_sprite6)
        grass_loop += 40
    grass_loop = 680


def load_game():
    global wall_group,player_group,tool_group,enemy_group,player,sword, grass_group, grass_loop, prev_location, active_save_info
    if active_save_info[5] == "T1":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        heal_group.empty()
        bullet_group.empty()
        if prev_location == "T2":
            player = Player(1300,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        else:
            player = Player(100,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        wall_group.add(Barrier(1400,0,50,700,img.log))
        log_left = pg.transform.rotate(img.log, 180)
        wall_group.add(Barrier(0,0,50,700,log_left))
        log_ground = pg.transform.rotate(img.log, -90)
        wall_group.add(Barrier(0,700,1440,200,log_ground))
        
        make_grass()
        
    elif active_save_info[5] == "T2":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        heal_group.empty()
        bullet_group.empty()
        player = Player(50,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        log_ground = pg.transform.rotate(img.log, -90)
        wall_group.add(Barrier(0,700,1440,200,log_ground))
        wall_group.add(Barrier(250,620,44*3,34*2.5,img.big_rock))
        wall_group.add(Barrier(920,650,30*3,16*3,img.rock))
        
        make_grass()
    
    elif active_save_info[5] == "L1-4":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        bullet_group.empty()
        heal_group.empty()
        if prev_location == "L1-5":
            player = Player(1300,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        else:
            player = Player(50,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        log_ground = pg.transform.rotate(img.log, -90)
        wall_group.add(Barrier(-10,0,10,900,img.log))
        wall_group.add(Barrier(1360,0,90,300,img.log))
        wall_group.add(Barrier(1360,500,90,200,img.log))
        wall_group.add(Barrier(0,700,1440,200,log_ground))
        enemy_group.add(Enemy(600,500,100,70,img.slime,img.big_rock,2,400,1,1))
        make_grass()
    
    elif active_save_info[5] == "L1-5":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        bullet_group.empty()
        heal_group.empty()
        if prev_location == "L1-6":
            player = Player(1300,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        elif prev_location == "L1-8":
            player = Player(150,700,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
            player.movex = 3
            player.movey = 4
        elif prev_location == "L1-2":
            player = Player(1200,20,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        
        else:
            player = Player(50,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        wall_group.add(Barrier(0,0,500,300,img.flat_log))
        wall_group.add(Barrier(0,520,1000,50,img.flat_log))
        wall_group.add(Barrier(720,250,820,50,img.flat_log))
        wall_group.add(Barrier(500,0,600,20,img.flat_log))
        wall_group.add(Barrier(1360,0,80,250,img.log))
        wall_group.add(Barrier(1300,520,140,380,img.log))
        wall_group.add(Barrier(0,570,30,330,img.log))
        wall_group.add(Barrier(250,850,1050,50,img.flat_log))
        wall_group.add(Barrier(1150,675,150,30,img.flat_log))
        enemy_group.add(Enemy(750,600,100,70,img.slime,img.big_rock,2,400,1,1))
        enemy_group.add(Enemy(850,150,100,70,img.slime,img.big_rock,2,400,1,1))
        
    elif active_save_info[5] == "L1-6":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        bullet_group.empty()
        heal_group.empty()
        player = Player(50,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        wall_group.add(Barrier(0,0,300,200,img.log))
        wall_group.add(Barrier(300,0,1140,20,img.flat_log))
        wall_group.add(Barrier(0,520,750,380,img.log))
        wall_group.add(Barrier(1200,520,750,380,img.log))
        enemy_group.add(Enemy(1000,200,100,80,img.bat,img.big_rock,2,700,2,1,True,True))
        enemy_group.add(Enemy(600,420,100,70,img.slime,img.big_rock,2,400,1,1))
        
    elif active_save_info[5] == "L1-9":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        bullet_group.empty()
        heal_group.empty()
        if prev_location == "L1-6":
            player = Player(900,50,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        else:
            player = Player(50,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        wall_group.add(Barrier(0,0,750,50,img.flat_log))
        wall_group.add(Barrier(1200,0,750,50,img.flat_log))
        wall_group.add(Barrier(0,850,1440,50,img.flat_log))
        wall_group.add(Barrier(0,650,70,200,img.log))
        wall_group.add(Barrier(1390,50,50,800,img.log))
        enemy_group.add(Enemy(550,690,140,80,img.wolf,img.big_rock,3,500,3,2))
        enemy_group.add(Enemy(500,700,100,70,img.slime,img.big_rock,2,400,1,1))
        enemy_group.add(Enemy(400,700,100,70,img.slime,img.big_rock,2,400,1,1))
        enemy_group.add(Enemy(300,700,100,70,img.slime,img.big_rock,2,400,1,1))
        enemy_group.add(Enemy(1200,700,100,70,img.slime,img.big_rock,2,400,1,1))
        enemy_group.add(Enemy(1280,700,100,70,img.slime,img.big_rock,2,400,1,1))
        
    elif active_save_info[5] == "L1-8":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        bullet_group.empty()
        heal_group.empty()
        if prev_location == "L1-9":
            player = Player(1300,300,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        elif prev_location == "L1-5":
            player = Player(50,100,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        else:
            player = Player(50,650,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)

        wall_group.add(Barrier(0,850,1040,50,img.flat_log))
        wall_group.add(Barrier(1040,850,350,50,img.destructable))
        wall_group.add(Barrier(1390,600,50,300,img.log))
        wall_group.add(Barrier(0,0,70,650,img.log))
        wall_group.add(Barrier(300,600,1090,50,img.flat_log))
        wall_group.add(Barrier(50,350,600,50,img.flat_log))
        wall_group.add(Barrier(850,350,200,30,img.flat_log))
        wall_group.add(Barrier(1050,350,100,250,img.log))
        wall_group.add(Barrier(1150,570,30,30,img.flat_log))
        wall_group.add(Barrier(300,0,1140,50,img.flat_log))
        wall_group.add(Barrier(1390,50,50,300,img.log))
        enemy_group.add(Enemy(700,700,100,70,img.slime,img.big_rock,2,400,1,1))
        enemy_group.add(Enemy(900,700,140,80,img.wolf,img.big_rock,3,500,3,2))
        enemy_group.add(Enemy(900,400,100,70,img.slime,img.big_rock,2,400,1,1))
        
    elif active_save_info[5] == "L1-7":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        bullet_group.empty()
        heal_group.empty()
        player = Player(1300,650,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        wall_group.add(Barrier(0,850,1440,50,img.flat_log))
        wall_group.add(Barrier(0,0,50,850,img.log))
        wall_group.add(Barrier(50,300,380,50,img.flat_log))
        wall_group.add(Barrier(630,300,50,550,img.log))
        wall_group.add(Barrier(50,560,380,50,img.flat_log))
        wall_group.add(Barrier(0,0,1440,50,img.flat_log))
        wall_group.add(Barrier(830,590,560,50,img.flat_log))
        wall_group.add(Barrier(1390,0,50,640,img.log))
        wall_group.add(Barrier(680,300,510,50,img.flat_log))
        wall_group.add(Barrier(1190,540,200,50,img.flat_log))
    
    elif active_save_info[5] == "L1-2":
        wall_group.empty()
        player_group.empty()
        tool_group.empty()
        enemy_group.empty()
        grass_group.empty()
        bullet_group.empty()
        heal_group.empty()
        if prev_location == "L1-5":
            player = Player(1000,650,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        elif prev_location == "L1-1":
            player = Player(50,650,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)
        else:
            player = Player(800,650,90,160,img.player,img.big_rock,img.player_crouching,img.player_jumping,img.player_walk,active_save_info[2],5,True,True,300)

        player_group.add(player)
        sword = Sword(20,78,img.sword1,50,250,img.sword1_slash,1)
        tool_group.add(sword)
        #if not active_save_info[7] == 1:
        enemy_group.add(Enemy(0,650,50,200,img.you_diedd,img.big_rock,1,0,0,0)) #destrutable wall
        
        wall_group.add(Barrier(0,850,900,50,img.flat_log))
        wall_group.add(Barrier(1140,850,340,50,img.flat_log))
        wall_group.add(Barrier(0,0,50,650,img.log))
        wall_group.add(Barrier(300,600,1150,50,img.flat_log))
        wall_group.add(Barrier(50,350,500,50,img.flat_log))
        wall_group.add(Barrier(350,0,1090,50,img.flat_log))
        wall_group.add(Barrier(750,350,300,250,img.log))
        destructable = pg.transform.rotate(img.destructable,90)
        wall_group.add(Barrier(500,50,50,300,destructable))


def respawn():
    global game_state
    game_state = "playing"
    load_game()


def return_to_main():
    global menu_optn
    menu_optn = "main"


def draw_rect_alpha(surface, color, rect):
    shape_surf = pg.Surface(pg.Rect(rect).size, pg.SRCALPHA)
    pg.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def play_pause():
    global pause_delay, pause, menu_optn
    if pause == True:
        pause = False
        pause_delay = 0
        menu_optn = "main"
    else:
        pause = True
        pause_delay = 0


def slash_unlock():
    global slash_unlocking,active_save_info
    draw_rect_alpha(WINDOW,(191, 153, 29,130),((WINDOW_WIDTH/2-WINDOW_WIDTH/4),(WINDOW_HEIGHT/2-WINDOW_HEIGHT/4),(WINDOW_WIDTH/2),(WINDOW_HEIGHT/2)))
    main_text = the_font.render("You Have Ulocked The Sword!",True,(255, 255, 255))
    main_text_width = main_text.get_width()
    WINDOW.blit(main_text,((WINDOW_WIDTH/2)-(main_text_width/2),(WINDOW_HEIGHT/2-WINDOW_HEIGHT/4)+30))
    sub_text = the_font.render("Press Any Key To Continue",True,(255, 255, 255))
    sub_text_width = sub_text.get_width()
    WINDOW.blit(sub_text,((WINDOW_WIDTH/2)-(sub_text_width/2),(WINDOW_HEIGHT/2-WINDOW_HEIGHT/4)+380))
    rotated_sword = pg.transform.scale_by(pg.transform.rotate(img.sword1,60),3)
    WINDOW.blit(rotated_sword,((WINDOW_WIDTH/2)-(rotated_sword.get_width()/2),(WINDOW_HEIGHT/2-WINDOW_HEIGHT/4)+170))
    for event in pg.event.get(pg.KEYDOWN):
        slash_unlocking = False
        active_save_info[6] = 1


def keybindings():
    global resume_text, keybinds, WINDOW, choosing_key
    for i,t in enumerate(kb_text):
        WINDOW.blit(t, (200,350+i*60))
    return_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
        
    left_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
    right_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
    jump_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
    crouch_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
    attack_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
    sprint_key_btn.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
    if choosing_key[0]:
        for event in pg.event.get(pg.KEYDOWN):
            key_name = pg.key.name(event.key)
            if key_name.upper() in keys:
                data.update(connection, "Keybinds", choosing_key[1], key_name.upper(), keybinds[choosing_key[1]])
                saved_keys = data.select_db(connection,"Keybinds").fetchall()
                for id in saved_keys:
                    keybinds = {"LEFT":id[1],"RIGHT":id[2],"JUMP":id[3],"CROUCH":id[4],"SPRINT":id[6],"ATTACK":id[5]}
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


def close_program():
    pg.quit()
    sys.exit()


def change_location(bound, side, new_location, last_location):
    global active_save_info, prev_location,player, tempx_vel, tempy_vel, temp_hp, temp_stamina
    
    tempx_vel, tempy_vel, temp_hp, temp_stamina = player.return_stats()
    active_save_info[2] = temp_hp
    if side == "R":
        if player.rect.x >= bound and tempx_vel > 0:
                active_save_info[5] = new_location
                prev_location = last_location
                load_game()
    elif side == "L":
        if player.rect.x <= bound and tempx_vel < 0:
                active_save_info[5] = new_location
                prev_location = last_location
                load_game()
    elif side == "B":
        if player.rect.y >= bound and tempy_vel > 0:
                active_save_info[5] = new_location
                prev_location = last_location
                load_game()
    elif side == "T":
        if player.rect.y <= bound and tempy_vel < 0:
                active_save_info[5] = new_location
                prev_location = last_location
                load_game()


def save_exit():
    global active_save_info, save1_data,save2_data,save3_data, current_save
    done = True
    
    if not done:
        save_location(int(current_save))
    else:
        pg.quit()
        sys.exit()


#^-------------------Button Functions-------------------^

game_text = the_font.render("The Deep Forest", True, (133, 69, 9))

current_font = 2

start_text = Text((WINDOW_WIDTH/2),350,"Start",70,fonts[current_font],start)
resume_text = Text((WINDOW_WIDTH/2),350,"Resume",70,fonts[current_font],play_pause)
how_to_play_text = Text((WINDOW_WIDTH/2),450,"How To Play",70,fonts[current_font],how_to_play)
settings_text = Text((WINDOW_WIDTH/2),550,"Settings",70,fonts[current_font],settings)
exit_text = Text((WINDOW_WIDTH/2),650,"Exit To Desktop",70,fonts[current_font],close_program)
save_exit_text = Text((WINDOW_WIDTH/2),650,"Save And Exit",70,fonts[current_font],close_program)
return_text = Text(125,60,"Return",70,fonts[current_font],return_to_main)
respawn_text = Text(WINDOW_WIDTH/2,500,"Respawn",70,fonts[current_font],respawn)

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

kb_text = []

kb_text.append(the_font.render("Left:", True, (117, 61, 8)))
kb_text.append(the_font.render("Right:", True, (117, 61, 8)))
kb_text.append(the_font.render("Jump:", True, (117, 61, 8)))
kb_text.append(the_font.render("Crouch:", True, (117, 61, 8)))
kb_text.append(the_font.render("Attack:", True, (117, 61, 8)))
kb_text.append(the_font.render("Sprint:", True, (117, 61, 8)))

left_key_btn = Text(500,375,keybinds['LEFT'],50,fonts[current_font],key_change_left)
right_key_btn = Text(500,435,keybinds['RIGHT'],50,fonts[current_font],key_change_right)
jump_key_btn = Text(500,495,keybinds['JUMP'],50,fonts[current_font],key_change_jump)
crouch_key_btn = Text(500,555,keybinds['CROUCH'],50,fonts[current_font],key_change_crouch)
attack_key_btn = Text(500,615,keybinds['ATTACK'],50,fonts[current_font],key_change_attack)
sprint_key_btn = Text(500,675,keybinds['SPRINT'],50,fonts[current_font],key_change_sprint)


def display_menu():
    global WINDOW, game_state, menu_optn, current_save, count, load_time, loading_text, choosing_key, htp_text, wall_group, keybinds, save3_data,save1_data,save2_data
    global active_save_info
    WINDOW.fill((255,255,255)) #White background

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
        keybindings()

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
                        menu_optn = "main"
                        #location = save1_data[5]
                        active_save_info = save1_data.copy()
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
                        menu_optn = "main"
                        #location = save2_data[5]
                        active_save_info = save2_data.copy()
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
                        menu_optn = "main"
                        #location = save3_data[5]
                        active_save_info = save3_data.copy()
                        active_save_info[5] = "L1-2"
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
    
    WINDOW.blit(pg.transform.scale(img.player,(90,160)).convert_alpha(),(50, 200))
    WINDOW.blit(pg.transform.scale(img.player_walk,(90,160)).convert_alpha(),(120, 200))
    WINDOW.blit(pg.transform.scale(img.player_jumping,(90,160)).convert_alpha(),(200, 200))
    WINDOW.blit(pg.transform.scale(img.player_crouching,(90,160)).convert_alpha(),(250, 200))


def display_play():
    global load_time, count, WINDOW, load_text, loading_text, pause, WINDOW_HEIGHT, WINDOW_WIDTH, pause_delay, game_state
    global menu_optn, save_datas, current_font, the_font, save_num, save_hp, save_time, choosing_key, htp_text, keybinds
    global tree_sheet, grass_loop, prev_location, active_save_info, slash_unlocking
    WINDOW.fill((255,255,255)) #White background
    key_press = pg.key.get_pressed()
    if load_time <= 0:#CHANGE TO 300 FOR LOAD TIME
        load_time += 1
        count += 1
        pg.Surface.blit(WINDOW,img.menu_backdrop,(0,0))
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
        pause_delay += 1
        if key_press[pg.K_ESCAPE] and pause_delay >= 40:
            play_pause()
            
        if active_save_info[5] == "T1":#-----------------------------------------------------------------------------------------------------
            
            WINDOW.blit(img.fogg,(0,0))
            WINDOW.blit(img.tree4,(194,192))
            WINDOW.blit(img.tree1,(-238,374))
            WINDOW.blit(img.tree1,(50,374))
            WINDOW.blit(img.tree1,(338,374))
            WINDOW.blit(img.tree1,(650,374))
            WINDOW.blit(img.tree4,(914,192))
            WINDOW.blit(img.tree1,(1202,374))
            WINDOW.blit(img.tree3,(482,290))
            
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            
            grass_group.draw(WINDOW)
            change_location(1310, "R","T2","T1")
                
        elif active_save_info[5] == "T2":#---------------------------------------------------------------------------------------------------
            
            change_location(20, "L","T1","T2")
                
            WINDOW.blit(img.fogg,(0,0))
            WINDOW.blit(img.tree_and_branch,(420,255))
            if active_save_info[6] == 0:
                WINDOW.blit(img.sword1,(953,610))
                if player.rect.x > 830:
                    player.back()
                if player.rect.x >= 800:
                    sword_text = the_font.render(f"Press [{keybinds['ATTACK']}]",True,(83, 148, 252))
                    sword_text_width = sword_text.get_width()
                    WINDOW.blit(sword_text,(960-(sword_text_width/2),450))
                    key_input = pg.key.get_pressed()
                    if key_input[keys[keybinds['ATTACK']]]:
                        slash_unlocking = True
            else:
                sword.draw(WINDOW)
            
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
            
            change_location(1310, "R","L1-4","T2")
            
        elif active_save_info[5] == "L1-4":#---------------------------------------------------------------------------------------------------
            
            change_location(1310, "R","L1-5","L1-4")
            
            WINDOW.blit(img.fogg,(0,0))
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
        
        elif active_save_info[5] == "L1-5":#---------------------------------------------------------------------------------------------------
            
            change_location(20, "L","L1-4","L1-5")
            change_location(1310, "R","L1-6","L1-5")
            change_location(800, "B","L1-8","L1-5")
            change_location(20, "T","L1-2","L1-5")
            
            WINDOW.blit(img.woodd,(0,0))
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
        
        elif active_save_info[5] == "L1-6":#---------------------------------------------------------------------------------------------------
            
            change_location(20, "L","L1-5","L1-6")
            change_location(800, "B","L1-9","L1-6")
            
            WINDOW.blit(img.woodd,(0,0))
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
            
        elif active_save_info[5] == "L1-7":#---------------------------------------------------------------------------------------------------
            
            change_location(1320, "R","L1-8","L1-7")
            
            WINDOW.blit(img.woodd,(0,0))
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
            
        elif active_save_info[5] == "L1-8":#---------------------------------------------------------------------------------------------------
            
            change_location(20, "L","L1-7","L1-8")
            change_location(1320, "R","L1-9","L1-8")
            change_location(20, "T","L1-5","L1-8")
            
            WINDOW.blit(img.woodd,(0,0))
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
            
        elif active_save_info[5] == "L1-9":#---------------------------------------------------------------------------------------------------
            
            change_location(20, "L","L1-8","L1-9")
            change_location(20, "T","L1-6","L1-9")
            
            WINDOW.blit(img.woodd,(0,0))
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
            
        elif active_save_info[5] == "L1-1":#---------------------------------------------------------------------------------------------------
            
            WINDOW.blit(img.fogg,(0,0)) #tree background
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
            
        elif active_save_info[5] == "L1-2":#---------------------------------------------------------------------------------------------------
            
            WINDOW.blit(img.fogg,(0,0))
            change_location(850, "B","L1-5","L1-2")
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
        
        elif active_save_info[5] == "L1-3":#---------------------------------------------------------------------------------------------------
            
            WINDOW.blit(img.fogg,(0,0))
            heal_group.draw(WINDOW)
            wall_group.draw(WINDOW)
            sword.draw(WINDOW)
            enemy_group.draw(WINDOW)
            bullet_group.draw(WINDOW)
            player.draw(WINDOW)
            grass_group.draw(WINDOW)
        
        if not pause:
            if not slash_unlocking:
                player.update(keys,keybinds,wall_group)
                sword.update(player)
                player.draw_health_bar(WINDOW,(player.rect.x,player.rect.y-40),(player.rect.width,10),(player.rect.width,10),(0,0,0),(200,0,0),(0,200,0),(200,200,0))
            else:
                slash_unlock()
            for e in enemy_group:
                e.move(wall_group,player)
                if pg.sprite.collide_mask(e,sword) and sword.stab:
                    result_of_stab = e.hit(sword)
                    if result_of_stab[0]:
                        for i in range(result_of_stab[1]):
                            heal_group.add(Barrier(e.rect.x + random.randint((-e.rect.width/2),(e.rect.width/2)),e.rect.y + random.randint((-e.rect.height/2),(e.rect.height/2)),30,30,img.heal))
                    e.hlt = True
                else:
                    e.hlt = False
                if pg.sprite.collide_mask(e,player):
                    if player.hit(e):
                        game_state = "dead"
                
                if e.shooter and e.shoot:
                    run = player.rect.centerx - (e.rect.centerx)
                    rise = player.rect.centery - (e.rect.centery)
                    if run != 0:
                        theta = abs(math.atan(rise/run))
                    else:
                        theta = 180
                    if run != 0:
                        vx = (run/abs(run))*math.cos(theta)*3
                    else:
                        vx = 0
                    if rise != 0 and run != 0:
                        vy = (rise/abs(rise))*math.sin(theta)*3
                    else:
                        vy = 3
                    bullet_group.add(Bullet(e.rect.centerx,e.rect.centery,30,30,img.projectile,[vx,vy],0,2))
            
            for h in heal_group:
                if pg.sprite.collide_mask(h,player) and player.hp < player.maxhp:
                    player.hp += 1
                    h.kill()

            for b in bullet_group:
                b.move()
                if b.hit_check([player]) == player:
                    if player.hit(b):
                        game_state = "dead"
        elif pause:
            pause_rec = draw_rect_alpha(WINDOW, (0, 0, 0, 190), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
            if menu_optn == "main":
                current_font = 1
                the_font = pg.font.Font(fonts[current_font],140)
                pause_tital = the_font.render("Paused", True, (117, 61, 8))
                temp_width2 = pause_tital.get_width()
                temp_height2 = pause_tital.get_height()
                WINDOW.blit(pause_tital, ((WINDOW_WIDTH/2)-(temp_width2/2),200-(temp_height2/2)))
                current_font = 2
                the_font = pg.font.Font(fonts[current_font],70)
                current_save_loaded = the_font.render(f"Save {current_save}", True, (117, 61, 8))
                temp_save_w = current_save_loaded.get_width()
                WINDOW.blit(current_save_loaded, ((125 - temp_save_w/2), 20))
                resume_text.process(WINDOW,(117, 61, 8),(158, 84, 14),(64, 39, 8))
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
                keybindings()
                
def display_dead():
    WINDOW.blit(img.you_diedd,(0,0))
    current_font = 1
    the_font = pg.font.Font(fonts[current_font],140)
    game_over_title = the_font.render("You_Died", True, (255, 180, 18))
    temp_width3 = game_over_title.get_width()
    temp_height3 = game_over_title.get_height()
    WINDOW.blit(game_over_title, ((WINDOW_WIDTH/2)-(temp_width3/2),300-(temp_height3/2)))
    current_font = 2
    the_font = pg.font.Font(fonts[current_font],70)
    current_save_loaded = the_font.render(f"Save {current_save}", True, (255, 180, 18))
    temp_save_w = current_save_loaded.get_width()
    WINDOW.blit(current_save_loaded, ((125 - temp_save_w/2), 20))
    exit_text.process(WINDOW,(255, 180, 18),(158, 84, 14),(64, 39, 8))
    respawn_text.process(WINDOW,(255, 180, 18),(158, 84, 14),(64, 39, 8))


while True:
    if game_state == "playing":
        display_play()
    elif game_state == "dead":
        display_dead() 
    elif game_state == "menu":
        display_menu()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            close_program()

    pg.display.update() #update the display
    fpsClock.tick(FPS) #speed of redraw
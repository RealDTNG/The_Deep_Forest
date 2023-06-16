"""
File TO Store Imgs Neatly
"""
import pygame as pg
from spritesheet import spritesheet

def imgs():
    global tree_sheet, menu_backdrop, grass, log, tree1, big_rock, rock, thin_grass, slime, player, sword1, tree_and_branch, dead_tree
    global tree2, tree3, tree4, sword2, sword1_slash, sword2_slash, fogg, wolf, bat, player_crouching, player_jumping, heal,player_walk, destructable
    global flat_log, projectile, woodd, you_diedd, hehe, power
    
    tree_sheet = spritesheet('Imgs\Tree_SpriteSheet.png')
    
    toolsheet = spritesheet('Imgs\Tool_SpriteSheet.png')
    
    playersheet = spritesheet('Imgs\Player_SpriteSheet.png')
    
    menu_backdrop = pg.transform.scale(pg.image.load('Imgs/menu_backdrop.png'),(1440,900))
    
    destructable = pg.transform.scale_by(tree_sheet.image_at((305,157,25,8)),3)
    
    player = playersheet.image_at((0,0,45,77))
    
    player_walk = playersheet.image_at((0,84,45,76))
    
    player_crouching = playersheet.image_at((52,0,45,77))
    
    player_jumping = playersheet.image_at((56,84,45,76))
    
    sword1 = pg.transform.scale_by(toolsheet.image_at((0,0,13,39)),2)
    
    sword2 = toolsheet.image_at((18,0,15,60))
    
    sword1_slash = toolsheet.image_at((38,0,19,85))
    
    sword2_slash = toolsheet.image_at((18,0,24,144))
    
    grass = pg.transform.scale_by(tree_sheet.image_at((672,136,96,30)),3)
    
    thin_grass = tree_sheet.image_at((569,144,96,17))
    
    log = tree_sheet.image_at((835,90,20,31))
    
    flat_log = pg.transform.rotate(log,-90)
    
    big_rock = pg.transform.scale_by(tree_sheet.image_at((616,201,50,33)), 2)
    
    rock = pg.transform.scale_by(tree_sheet.image_at((569,216,30,16)),2)
    
    tree1 = pg.transform.scale_by(tree_sheet.image_at((379, 42, 68, 87)),4)
    
    tree2 = pg.transform.scale_by(tree_sheet.image_at((472, 23, 83, 106)),4)
    
    tree3 = pg.transform.scale_by(tree_sheet.image_at((572, 26, 73, 103)),4)
    
    tree4 = pg.transform.scale_by(tree_sheet.image_at((665, 2, 64, 127)),4)
    
    dead_tree = pg.transform.scale_by(tree_sheet.image_at((753,31,64,98)),4)
    
    tree_and_branch = pg.transform.scale_by(tree_sheet.image_at((282,24,83,106)),4.2)
    
    slime = pg.transform.scale(pg.image.load('Imgs/slime_enemy.png'),(100,80))

    wolf = pg.transform.scale(pg.image.load('Imgs/wolf_enemy.png'),(140,80))

    bat = pg.transform.flip(pg.transform.scale(pg.image.load('Imgs/bat_enemy.png'),(100,80)), True, False)
    
    fogg = pg.transform.scale_by(tree_sheet.image_at((0,0,230,130)),7)
    
    woodd = pg.transform.scale_by(tree_sheet.image_at((0,170,230,130)),7)
    
    you_diedd = pg.transform.scale_by(tree_sheet.image_at((970,0,230,130)),7)

    heal = pg.transform.scale(pg.image.load('Imgs/heal.png'),(20,20))
    
    projectile = pg.transform.scale(pg.image.load('Imgs/Projectile.png'),(20,20))

    hehe = pg.transform.scale(pg.image.load('Imgs/enemy_1_concept.png'),(200,300))

    power = pg.transform.scale(pg.image.load('Imgs/power.png'),(60,60))
    
    
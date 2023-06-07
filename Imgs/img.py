"""
File TO Store Imgs Neatly
"""
import pygame as pg
from spritesheet import spritesheet

def imgs():
    global tree_sheet, menu_backdrop, grass, log, tree1, big_rock, rock, thin_grass, slime, player, sword1, tree_and_branch, dead_tree
    global tree2, tree3, tree4
    tree_sheet = spritesheet('Imgs\Tree_SpriteSheet.png')
    toolsheet = spritesheet('Imgs\Tool_SpriteSheet.png')
    menu_backdrop = pg.transform.scale(pg.image.load('Imgs/menu_backdrop.png'),(1440,900))
    player = pg.transform.scale(pg.image.load('Imgs/Player.png'),(90,160))
    sword1 = toolsheet.image_at((0,0,14,39))
    grass = tree_sheet.image_at((672,136,96,30))
    thin_grass = tree_sheet.image_at((569,144,96,17))
    log = tree_sheet.image_at((835,90,20,31))
    big_rock = tree_sheet.image_at((616,200,44,34))
    rock = tree_sheet.image_at((569,216,30,16))
    tree1 = tree_sheet.image_at((379, 42, 68, 87))
    tree2 = tree_sheet.image_at((472, 23, 83, 106))
    tree3 = tree_sheet.image_at((572, 26, 73, 103))
    tree4 = tree_sheet.image_at((665, 2, 64, 127))
    dead_tree = tree_sheet.image_at((753,31,64,98))
    tree_and_branch = tree_sheet.image_at((282,24,83,106))
    slime = pg.transform.scale(pg.image.load('Imgs/slime_enemy.png'),(100,80))
    
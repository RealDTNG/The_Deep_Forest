"""
File TO Store Imgs Neatly
"""
import pygame as pg
from spritesheet import spritesheet

def imgs():
    global tree_sheet, menu_backdrop, grass, log, tree1, big_rock, rock, thin_grass, slime, player
    tree_sheet = spritesheet('Imgs\Tree_SpriteSheet.png')
    menu_backdrop = pg.transform.scale(pg.image.load('Imgs/menu_backdrop.png'),(1440,900))
    player = pg.transform.scale(pg.image.load('Imgs/Player.png'),(90,160))
    grass = tree_sheet.image_at((672,136,96,30))
    log = tree_sheet.image_at((835,90,20,31))
    big_rock = tree_sheet.image_at((616,200,44,34))
    rock = tree_sheet.image_at((569,216,30,16))
    thin_grass = tree_sheet.image_at((569,144,96,17))
    tree1 = tree_sheet.image_at((379, 42, 68, 87))
    slime = pg.transform.scale(pg.image.load('Imgs/slime_enemy.png'),(100,80))
    
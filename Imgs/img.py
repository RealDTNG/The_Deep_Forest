"""
File TO Store Imgs Neatly
"""
import pygame as pg
from spritesheet import spritesheet

def imgs():
    global tree_sheet, menu_backdrop, grass, log, tree1, big_rock, rock, thin_grass
    tree_sheet = spritesheet('Imgs\Tree_SpriteSheet.png')
    menu_backdrop = pg.transform.scale(pg.image.load('Imgs/menu_backdrop.png'),(1440,900))
    grass = tree_sheet.image_at((671,136,97,30))
    log = tree_sheet.image_at((834,88,21,33))
    big_rock = tree_sheet.image_at((616,200,44,34))
    rock = tree_sheet.image_at((569,216,30,16))
    thin_grass = tree_sheet.image_at((569,144,96,17))
    tree1 = tree_sheet.image_at((0, 41, 71, 86))
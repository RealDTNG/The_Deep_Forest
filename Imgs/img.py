"""
File TO Store Imgs Neatly
"""
import pygame as pg
from spritesheet import spritesheet

def imgs():
    global tree_sheet, menu_backdrop, grass, logg, tree1
    tree_sheet = spritesheet('Imgs\Tree_SpriteSheet_Outlined.png')
    menu_backdrop = pg.transform.scale(pg.image.load('Imgs/menu_backdrop.png'),(1440,900))
    grass = pg.transform.scale(pg.image.load('Imgs/grass.jfif'),(1440,200))
    logg = tree_sheet.image_at((314,97,12,31))
    tree1 = tree_sheet.image_at((0, 41, 71, 86))
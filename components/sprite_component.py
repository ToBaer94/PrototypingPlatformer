import pygame as pg


class SpriteComponent(object):
    def __init__(self, size, color):
        self.image = pg.Surface(size)
        self.image.fill(color)

import pygame as pg

Vector = pg.math.Vector2


class PositionComponent(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, entity):
        pass
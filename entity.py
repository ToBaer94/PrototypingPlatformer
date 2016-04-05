import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, level):
        super(Entity, self).__init__()

        self.world = level
        self.level = level.tile_renderer.tmx_data

        self.direct = -1

        self.on_ground = False
        self.components = {}

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def remove_component(self, component_name):
        del self.components[component_name]

    def add_component(self, component_name, component):
        self.components[component_name] = component

    def has_component(self, component_name):
        if component_name in self.components:
            return True
        return False

    def get_component(self, component_name):
        if self.has_component(component_name):
            return self.components[component_name]
        return None





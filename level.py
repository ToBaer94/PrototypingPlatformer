
from tilerenderer import Renderer
import pygame as pg
from os import path
from entity import Entity

import random

from components.input_component import InputComponent
from components.velocity_component import VelocityComponent
from components.position_component import PositionComponent
from components.gravity_component import GravityComponent
from components.physics_component import PhysicsComponent
from components.ai_component import AIComponent
from components.health_component import HealthComponent
from components.player_component import PlayerObject
from components.sprite_component import SpriteComponent
from components.flying_component import FlyingComponent


class Level(object):
    def __init__(self):
        self.tmx_file = path.join(path.dirname(__file__), "assets", "levels", "map.tmx")
        self.tile_renderer = Renderer(self.tmx_file)
        self.map_surface = self.tile_renderer.make_map()
        self.map_rect = self.map_surface.get_rect()

        self.entities = pg.sprite.Group()

        self.create_player()

        self.create_enemy()

        self.input = InputComponent()
        self.ai = AIComponent()
        self.gravity = GravityComponent()
        self.physics = PhysicsComponent()

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                self.create_enemy()

            if event.key == pg.K_SPACE:
                for entity in self.entities:
                    if entity.has_component("player") and entity.has_component("velocity"):
                        entity.remove_component("velocity")
                    elif not entity.has_component("velocity"):
                        entity.add_component("velocity", VelocityComponent())



    def update(self, dt):
        for entity in self.entities:
            self.input.update(entity)
            self.ai.update(entity)
            self.gravity.update(entity)
            self.physics.update(entity)

    def draw(self, screen):
        screen.blit(self.map_surface, (0, 0))
        self.entities.draw(screen)

    def create_enemy(self):
        pos_x = random.randint(1, 700)
        pos_y = random.randint(100, 400)
        position = PositionComponent(pos_x, pos_y)
        velocity = VelocityComponent()
        health = HealthComponent()

        sprite = SpriteComponent((10, 10), pg.Color("red"))

        enemy = Entity(self)
        enemy.add_component("sprite", sprite)


        enemy.image = enemy.components["sprite"].image
        enemy.rect = enemy.components["sprite"].image.get_rect()
        enemy.add_component("position", position)

        enemy.add_component("velocity", velocity)
        enemy.add_component("health", health)
        self.entities.add(enemy)

    def create_player(self):
        pos_x = 200
        pos_y = 200

        tag = PlayerObject()

        position = PositionComponent(pos_x, pos_y)
        velocity = VelocityComponent()
        health = HealthComponent()
        canfly = FlyingComponent()

        sprite = SpriteComponent((20, 20), pg.Color("blue"))

        player = Entity(self)
        player.add_component("sprite", sprite)
        player.image = player.components["sprite"].image
        player.rect = player.components["sprite"].image.get_rect()
        player.add_component("position", position)
        player.add_component("velocity", velocity)
        player.add_component("health", health)
        player.add_component("player", tag)
        player.add_component("can_fly", canfly)

        self.entities.add(player)
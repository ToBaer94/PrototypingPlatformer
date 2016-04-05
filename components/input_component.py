import pygame as pg


class InputComponent(object):
    WALK_SPEED = 5
    RUN_SPEED = 10
    JUMP_HEIGHT = -6
    RUN_JUMP_HEIGHT = -8

    def update(self, entity):
        if "player" in entity.components:
            if entity.has_component("velocity"):
                keys_pressed = pg.key.get_pressed()
                if keys_pressed[pg.K_LSHIFT]:
                    speed = self.RUN_SPEED
                    height = self.RUN_JUMP_HEIGHT
                else:
                    speed = self.WALK_SPEED
                    height = self.JUMP_HEIGHT
                if keys_pressed[pg.K_RIGHT]:
                    entity.components["velocity"].x = speed

                elif keys_pressed[pg.K_LEFT]:
                    entity.components["velocity"].x = -speed

                else:
                    entity.components["velocity"].x = 0

                if keys_pressed[pg.K_UP]:
                    if entity.on_ground:
                        entity.on_ground = False
                        entity.components["velocity"].y = height

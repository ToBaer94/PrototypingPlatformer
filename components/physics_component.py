import pygame as pg


class PhysicsComponent(object):
    def update(self, entity):
        if entity.has_component("velocity"):

            if entity.has_component("can_fly"):
                entity.on_ground = True
            else:
                entity.on_ground = False
                
            entity.components["position"].x += entity.components["velocity"].x
            self.handle_horizontal_collision(entity)

            entity.components["position"].y += entity.components["velocity"].y
            self.handle_vertical_collision(entity)

            entity.rect.x = entity.components["position"].x
            entity.rect.y = entity.components["position"].y

    def handle_horizontal_collision(self, entity):
        world_pos_y = (entity.components["position"].y + 0.5 * entity.rect.height) // 32

        left = entity.components["position"].x // 32
        right = (entity.components["position"].x + entity.rect.width) // 32

        try:
            properties_left = entity.level.get_tile_properties(left, world_pos_y, 0)
            properties_right = entity.level.get_tile_properties(right, world_pos_y, 0)


            if "collider" in properties_left:
                if properties_left["collider"] == "True":
                    entity.components["position"].x = left * 32 + 32
                    entity.components["velocity"].x = 0

            if "collider" in properties_right:
                if properties_right["collider"] == "True":
                    entity.components["position"].x = right * 32 - entity.rect.width
                    entity.components["velocity"].x = 0

        except:
            if entity.components["position"].x <= 0:
                entity.components["position"].x = 0
                entity.components["velocity"].x = 0
            elif entity.components["position"].x >= 800 - entity.rect.width:
                entity.components["position"].x = 800 - entity.rect.width
                entity.components["velocity"].x = 0

    def handle_vertical_collision(self, entity):
        world_pos_x = (entity.components["position"].x + 0.5 * entity.rect.width ) // 32

        try:
            top = entity.components["position"].y  // 32
            bottom = (entity.components["position"].y + entity.rect.height) // 32

            properties_top = entity.level.get_tile_properties(world_pos_x, top, 0)
            properties_bottom = entity.level.get_tile_properties(world_pos_x, bottom, 0)

            if "collider" in properties_top:
                if properties_top["collider"] == "True":
                    entity.components["position"].y = top * 32 + 32

            if "collider" in properties_bottom:
                if properties_bottom["collider"] == "True":
                    entity.components["position"].y = bottom * 32 - entity.rect.height
                    entity.components["velocity"].y = 0
                    entity.on_ground = True

        except:
            if entity.components["position"] > 600:
                print "entity fell off the world"
                entity.kill()


class EnemyCollision(object):
    def update(self, entity):
        for enemy in entity.world.enemy_group:
            if entity.rect.colliderect(enemy):
                entity.health.decrease_health(enemy.damage)
                print entity.health.get_health()







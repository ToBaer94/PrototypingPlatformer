

class AIComponent(object):
    WALK_SPEED = 2

    def update(self, entity):
        if not "player" in entity.components:
            if entity.has_component("velocity"):
                if entity.components["velocity"].x == 0 and entity.on_ground:
                    entity.direct *= -1
                    entity.components["velocity"].y = -5

                if entity.direct > 0:
                    speed = self.WALK_SPEED
                elif entity.direct < 0:
                    speed = -self.WALK_SPEED

                else:
                    raise ValueError("Error")

                entity.components["velocity"].x = speed
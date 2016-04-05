

class GravityComponent(object):
    GRAVITY = 0.2

    def update(self, entity):
        if entity.has_component("velocity"):
            entity.components["velocity"].y += self.GRAVITY

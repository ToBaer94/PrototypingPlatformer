

class HealthComponent(object):
    def __init__(self, x=10):
        self.health = x

    def get_health(self):
        return self.health

    def increase_health(self, amount):
        self.health += amount

    def decrease_health(self, amount):
        self.health -= amount
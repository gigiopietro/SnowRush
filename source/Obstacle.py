from source.Const import entity_speed
from source.Entity import Entity


class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def destroy(self):
        pass

    def move(self,):
        if self.rect.right > -10:
            self.rect.centerx -= entity_speed[self.name]
            # self.destroy()
from source.Const import display_width, display_height
from source.Entity import Entity


class Ground(Entity):
    def __init__(self, name: str, position: tuple):
        self.respawn_position = (0,0)
        super().__init__(name, position)
        self.speed = 4
        # self.start_pos = (self.rect.centerx, self.rect.centery)

    def move(self, ):
        self.rect.centery -= float(self.speed / 2)
        self.rect.centerx -= float(self.speed )
        if self.rect.right <= 0:
            self.rect.left = self.respawn_position[0]
            self.rect.top = self.respawn_position[1]
        # if self.rect.top <= display_height * -1:
        #     self.rect.bottom = display_height

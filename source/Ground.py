from source.Const import display_width, display_height
from source.Entity import Entity


class Ground(Entity):
    def __init__(self, name: str, position: tuple):
        self.speed = 1
        super().__init__(name, position)
        self.start_pos = (self.rect.centerx, self.rect.centery)

    def move(self, ):
        self.rect.centery -= self.speed / 2
        self.rect.centerx -= self.speed / 1.76
        if self.rect.right <= 0:
            self.rect.left = 0
            self.rect.top = 0
        # if self.rect.top <= display_height * -1:
        #     self.rect.bottom = display_height

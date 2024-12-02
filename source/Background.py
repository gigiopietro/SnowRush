from source.Const import display_width, display_height
from source.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= 1
        if self.rect.right <= 0:
            self.rect.left = display_width
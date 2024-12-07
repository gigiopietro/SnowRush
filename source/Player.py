import pygame.key
from source.Entity import Entity

JUMP_Y = 140
class Player(Entity):
    def __init__(self, name:str, position: tuple):
        self.is_jumping = False
        self.is_falling = False
        super().__init__(name, position)
        self.start_position_y = self.rect.centery
    def can_jump(self) -> bool:
        return not self.is_jumping and not self.is_falling

    def update(self,):
        # atualizar estados
        if self.rect.centery >= self.start_position_y and self.is_falling:
            self.is_falling = False

        # checar inputs para modificar estados
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] and self.can_jump():
            self.jump()

        # chamar metodos com os estados modificados
        self.move()
        pass

    def jump(self):
        self.is_jumping = True
        # fazer ele mover para cima
        # self.rect.centery -= JUMP_Y

        pass

    def destroy(self):
        pass

    def move(self, ):
        if self.is_jumping:
            if self.rect.centery > self.start_position_y - JUMP_Y:
                self.rect.centery -= self.speed * 2
            else:
                self.is_jumping = False
                self.is_falling = True

        if self.is_falling and self.rect.centery < self.start_position_y:
            self.rect.centery += self.speed
        pass
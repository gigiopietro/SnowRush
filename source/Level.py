import pygame
from source.Entity import Entity
from source.EntityFactory import EntityFactory

menu_path = './Asset/Background/'

class Level:
    def __init__(self, display_surface, name, game_mode):
        self.display_surface=display_surface
        self.name=name
        self.game_mode=game_mode
        self.entity_list: list[Entity]=[]
        self.entity_list.extend(EntityFactory.get_entity('lvl1_bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.display_surface.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass

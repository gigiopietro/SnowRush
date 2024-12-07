from abc import ABC, abstractmethod
import pygame.image

from source.Const import entity_health, entity_speed

background_path='./Asset/Background/'

class Entity(ABC):
    def __init__(self, name:str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(background_path + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = entity_speed[self.name]

        self.health = entity_health[self.name]

    @abstractmethod
    def move(self,):
        pass

    @abstractmethod
    def destroy(self):
        pass
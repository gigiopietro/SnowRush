from abc import ABC, abstractmethod
import pygame.image

background_path='./Asset/Background/'

class Entity(ABC):
    def __init__(self, name:str, position: tuple, custom_speed: int = 3):
        self.name=name
        self.surf=pygame.image.load(background_path + name + '.png')
        self.rect=self.surf.get_rect(left=position[0], top=position[1])
        self.speed=custom_speed

    @abstractmethod
    def move(self,):
        pass
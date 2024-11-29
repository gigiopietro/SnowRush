import pygame
from source.Menu import Menu

Size=(576, 324)

class Game:
    def __init__(self):
        pygame.init()
        print('pygame init')
        self.displaySurface = pygame.display.set_mode(size=Size)
        self.menu = Menu(self.displaySurface)

    def run(self):
        while True:
            menu = Menu(self.displaySurface)
            menu.run()
            pass


 
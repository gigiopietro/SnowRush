import pygame
from source.Menu import Menu
from source.Const import displayWidth,displayHeight

class Game:
    def __init__(self):
        pygame.init()
        print('pygame init')
        self.displaySurface = pygame.display.set_mode(size=(displayWidth, displayHeight))
        self.menu = Menu(self.displaySurface)

    def run(self):
        while True:
            menu = Menu(self.displaySurface)
            menu.run()
            pass


 
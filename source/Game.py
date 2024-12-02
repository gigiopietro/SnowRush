import pygame

from source.Level import Level
from source.Menu import Menu
from source.Const import display_width, display_height, option_menu


class Game:
    def __init__(self):
        pygame.init()
        print('pygame init')
        self.display_surface=pygame.display.set_mode(size=(display_width, display_height))

    def run(self):
        while True:
            menu=Menu(self.display_surface)
            return_menu=menu.run()

            if return_menu==option_menu[0]:
                level=Level(self.display_surface, "Level1", return_menu)
                level_return = level.run()
            elif return_menu==option_menu[2]:
                pygame.quit()
                quit()
            else:
                pass

 
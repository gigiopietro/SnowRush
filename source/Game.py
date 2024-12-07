import pygame

from source.Level import Level
from source.Menu import Menu
from source.Const import display_width, display_height, option_menu
from source.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.player_score = [0]
        self.display_surface=pygame.display.set_mode(size=(display_width, display_height))

    def run(self):
        while True:
            score = Score(self.display_surface)
            menu=Menu(self.display_surface)
            return_menu = menu.run()

            if return_menu==option_menu[0]:
                player_score = [0]
                level = Level(self.display_surface, "Level1", return_menu)
                level_return = level.run(player_score)
                if level_return:
                    score.save_score(return_menu, player_score)

            elif return_menu==option_menu[1]:
                score.show_score()
            elif return_menu==option_menu[2]:
                pygame.quit()
                quit()
            else:
                pass


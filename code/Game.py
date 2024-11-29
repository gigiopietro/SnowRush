import pygame
from code.Menu import Menu

Size=(576, 324)

class Game:
    def __init__(self):
        pygame.init()
        print('pygame init')
        self.window=pygame.display.set_mode(size=Size)

    def run(self):
        pygame.mixer_music.load('./Asset/MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # or event in pygame.event.get():
               # if event.type == pygame.QUIT:
                #    pygame.quit()  # Close Window
                #    quit()  # end pygame


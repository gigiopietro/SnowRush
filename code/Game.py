import pygame
from code.Menu import Menu

Size=(640, 480)

class Game:
    def __init__(self):
        self.window = None

    def __init_(self):
        pygame.init()
        window = pygame.display.set_mode(size=Size)

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame


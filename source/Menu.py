import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from source.Const import displayWidth, lilacColor, optionMenu, whiteColor

music_path = './Asset/Music/'
menu_path = './Asset/Menu/'

class Menu:
    def __init__(self, window):
        self.window=window
        self.bgMenu = pygame.image.load(menu_path + 'PRE_ORIG_SIZE.png')
        self.rect = self.bgMenu.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load(music_path + 'MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.bgMenu, dest=self.rect)
            self.menu_text(50, "SNOW RUSH", lilacColor, ((displayWidth/2), 70))
            for i in range(len(optionMenu)):
                self.menu_text(30, optionMenu[i], whiteColor, ((displayWidth/2), 150 + 50 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="PromptFont", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

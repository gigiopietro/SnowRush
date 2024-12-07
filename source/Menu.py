import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from source.Const import display_width, lilac_color, option_menu, white_color, yellow_color, menu_path, music_path


class Menu:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.surf = pygame.image.load(menu_path + 'PRE_ORIG_SIZE.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load(music_path + 'MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.display_surface.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "SNOW RUSH", lilac_color, ((display_width / 2), 70))

            for i in range(len(option_menu)):
                if i == menu_option:
                    self.menu_text(30, option_menu[i], yellow_color, ((display_width / 2), 150 + 50 * i))
                else:
                    self.menu_text(30, option_menu[i], white_color, ((display_width / 2), 150 + 50 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(option_menu) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(option_menu) - 1
                    if event.key == pygame.K_RETURN:
                        return option_menu[menu_option]


            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.display_surface.blit(source=text_surf, dest=text_rect)

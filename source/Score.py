import pygame
from pygame import Surface, Rect
from pygame.font import Font

from source.Const import score_path, music_path, lilac_color, score_pos, option_menu


class Score:

    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.surf = pygame.image.load( score_path + 'Score_bg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, game_mode: str ,player_score: list[int]):
        pygame.mixer_music.load(music_path + 'MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        self.display_surface.blit(source=self.surf, dest=self.rect)
        while True:
            self.score_text(48, f'Score:{player_score}', lilac_color, score_pos['Title'])
            if game_mode == option_menu[0]:
                text = 'Enter your nickname (4 Character):'
            pygame.display.flip()
            pass

    def show_score(self):
        pygame.mixer_music.load(music_path + 'MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        self.display_surface.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="PromptFont", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.display_surface.blit(source=text_surf, dest=text_rect)
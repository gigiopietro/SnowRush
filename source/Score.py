import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from source.Const import score_path, music_path, lilac_color, score_pos, option_menu, yellow_color
from source.DBProxy import DBProxy


class Score:

    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.surf = pygame.image.load( score_path + 'Score_bg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, return_menu: str, player_score: list[int]):
        pygame.mixer_music.load(music_path + 'MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        nickname = ''
        while True:
            self.display_surface.blit(source=self.surf, dest=self.rect)
            self.score_text(48, f'Score:{player_score}', yellow_color, score_pos['Title'])
            if return_menu == option_menu[0]:
                score = player_score[0]
                text_nick = 'Insert a nickname (4 characters):'
                text_info = 'Press "ESC" to return to the menu'
            self.score_text(20, text_nick, lilac_color, score_pos['EnterName'])
            self.score_text(20, text_info, lilac_color, score_pos['Label2'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(nickname) == 4:
                        db_proxy.save({'name': nickname, 'score': score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == K_ESCAPE:
                            return
                    elif event.key == K_BACKSPACE:
                        nickname = nickname[:-1]
                    else:
                        if len(nickname) < 4:
                            nickname += event.unicode

            self.score_text(20, nickname, lilac_color, score_pos['Nickname'])
            pygame.display.flip()
            pass

    def show_score(self):
        pygame.mixer_music.load(music_path + 'MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        self.display_surface.blit(source=self.surf, dest=self.rect)
        self.score_text(20, 'TOP 5 SCORE', yellow_color, score_pos['Title'])
        self.score_text(20, 'NAME          SCORE          DATE          ', lilac_color, score_pos['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top5()
        db_proxy.close()
        for player_score in list_score:
            id_, nickname, score, date = player_score
            self.score_text(20, f'            {nickname}               {score: 05d}          {date}', yellow_color, score_pos[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="PromptFont", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.display_surface.blit(source=text_surf, dest=text_rect)

# Pegando a data e horário
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
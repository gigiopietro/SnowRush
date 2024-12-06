import random
import sys

import pygame
from pygame import SurfaceType, Surface, Rect
from pygame.font import Font

from source.Const import white_color, display_height, lilac_color, event_obstacle, spawn_time
from source.Entity import Entity
from source.EntityFactory import EntityFactory
from source.Menu import music_path


class Level:
    def __init__(self, display_surface: SurfaceType, name, game_mode):
        self.timeout = 20000
        self.display_surface=display_surface
        self.name=name
        self.game_mode=game_mode
        self.entity_list: list[Entity]=[]
        self.entity_list.extend(EntityFactory.get_entity('lvl1_bg'))
        self.character = EntityFactory.get_entity('Character')
        pygame.time.set_timer(event_obstacle, spawn_time)

    def run(self):
        pygame.mixer_music.load(music_path + 'ThemeMusic.mp3')
        pygame.mixer_music.play(-1)
        clock=pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.display_surface.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            self.display_surface.blit(self.character.surf, self.character.rect)
            self.character.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == event_obstacle:
                    choice = random.choice(('Obstacle1', 'Obstacle2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14,f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', white_color, (10,5))
            self.level_text(14, f'fps:{clock.get_fps() :.0f}', lilac_color, (10, display_height - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', lilac_color, (10, display_height - 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='PromptFont', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.display_surface.blit(source=text_surf, dest=text_rect)
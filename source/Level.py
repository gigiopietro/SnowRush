import random
import sys

import pygame
from pygame import SurfaceType, Surface, Rect
from pygame.font import Font

from source.Const import white_color, display_height, lilac_color, event_obstacle, spawn_time
from source.Entity import Entity
from source.EntityFactory import EntityFactory
from source.EntityMediator import EntityMediator
from source.Menu import music_path
from source.Obstacle import Obstacle


class Level:
    def __init__(self, display_surface: SurfaceType, name, game_mode):
        self.display_surface=display_surface
        self.name=name
        self.game_mode=game_mode
        self.level_entity_list: list[Entity]=[]
        self.level_entity_list.extend(EntityFactory.get_entity('lvl1_bg'))
        self.obstacle_list: list[Obstacle] = []
        self.character = EntityFactory.get_entity('Character')
        self.is_game_over = False
        self.spawn_obstacle()
        pygame.time.set_timer(event_obstacle, spawn_time)

    def spawn_obstacle(self):
        choice = random.choice(('Obstacle1', 'Obstacle2'))
        self.obstacle_list.append(EntityFactory.get_entity(choice))

    def run(self, score: list[int]):
        pygame.mixer_music.load(music_path + 'ThemeMusic.mp3')
        pygame.mixer_music.set_volume(0.4)
        pygame.mixer_music.play(-1)
        clock=pygame.time.Clock()
        while True:
            clock.tick(60)
            if not self.is_game_over:
                score[0] += 1

            for ent in self.level_entity_list:
                self.display_surface.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for obstacle in self.obstacle_list:
                self.display_surface.blit(source=obstacle.surf, dest=obstacle.rect)
                obstacle.move()

            self.display_surface.blit(self.character.surf, self.character.rect)
            self.character.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == event_obstacle:
                    self.spawn_obstacle()

            self.level_text(14, f'Score:{score[0]}', white_color, (10, 20))
            self.level_text(14, f'fps:{clock.get_fps() :.0f}', lilac_color, (10, display_height - 35))
            self.level_text(14, f'entidades: {len(self.obstacle_list)}', lilac_color, (10, display_height - 20))
            pygame.display.flip()
            # collisions
            EntityMediator.verify_collision(entity_list=self.obstacle_list)
            EntityMediator.verify_health(entity_list=self.obstacle_list)
            has_player_collide = EntityMediator.check_player_collision(self.character, self.obstacle_list)
            if has_player_collide:
                self.game_over()
                return True

    def game_over(self):
        self.is_game_over = True
        # chamar game over
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.display_surface.blit(source=text_surf, dest=text_rect)

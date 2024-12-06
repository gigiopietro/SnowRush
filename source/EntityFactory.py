from source.Background import Background
from source.Const import display_width, display_height
from source.Ground import Ground
from source.Obstacle import Obstacle
from source.Player import Player

# offset_y_second_ground = 399
offset_y_second_ground = 200

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'lvl1_bg':
                list_bg=[]
                for i in range(5):
                     list_bg.append(Background(f'lvl1_{i + 1}',(0,0)))
                     list_bg.append(Background(f'lvl1_{i + 1}', (display_width, 0)))

                first_ground = Ground('bg_losangcompleto', (0, 0))
                respawn_ground_position = (first_ground.rect.bottomright[0], first_ground.rect.bottomright[1] - offset_y_second_ground)
                first_ground.respawn_position = respawn_ground_position
                list_bg.append(first_ground)

                second_ground = Ground('bg_losangcompleto', respawn_ground_position)
                second_ground.respawn_position = respawn_ground_position
                list_bg.append(second_ground)
                # list_bg.append(Ground('bg_neve', (display_width, display_height)))
                return list_bg
            case 'Character':
                return Player('Character', (10, display_height / 2))
            case 'Obstacle1':
                return Obstacle('Obstacle1', (display_width + 10, 220))
            case 'Obstacle2':
                return Obstacle('Obstacle2', (display_width + 10, 165))
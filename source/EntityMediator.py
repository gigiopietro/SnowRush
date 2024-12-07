from source.Entity import Entity
from source.Obstacle import Obstacle
from source.Player import Player


class EntityMediator:

    @staticmethod
    def __collision_display(ent: Entity):
        if isinstance(ent, Obstacle):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__collision_display(test_entity)

    @staticmethod
    def check_player_collision(player: Player, entity_list: list[Entity]) -> bool:
        rects = []
        for i in range(len(entity_list)):
            rects.append(entity_list[i].rect)
        return len(player.rect.collidelistall(rects)) > 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)


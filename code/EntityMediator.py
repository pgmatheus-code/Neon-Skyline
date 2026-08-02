from code.Background import Background
from code.Const import WIN_WIDTH
from code.Entity import Entity
from code.Foe import Foe
from code.FoeShot import FoeShot
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collision_window(entity: Entity): # private out-of-bounds destruction
        if isinstance(entity, Foe): # similar to if (entity is Foe) from c#
            if entity.rect.right < 0:
                entity.health = 0
        if isinstance(entity, PlayerShot): # similar to if (entity is Foe) from c#
            if entity.rect.left > WIN_WIDTH:
                entity.health = 0
        if isinstance(entity, FoeShot): # similar to if (entity is Foe) from c#
            if entity.rect.left < 0:
                entity.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            EntityMediator.__verify_collision_window(entity= entity_list[i])

            for j in range(i+1, len(entity_list)):
                EntityMediator.__verify_collision_entity(entity_list[i], entity_list[j])

    @staticmethod
    def __give_score(foe: Foe, entity_list: list[Entity]):
        if foe.last_dmg == 'player1_shot':
            for entity in entity_list:
                if entity.name == 'player1_ship':
                    entity.score += foe.score
        elif foe.last_dmg == 'player2_shot':
            for entity in entity_list:
                if entity.name == 'player2_ship':
                    entity.score += foe.score

    @staticmethod
    def __verify_collision_entity(entity1: Entity, entity2: Entity):  # private

        # avoid friendly fire
        is_interaction_valid = False
        if ((isinstance(entity1, Foe) and isinstance(entity2, PlayerShot)) or
            (isinstance(entity1, PlayerShot) and isinstance(entity2, Foe)) or
            (isinstance(entity1, Player) and isinstance(entity2, FoeShot)) or
            (isinstance(entity1, FoeShot) and isinstance(entity2, Player))
        ):
            is_interaction_valid = True

        if is_interaction_valid:
            if (entity1.rect.right >= entity2.rect.left and
                entity1.rect.left <= entity2.rect.right and
                entity1.rect.bottom >= entity2.rect.top and
                entity1.rect.top <= entity2.rect.bottom
            ):
                # entity2 damages entity1
                entity1.last_dmg = entity2.name
                entity1.health -= entity2.damage
                # entity1 damages entity2
                entity2.last_dmg = entity1.name
                entity2.health -= entity1.damage

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health > 0 or isinstance(entity, Background): continue

            if isinstance(entity, Foe):
                EntityMediator.__give_score(entity, entity_list)

            entity_list.remove(entity)
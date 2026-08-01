from code.Entity import Entity
from code.Foe import Foe


class EntityMediator:
    @staticmethod
    def __verify_collision_window(entity: Entity): # private
        if isinstance(entity, Foe): # similar to if (entity is Foe) from c#
            if entity.rect.right < 0:
                entity.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity=test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)
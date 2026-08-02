from code.Const import ENTITY_DEFAULT_HEALTH, SHOT_DEFAULT_SPEED, ENTITY_DEFAULT_DAMAGE
from code.Entity import Entity

class FoeShot(Entity):
    def __init__(self, name: str, position: tuple, entity_name: str):
        super().__init__(
            entity_type='shot',
            name=name,
            position=position,
            health=ENTITY_DEFAULT_HEALTH['shot'],
            damage=ENTITY_DEFAULT_DAMAGE[f'{entity_name[:-2]}_shot']
        )

    def move(self):
        layer_name = self.name[6:]
        self.rect.centerx -= SHOT_DEFAULT_SPEED # scrolling movement
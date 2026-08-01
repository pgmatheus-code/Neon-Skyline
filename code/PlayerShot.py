from code.Const import ENTITY_DEFAULT_HEALTH, SHOT_DEFAULT_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(entity_type='shot', name=name, position=position, health=ENTITY_DEFAULT_HEALTH['shot'])

    def move(self):
        layer_name = self.name[6:]
        self.rect.centerx += SHOT_DEFAULT_SPEED # scrolling movement
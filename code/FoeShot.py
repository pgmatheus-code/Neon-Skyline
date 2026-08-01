from code.Entity import Entity


class FoeShot(Entity):
    pass
    # def __init__(self, name: str, position: tuple, auto_stretch: bool = False):
    #
    #     super().__init__('ship', f'{name}_ship_{foe_ship_size}', position)
    #     self.current_foe_speed = FOE_SHIP_DICT[foe_ship_size]
    #
    # def move(self):
    #     layer_name = self.name[6:]
    #     self.rect.centerx -= self.current_foe_speed * FOE_SPEED_MULTIPLIER # scrolling movement
    #
    #     # reset scrolling at the end
    #     #if self.rect.right <= 0:
    #     #    self.rect.left = WIN_WIDTH + 10
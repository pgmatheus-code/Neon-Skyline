#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Player(Entity):
    def __init__(self, position: tuple):
        super().__init__('ship', 'player_ship', position)

    def move(self, ):
        pass

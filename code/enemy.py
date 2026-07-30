#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__('ship', name, position)

    def move(self, ):
        pass

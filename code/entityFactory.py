#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'city1':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(name=f'city1/layer{i+1}', position=(0,0)))
                    list_bg.append(Background(name=f'city1/layer{i + 1}', position=(WIN_WIDTH, 0)))
                return list_bg
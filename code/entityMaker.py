#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityMaker:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'bg{i}', (0, 0)))
                return list_bg

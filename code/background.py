#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity1 import Entity1

class Background(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= 1
        pass

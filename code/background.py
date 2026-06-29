#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH
from code.entity1 import Entity1

class Background(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= 1
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("./assets/bg/nature_8/1.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)
        pg.display.flip()
        pass

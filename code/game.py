#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code import menu
from code.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(640, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # # check event queue
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()  # close
            #         quit()  # end

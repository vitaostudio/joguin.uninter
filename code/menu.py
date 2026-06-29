#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame import Surface, Rect
from pygame.ftfont import Font

from code.const import WIN_WIDTH, COLOR_BLUE, MENU_OPTION, COLOR_BLACK, COLOR_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./assets/bg/nature_8/1.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pg.mixer_music.load('./bgm/1.ogg')
        pg.mixer_music.play(-1)
        while True:
            #DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Dankey", COLOR_BLUE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Kang dois", COLOR_BLUE, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 180 + 30 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 180 + 30 * i))

            # CHECK EVENTS
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # close
                    quit()  # end
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pg.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pg.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]


            pg.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

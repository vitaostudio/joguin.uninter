import pygame as pg

print('Setup Start')
pg.init()
window = pg.display.set_mode(size=(800, 600))
print('Setup Finish')

print('Loop Start')
while True:
    # check event queue
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # close
            quit()  # end

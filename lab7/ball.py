import pygame as pg
pg.init()
wit = 500
hei = 500
scrin = pg.display.set_mode((wit, hei))
pg.display.set_caption("Moving Ball")
whit = (255, 255, 255)
red = (255, 0, 0)
x = wit // 2
y = hei // 2
speed = 20
def ballpic(x, y):
    pg.ballpic(scrin, red, (x, y), 25)
running = True
while running:
    for e in pg.e.get():
        if e.type == pg.QUIT:
            running = False
        elif e.type == pg.KEYDOWN:
            if e.key == pg.K_UP:
                y -= speed
            elif e.key == pg.K_DOWN:
                y += speed
            elif e.key == pg.K_LEFT:
                x -= speed
            elif e.key == pg.K_RIGHT:
                x += speed
    if x < 25:
        x = 25
    elif x > wit - 25:
        x = wit - 25
    if y < 25:
        y = 25
    elif y > hei - 25:
        y = hei - 25
    scrin.fill(whit)
    ballpic(x, y)
    pg.display.update()
pg.quit()
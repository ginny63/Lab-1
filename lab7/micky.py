import pygame as pg
import time
import datetime
import math
pg.init()
gas = WIDTH ,HEIGHT = 1000,1000
mid = WIDTH//2 , HEIGHT//2
rad = 1000
scrin = pg.display.set_mode((RES))
chasy = pg.time.Clock()
pg.display.set_caption("Mickey Clock")
cec = pg.image.load("C:\Users\kairb\Pictures").convert_alpha()
min = pg.image.load("C:\Users\kairb\Pictures").convert_alpha()
recec = cec.get_rect()
remin = min.get_rect()
remin.centr = remin.centr = mid
backgr = pg.image.load("C:\Users\kairb\Pictures\mickey")
runn =True
angl1 = 0
angl2 = 0
while runn:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            runn = False
    time = datetime.datetime.now()
    timinut = time.minute
    tisec = time.second
    angl1 = -timinut*6 
    leg1 = pg.transform.rotate(min, angl1)
    rec1 = leg1.get_rect()
    rec1.center = remin.center
    angl2 = -tisec*6 #6 is degree
    leg2 = pg.transform.rotate(cec, angl2)
    rec2 = leg2.get_rect()
    rec2.centr = recec.center
    scrin.blit(backgr, (0, 0))
    scrin.blit(leg1, rec1)
    scrin.blit(leg2, rec2)
    pg.display.flip()
    chasy.tick(60)
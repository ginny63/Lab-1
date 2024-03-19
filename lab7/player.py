import time
import pygame as pg
pg.init()

s1path = "C:\Users\kairb\Documents\mp1"
s2path = "C:\Users\kairb\Documents\mp2"
s3path = "/C:\Users\kairb\Documents\mp3"
sc = pg.display.set_mode((480, 360))
pg.display.set_caption("mp3 player")
vremya = pg.time.Clock()
s2 = pg.mixer.music.load(s2path)
s3 = pg.mixer.music.load(s3path)
s1 = pg.mixer.music.load(s1path)
musiclis = [s1path, s2path, s3path]
pg.mixer.music.play(-1)
cove = pg.image.load("C:\Users\kairb\Pictures\cover")

sc.blit(cove, (0, 0))
dplay = False
runn = True
res = 0
while runn:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            runn = False
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_SPACE:
                dplay = not dplay
                if dplay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif ev.key == pg.K_RIGHT:
                
                res += 1
                if res == len(musiclis):
                    res = 0
                pg.mixer.music.load(musiclis[res])
                pg.mixer.music.play()
            elif ev.key == pg.K_LEFT:
                res -= 1
                if res == -1:
                    res = len(musiclis)-1
                pg.mixer.music.load(musiclis[res])
                pg.mixer.music.play()


    pg.display.flip()
    vremya.tick(60)
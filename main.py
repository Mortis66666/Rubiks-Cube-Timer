import pygame
import os
import time
from datetime import datetime

width, height = 1000,600

pygame.font.init()


render = pygame.font.SysFont("LCD",100)
render2 = pygame.font.SysFont("LCD",70)

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Rubik's cube timer")

white = 233,233,233
black = 0,0,0

background = pygame.image.load(
    os.path.join("Assets","background.jpeg")
)

background = pygame.transform.scale(background,(width,height))


def draw_window(mm:int,ss:int,ms:int,pause:bool):
    win.blit(background,(0,0))

    m = str(mm)if len(str(mm))==2 else f"0{mm}"
    s = str(ss)if len(str(ss))==2 else f"0{ss}"
    e = str(ms)if len(str(ms))==2 else f"0{ms}"

    time = render.render(f"{m}:{s}",1,black)
    position = width//2-time.get_width()//2-20, height//2-time.get_height()//2-20

    time2 = render2.render(f"{e}",1,black)
    position2 = width//2-time2.get_width()//2-20, height//2-time2.get_height()//2+30

    t = render.render("Hit space to start and pause",1,white)

    win.blit(time,position)
    win.blit(time2,position2)
    win.blit(t,(width//2-t.get_width()//2,0))
    



    pygame.display.update()


def main():

    run = True
    clock = pygame.time.Clock()

    minutes = 0
    seconds = 0
    milliseconds = 0
    pause = True

    last_space_hitted = time.time()

    while run:

        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(minutes,seconds,milliseconds,pause)

        if not pause:
            if milliseconds < 99:
                milliseconds += 1
            elif milliseconds == 99 and seconds < 59:
                milliseconds = 0
                seconds += 1
            elif seconds == 59 and milliseconds == 99:
                seconds = 0
                milliseconds = 0
                minutes += 1
        
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_SPACE]and time.time()-last_space_hitted>1.5:
            pause = (False if pause else True)
            last_space_hitted = time.time()
        elif key_pressed[pygame.K_r]:
            minutes,seconds,milliseconds = black

        

if __name__ == '__main__':
    main()
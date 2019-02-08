# -*- coding: utf-8 -*- 
# Time : 2019/1/30 21:33 
# Author : hubozhi
import pygame
from pygame import *
from sys import exit
back_image = './image/sushiplate.jpg'
SCREEN_SIZE = 0,0

if __name__ == "__main__":
    pygame.init()
    screen_size = (640,480)
    win = pygame.display.set_mode(screen_size,RESIZABLE,32)
    background = pygame.image.load(back_image).convert()

    while True:
        event = pygame.event.wait()
        if event.type == QUIT: exit()

        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption("Window resized to " + str(event.size))
        screen_width, screen_height = SCREEN_SIZE
        # 这里需要重新填满窗口
        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                win.blit(background, (x, y))

        pygame.display.update()
    pass
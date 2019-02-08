# -*- coding: utf-8 -*-
# Time : 2019/2/3 12:07
# Author : hubozhi
import pygame
from pygame.locals import *
from sys import exit
import time
background_image = './image/sushiplate.jpg'
sprite_image = './image/fugu.png'

if __name__=="__main__":
    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)
    background = pygame.image.load(background_image).convert()
    sprite = pygame.image.load(sprite_image)
    width =sprite.get_width()
    click = pygame.time.Clock()
    # 大小：get_size 高：get_height  宽：get_width
    clock = pygame.time.Clock()
    speed = 250
    # sprite的起始坐标
    x = -width

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:exit()

        screen.blit(background, (0, 0))
        screen.blit(sprite, (x, 100))
        time_passed = clock.tick()
        time_passed_seconds = time_passed/1000
        distance_moved = time_passed_seconds * speed
        x += distance_moved
        #消失多少，出现多少
        if x>640-width:
            screen.blit(sprite,(-(640-x),100))

        if x>640:x=0

        pygame.display.update()
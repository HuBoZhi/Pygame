# -*- coding: utf-8 -*- 
# Time : 2019/2/3 13:36 
# Author : hubozhi
import pygame
from pygame.locals import *
from sys import exit

background_image = './image/sushiplate.jpg'
sprite_image = './image/fugu.png'

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    background = pygame.image.load(background_image).convert()
    sprite = pygame.image.load(sprite_image)
    clock = pygame.time.Clock()
    x, y = 100, 100
    speed_x, speed_y = 133, 170

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(background, (0, 0))



        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 1000
        x += int(speed_x * time_passed_seconds)
        y += int(speed_y * time_passed_seconds)

        screen.blit(sprite, (x, y))

        # 到达边界后速度反向
        if x > 640 - sprite.get_width():
            speed_x = -speed_x
            x = 640 - sprite.get_width()
        elif x < 0:
            speed_x = -speed_x

        if y > 480 - sprite.get_height():
            speed_y = -speed_y
            y = 480 - sprite.get_height()
        elif y < 0:
            speed_y = -speed_y
            y = 0
        pygame.display.update()
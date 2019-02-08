# -*- coding: utf-8 -*- 
# Time : 2019/1/29 22:03 
# Author : hubozhi
import pygame
from pygame.locals import *
from sys import exit
import time
background_image_filename = './image/sushiplate.jpg'

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    background = pygame.image.load(background_image_filename).convert()

    x, y = 0, 0
    move_x, move_y = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            print('Pressed LEFT Button!')
                        elif index == 1:
                            print('The mouse wheel Pressed!')
                        elif index == 2:
                            print('Pressed RIGHT Button!')

        if event.type == KEYDOWN:
            # 键盘有按下？
            if event.key == K_LEFT:
                # 按下的是左方向键的话，把x坐标减一
                move_x = -1
            elif event.key == K_RIGHT:
                # 右方向键则加一
                move_x = 1
            elif event.key == K_UP:
                # 类似了
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            # 如果用户放开了键盘，图就不要动了
            move_x = 0
            move_y = 0

        # 计算出新的坐标
        x += move_x
        y += move_y

        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        # 在新的位置上画图
        pygame.display.update()
        time.sleep(0.035)
    pass
# -*- coding: utf-8 -*- 
# Time : 2019/2/3 14:46 
# Author : hubozhi
import pygame
from pygame.locals import *
from sys import exit
from gameobjects import vector2

background_image = './image/sushiplate.jpg'
sprite_image = './image/fugu.png'
mouse_x,mouse_y=0,0

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    background = pygame.image.load(background_image).convert()
    sprite = pygame.image.load(sprite_image)
    clock = pygame.time.Clock()
    heading = vector2.Vector2((50,50))
    position = vector2.Vector2(20.0,20.0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                for index in range(len(mouse_presses)):
                    if mouse_presses[index]:
                        if index==0:
                            mouse_x,mouse_y = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        screen.blit(sprite, position)

        time_passed = clock.tick(200)
        time_passed_seconds = time_passed / 1000

        # 在参数前面加*意味着把列表或元组展开

        destination = vector2.Vector2((mouse_x,mouse_y)) - vector2.Vector2(*sprite.get_size()) / 2
        # 计算当鱼儿当前位置到鼠标位置的向量
        vector_to_mouse = vector2.Vector2.__sub__(destination, position)
        vector_to_mouse.normalize()
        # heading可以看做是鱼的速度，鱼的速度大小、方向不断改变

        heading = heading + (vector_to_mouse * 0.1)
        position += heading * time_passed_seconds
        pygame.display.update()
# -*- coding: utf-8 -*- 
# Time : 2019/2/7 11:58 
# Author : hubozhi
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

background_image_filename = './image/sushiplate.jpg'
sprite_image_filename = './image/fugu.png'

def fire():
    print("K_SPACE")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    background = pygame.image.load(background_image_filename).convert()
    sprite = pygame.image.load(sprite_image_filename).convert_alpha()
    clock = pygame.time.Clock()
    sprite_pos = Vector2(200, 150)  # 初始位置

    sprite_speed = 300. # 每秒前进的像素数（速度）

    sprite_rotation = 0.# 初始角度

    sprite_rotation_speed = 360.  # 每秒转动的角度数（转速）

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pressed_keys = pygame.key.get_pressed()
        rotation_direction = 0.
        movement_direction = 0.
          # 更改角度
        if pressed_keys[K_LEFT]:
            rotation_direction = +1.
        if pressed_keys[K_RIGHT]:
            rotation_direction = -1.

         # 前进、后退
        if pressed_keys[K_UP]:
            movement_direction = +1.
        if pressed_keys[K_DOWN]:
            movement_direction = -1.

        screen.blit(background, (0, 0))
        # 获得一条转向后的鱼
        rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
        # 转向后，图片的长宽会变化，因为图片永远是矩形，为了放得下一个转向后的矩形，外接的矩形势必会比较大
        w, h = rotated_sprite.get_size()
        # 获得绘制图片的左上角
        sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
        screen.blit(rotated_sprite, sprite_draw_pos)
        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0

        # 图片的转向速度也需要和行进速度一样，通过时间来控制
        sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
        # 获得前进（x方向和y方向），这两个需要一点点三角的知识
        heading_x = sin(sprite_rotation * pi / 180.)
        heading_y = cos(sprite_rotation * pi / 180.)
        # 转换为单位速度向量
        heading = Vector2(heading_x, heading_y)
        # 转换为速度
        heading *= movement_direction
        sprite_pos += heading * sprite_speed * time_passed_seconds
        pygame.display.update()


    # pygame.init()
    # screen = pygame.display.set_mode((640, 480), 0, 32)
    # background = pygame.image.load(background_image_filename).convert()
    # sprite = pygame.image.load(sprite_image_filename).convert_alpha()
    #
    # clock = pygame.time.Clock()
    #
    # sprite_pos = Vector2(200, 150)
    # sprite_speed = 300.
    #
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             exit()
    #     pressed_keys = pygame.key.get_pressed()
    #
    #     key_direction = Vector2(0, 0)
    #     if pressed_keys[K_LEFT]:
    #         key_direction.x = -1
    #     elif pressed_keys[K_RIGHT]:
    #         key_direction.x = +1
    #
    #     if pressed_keys[K_UP]:
    #         key_direction.y = -1
    #     elif pressed_keys[K_DOWN]:
    #         key_direction.y = +1
    #
    #     key_direction.normalize()
    #
    #     screen.blit(background, (0,0))
    #     screen.blit(sprite, sprite_pos)
    #
    #     time_passed = clock.tick(30)
    #     time_passed_seconds = time_passed / 1000.0
    #
    #     sprite_pos += key_direction * sprite_speed * time_passed_seconds
    #
    #     pygame.display.update()

        # pygame.init()
        #
        # win = pygame.display.set_mode((640,480),0,32)
        # while True:
        #     for event in pygame.event.get():
        #         if event.type==QUIT:
        #             exit()
        #         if event.type==KEYDOWN:
        #             pressed_keys = pygame.key.get_pressed()
        #
        #             if pressed_keys[K_SPACE]:
        #              # Space key has been pressed
        #                 fire()
        #             pressed_keys = pygame.key.get_pressed()
        pass
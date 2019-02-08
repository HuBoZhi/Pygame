# -*- coding: utf-8 -*-
# Time : 2019/1/29 17:59 
# Author : hubozhi
import pygame
from pygame.locals import *  # 导入一些常用的函数和常量
from sys import exit         # 向sys模块借一个exit函数用来退出程序

# 指定图像文件名称
back_image_filename = './image/sushiplate.jpg'
mouse_image_filename = './image/fugu.png'

if __name__=='__main__':
    # 初始化pygame,为使用硬件做准备
    pygame.init()

    # 创建了一个窗口
    win = pygame.display.set_mode((640,470),0,32)
    # 设置窗口标题
    pygame.display.set_caption("Hello, World!")
    # pygame.display.set_caption('The first game')
    # 加载并转换图像
    background = pygame.image.load(back_image_filename).convert()
    mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            # 接收到退出事件后退出程序
            if event.type == QUIT:  exit()
        # 将背景图画上去
        win.blit(background,(0,0))
        # blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。
        # 画完以后一定记得用update更新一下，否则画面一片漆黑。

        # 获得鼠标位置
        x, y = pygame.mouse.get_pos()

        # 计算[光标图案]的左上角位置【图片以左上角为基准】
        # mouse_cursor.get_width(),mouse_cursor.get_height()得到图片的长宽
        # 让鼠标所在位置为光标图案的中心点，所以图片的左上角应该向左上方移动
        x = x - mouse_cursor.get_width()/2
        y = y - mouse_cursor.get_height()/2
        win.blit(mouse_cursor, (x, y))  # 把光标画上去
        pygame.display.update()        # 刷新一下画面

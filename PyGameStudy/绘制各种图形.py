# -*- coding: utf-8 -*-
# Time : 2019/2/2 14:09
# Author : hubozhi
import pygame
from pygame.locals import *
from sys import exit

from random import *
from math import pi

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    points = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            # 按 【任意键】 加and条件后变成 【按c键】可以清屏并把点回复到原始状态
            if event.type == KEYDOWN and event.key==K_c:
                points = []
                screen.fill((255, 255, 255))

            if event.type == MOUSEBUTTONDOWN:
                screen.fill((255, 255, 255))
                # 获得当前鼠标点击位置
                x, y = pygame.mouse.get_pos()
                points.append((x, y))

                # 画随机矩形
                # rc = (randint(0, 255), randint(0, 255), randint(0, 255)) # 矩形的颜色
                # # rp = (randint(0, 639), randint(0, 479))    # x,y位置,x,y为矩形左上角
                # # rs = (639 - randint(rp[0], 639), 479 - randint(rp[1], 479))  # 宽高
                # rp = (x,y)
                # rs = (400,200)
                # pygame.draw.rect(screen, rc, Rect(rp, rs))

                # 画随机圆形
                # rc = (randint(0, 255), randint(0, 255), randint(0, 255))
                # # rp = (randint(0, 639), randint(0, 479)) # 圆心位置
                # # rr = randint(1, 200) # 圆的半径
                # rp = (500,200)
                # rr = 90
                # pygame.draw.circle(screen, rc, rp, rr)


                # 根据点击位置画弧线
                # angle = (x / 639.) * pi * 2.
                # pygame.draw.arc(screen, (0, 0, 0), (0, 0, 639, 479), 0, angle, 3)

                # 根据点击位置画椭圆(和矩形类似)
                # rc = (0, 255, 0)
                # rp = (x,y)
                # rs = (200,300)
                # pygame.draw.ellipse(screen, rc, Rect(rp,rs))

                # 从左上和右下画两根线连接到点击位置
                # l1c = (0, 0, 255);l2c = (255, 0, 0) # line 的颜色
                # l1start_p=(0, 0);l2start_p=(640, 480) # line 的起始坐标
                # l1end_p=(x,y);l2end_p=(x, y) #line 的结束坐标
                # pygame.draw.line(screen, l1c, l1start_p, l1end_p)
                # pygame.draw.line(screen, l2c, l2start_p, l2end_p)

                # 画点击轨迹图
                if len(points) > 1:
                    pygame.draw.lines(screen, (155, 155, 0), False, points, 2)

                # 画多边形，可以理解为存在一条连线（连线为最后一次点击和第一次点击的连线，这条线没啥用）的轨迹图
                # if len(points) >= 3:
                #    pygame.draw.polygon(screen, (0, 155, 155), points, 2)

                # # 把每个点画明显一点
                # for p in points:
                #     # 在点击的位置画一个小圆，p是坐标，3是半径
                #     pygame.draw.circle(screen, (155, 155, 155), p, 3)

                # 画一条平滑的线
                aalc = (0,255,0)
                # pygame.draw.aaline(screen,aalc,(0,0),(x,y))

                # 画一系列平滑的线（轨迹图）
                # if len(points)>1:
                #     pygame.draw.aalines(screen, aalc,False,points)
        pygame.display.update()
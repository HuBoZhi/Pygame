# -*- coding: utf-8 -*- 
# Time : 2019/1/30 21:15 
# Author : hubozhi
import pygame
from pygame.locals import *
from sys import exit

if __name__ == "__main__":
    pygame.init()
    SCREEN_SIZE = (640, 480)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

    font = pygame.font.SysFont("arial", 16)
    font_height = font.get_linesize()
    event_text = []

    while True:
        event = pygame.event.wait()

        event_text.append(str(event))# 获得事件的名称

        event_text = event_text[int(-SCREEN_SIZE[1] / font_height):]

        # 这个切片操作保证了event_text里面只保留一个屏幕的文字
        # my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')
        # 你也可以像下面这样写，看起来比较清晰（但字变多了……）
        my_event = pygame.event.Event(KEYDOWN, {"key": K_SPACE, "mod": 0, "unicode": u' '})


        if event.type == QUIT:
            exit()
        # 将模拟的操作加入到队列的最后
        # event_text.append('my====='+str(my_event))
        pygame.event.post(my_event)#注意：该种写法需要在退出判断的后面，否则退出操作会被覆盖

        screen.fill((255, 255, 255))

        y = SCREEN_SIZE[1] - font_height
        # 找一个合适的起笔位置，最下面开始但是要留一行的空
        for text in reversed(event_text):
            screen.blit(font.render(text, True, (0, 0, 0)), (0, y))

            y -= font_height
            # 把笔提一行

        pygame.display.update()
    pass
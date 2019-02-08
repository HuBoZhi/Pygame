# -*- coding: utf-8 -*- 
# Time : 2019/1/31 12:25 
# Author : hubozhi
import pygame

if __name__ == "__main__":
    my_name = "Will McGugan"

    pygame.init()
    # my_font = pygame.font.SysFont("my_font.ttf", 64)
    my_font = pygame.font.SysFont('./font/华文中宋.ttf',64)
    name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(name_surface, "xxx.png")
    pass
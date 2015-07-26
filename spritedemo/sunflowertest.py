# _*_ coding:utf-8 _*_
import pygame
from spritedemo.sunflower import SunFlower

__author__ = 'Administrator'

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
sun = SunFlower()

clock = pygame.time.Clock()
while True:
    screen.fill((255, 255, 255))
    passed_time = clock.tick(30)
    sun.update(passed_time)
    screen.blit(sun.image, sun.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
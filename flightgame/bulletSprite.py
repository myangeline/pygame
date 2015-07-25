# _*_ coding:utf-8 _*_
__author__ = 'Administrator'
import pygame


class BulletSprite(pygame.sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
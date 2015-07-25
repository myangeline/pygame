# _*_ coding:utf-8 _*_
import random
import pygame

__author__ = 'Administrator'


class Plane():
    def __init__(self, width, height, value, image, type):
        self.width = width
        self.height = height
        self.value = value
        self.image = image
        self.type = type
        self.rect = pygame.Rect(self.image.get_rect())
        # self.position = [random.randint(0, 450 - self.width), -self.height / 2]


class Hero(Plane):

    def __init__(self, width, height, value, image, type, position):
        Plane.__init__(self, width, height, value, image, type)
        self.position = position
        self.keys = [False, False, False, False]

    def deal_keydown(self, event):
        if event.key == pygame.K_w:
            self.keys[0] = True
        elif event.key == pygame.K_a:
            self.keys[1] = True
        elif event.key == pygame.K_s:
            self.keys[2] = True
        elif event.key == pygame.K_d:
            self.keys[3] = True

    def deal_keyup(self, event):
        if event.key == pygame.K_w:
            self.keys[0] = False
        elif event.key == pygame.K_a:
            self.keys[1] = False
        elif event.key == pygame.K_s:
            self.keys[2] = False
        elif event.key == pygame.K_d:
            self.keys[3] = False

    def move(self, step=5):
        if self.keys[0]:
            self.position[1] -= step
        elif self.keys[2]:
            self.position[1] += step
        if self.keys[1]:
            self.position[0] -= step
        elif self.keys[3]:
            self.position[0] += step


class EnemyPlane(Plane):
    def __init__(self, width, height, value, image, type):
        Plane.__init__(self, width, height, value, image, type)
        self.position = [random.randint(0, 450 - self.width), -self.height / 2]

    def move(self, step=3):
        if self.position[1] > 650:
            self.value = 0
        self.position[1] += step
# _*_ coding:utf-8 _*_
import random
from plane import Hero, EnemyPlane
from parser_xml import doxml

__author__ = 'Administrator'

import pygame


def item_to_int(array=[]):
    arr = []
    for a in array:
        arr.append(int(a))
    return arr


pygame.init()
screen = pygame.display.set_mode((450, 650), 0, 32)
pygame.display.set_caption(u'飞机大战'.encode('utf-8'))

plane = pygame.image.load('resources/plane.png').convert_alpha()
pos = doxml('resources/plane.xml')

# 背景图片
bg1 = pygame.image.load('resources/bg_01.png')

hero_1_p = pos['hero_1']
hero_1_p = item_to_int(hero_1_p)
hero_1 = plane.subsurface(pygame.Rect((hero_1_p[2], hero_1_p[3]), (hero_1_p[0], hero_1_p[1])))
hero_1_pos = [200, 580]

# enemy_s
enemy_s_p = item_to_int(pos['enemy_s'])
enemy_s = plane.subsurface(pygame.Rect((enemy_s_p[2], enemy_s_p[3]), (enemy_s_p[0], enemy_s_p[1])))
# enemy_s_rect = pygame.Rect(enemy_s.get_rect())


hero = Hero(hero_1_p[0], hero_1_p[1], 100, hero_1, 0, hero_1_pos)

# 敌机保存列表
enemyPlane = EnemyPlane(enemy_s_p[0], enemy_s_p[1], 100, enemy_s, 1)
smallenemy = [enemyPlane]
midenemy = []
bigenemy = []

enemytimer = [100, 200, 300]
enemytimers = [0, 0, 0]


while True:
    for i in range(3):
        enemytimer[i] -= 1
    screen.fill(0)
    screen.blit(bg1, (0, 0))
    screen.blit(hero.image, hero.position)

    if not enemytimer[0]:
        smallenemy.append(EnemyPlane(enemy_s_p[0], enemy_s_p[1], 100, enemy_s, 1))
        enemytimer[0] = 100 - (enemytimers[0] * 2)
        enemytimers[0] = 35 if enemytimers[0] > 35 else enemytimers[0] + 5
    index = 0
    for enemy in smallenemy:
        if not enemy.value:
            smallenemy.pop(index)
        enemy.move()
        index += 1
    for enemy in smallenemy:
        screen.blit(enemy.image, enemy.position)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            hero.deal_keydown(event)

        if event.type == pygame.KEYUP:
            hero.deal_keyup(event)

    hero.move()
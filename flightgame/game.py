# _*_ coding:utf-8 _*_
import random
from parser_xml import doxml

__author__ = 'Administrator'
import pygame


def item_to_int(array=[]):
    arr = []
    for a in array:
        arr.append(int(a))
    return arr


pygame.init()

keys = [False, False, False, False]

screen = pygame.display.set_mode((450, 650), 0, 32)
pygame.display.set_caption(u'飞机大战'.encode('utf-8'))

plane = pygame.image.load('resources/plane.png').convert_alpha()
pos = doxml('resources/plane.xml')

# hero_1
hero_1_p = pos['hero_1']
hero_1_p = item_to_int(hero_1_p)
hero_1 = plane.subsurface(pygame.Rect((hero_1_p[2], hero_1_p[3]), (hero_1_p[0], hero_1_p[1])))
hero_1_pos = [200, 580]

# bullet_1 蓝色
bullet_1_p = item_to_int(pos['bullet_1'])
bullet_1 = plane.subsurface(pygame.Rect((bullet_1_p[2], bullet_1_p[3]), (bullet_1_p[0], bullet_1_p[1])))
bullet_1_pos = [hero_1_pos[0] + hero_1_p[0] / 2 - bullet_1_p[0] / 2 + 1, hero_1_pos[1] - bullet_1_p[1]]
bullet_1_rect = pygame.Rect(bullet_1.get_rect())

# bullet_0 橙色
bullet_0_p = item_to_int(pos['bullet_0'])
bullet_0 = plane.subsurface(pygame.Rect((bullet_0_p[2], bullet_0_p[3]), (bullet_0_p[0], bullet_0_p[1])))

# 背景图片
bg1 = pygame.image.load('resources/bg_01.png')

# enemy_s
enemy_s_p = item_to_int(pos['enemy_s'])
enemy_s = plane.subsurface(pygame.Rect((enemy_s_p[2], enemy_s_p[3]), (enemy_s_p[0], enemy_s_p[1])))
enemy_s_rect = pygame.Rect(enemy_s.get_rect())

# enemy_m
enemy_m_p = item_to_int(pos['enemy_m'])
enemy_m = plane.subsurface(pygame.Rect((enemy_m_p[2], enemy_m_p[3]), (enemy_m_p[0], enemy_m_p[1])))
enemy_m_rect = pygame.Rect(enemy_m.get_rect())

# enemy_b
enemy_b_p = item_to_int(pos['enemy_b'])
enemy_b = plane.subsurface(pygame.Rect((enemy_b_p[2], enemy_b_p[3]), (enemy_b_p[0], enemy_b_p[1])))
enemy_b_rect = pygame.Rect(enemy_b.get_rect())

bullet_1_time = 15
bullet_1_array = [bullet_1_pos]

enemytimer = [100, 200, 300]
enemytimers = [0, 0, 0]

# 敌机的发子弹概率
enemy_s_g = [1, 4, 7, 9]
enemy_m_g = [1, 4]
enemy_b_g = [1]

# 敌机子弹的保存列表
enemy_s_array = []
enemy_m_array = []
enemy_b_array = []

# 敌机保存列表
smallenemy = [[100, 0]]
midenemy = []
bigenemy = []

while True:
    bullet_1_time -= 1
    for i in range(3):
        enemytimer[i] -= 1

    screen.fill(0)
    screen.blit(bg1, (0, 0))
    screen.blit(hero_1, hero_1_pos)
    # 绘制hero_1子弹
    if not bullet_1_time:
        bullet_1_array.append([hero_1_pos[0] + hero_1_p[0] / 2 - bullet_1_p[0] / 2 + 1, hero_1_pos[1] - bullet_1_p[1]])
        bullet_1_time = 15
    index = 0
    for bullet_pos in bullet_1_array:
        if bullet_pos[1] < 0:
            bullet_1_array.pop(index)
        bullet_pos[1] -= 5
        index += 1
    for bullet_pos in bullet_1_array:
        screen.blit(bullet_1, bullet_pos)

    # 绘制小敌机
    if not enemytimer[0]:
        smallenemy.append([random.randint(0, 410), -20])
        enemytimer[0] = 100 - (enemytimers[0] * 2)
        enemytimers[0] = 35 if enemytimers[0] > 35 else enemytimers[0] + 5

    index = 0
    for se in smallenemy:
        if se[1] > 650:
            smallenemy.pop(index)
        se[1] += 3

        enemy_s_rect.left = se[0]
        enemy_s_rect.top = se[1]
        index_bullet = 0
        for bullet in bullet_1_array:
            bullet_1_rect.left = bullet[0]
            bullet_1_rect.top = bullet[1]
            if enemy_s_rect.colliderect(bullet_1_rect):
                bullet_1_array.pop(index_bullet)
                smallenemy.pop(index)
        index += 1
        # 随机是否发射子弹
        # r = random.randint(1, 500)
        # if r in enemy_s_g:
        #     enemy_s_array.append([se[0] + 15, se[1] + 27])
    index = 0
    # for bullet in enemy_s_array:
    #     if bullet[1] > 650:
    #         enemy_s_array.pop(index)
    #     bullet[1] += 5
    #     index += 1

    for se in smallenemy:
        screen.blit(enemy_s, se)

    for bullet in enemy_s_array:
        screen.blit(bullet_0, bullet)

    # 绘制中等敌机
    if not enemytimer[1]:
        midenemy.append([random.randint(0, 380), -40])
        enemytimer[1] = 200 - (enemytimers[1] * 2)
        enemytimers[1] = 55 if enemytimers[1] > 55 else enemytimers[1] + 5
    index = 0
    for me in midenemy:
        if me[1] > 650:
            midenemy.pop(index)
        me[1] += 2
        index += 1
    for me in midenemy:
        screen.blit(enemy_m, me)

    # 绘制大飞机
    if not enemytimer[2]:
        bigenemy.append([random.randint(0, 340), -100])
        enemytimer[2] = 300 - (enemytimers[2] * 2)
        enemytimers[2] = 65 if enemytimers[2] > 65 else enemytimers[2] + 5
    index = 0
    for be in bigenemy:
        if be[1] > 650:
            bigenemy.pop(index)
        be[1] += 1
        index += 1
    for be in bigenemy:
        screen.blit(enemy_b, be)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    if keys[0]:
        hero_1_pos[1] -= 5
    elif keys[2]:
        hero_1_pos[1] += 5
    if keys[1]:
        hero_1_pos[0] -= 5
    elif keys[3]:
        hero_1_pos[0] += 5

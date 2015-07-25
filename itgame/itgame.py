# _*_coding:utf-8_*_
import math
import random

__author__ = 'Administrator'

import pygame

pygame.init()
width, height = 640, 480
keys = [False, False, False, False]
playerpos = [100, 240]
# 记录玩家射击精度，射击次数、命中次数
acc = [0, 0]
arrows = []
# 命中率
accuracy = 0

# 记录獾的数据
badtimer = 100
rest = 0
badguys = [[640, 100]]
healthvalue = 194

screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption(u'城堡保卫战'.encode('utf-8'))

player = pygame.image.load('resources/images/dude.png')
player_w, player_h = player.get_width(), player.get_height()

grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')
arrow = pygame.image.load('resources/images/bullet.png')
bulletrect = pygame.Rect(arrow.get_rect())
badguyimg1 = pygame.image.load('resources/images/badguy.png')
badguyimg = badguyimg1
badrect = pygame.Rect(badguyimg.get_rect())

healthbar = pygame.image.load('resources/images/healthbar.png')
health = pygame.image.load('resources/images/health.png')

youwin = pygame.image.load('resources/images/youwin.png')
gameover = pygame.image.load('resources/images/gameover.png')

# 加载音频
pygame.mixer.init()

hit = pygame.mixer.Sound('resources/audio/explode.wav')
enemy = pygame.mixer.Sound('resources/audio/enemy.wav')
shoot = pygame.mixer.Sound('resources/audio/shoot.wav')
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
# 设置背景音乐，循环播放
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

running = 1
exitcode = 0

# 全屏
fullscreen = False

while running:
    badtimer -= 1

    screen.fill(0)

    for x in range(width / grass.get_width() + 1):
        for y in range(height / grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))

    for i in range(4):
        screen.blit(castle, (0, i * 105 + 30))

    # screen.blit(player, playerpos)
    mousepos = pygame.mouse.get_pos()
    angle = math.atan2(mousepos[1] - (playerpos[1] + 32), mousepos[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playertranspos = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playertranspos)

    # 绘制 箭
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            aow = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
            screen.blit(aow, (projectile[1], projectile[2]))

    # 产生 獾
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        badtimer = 100 - (rest * 2)
        rest = 35 if rest >= 35 else rest + 5
    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)

        # 炸毁城堡
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(5, 20)
            badguys.pop(index)

        index_bullet = 0
        for bullet in arrows:
            bulletrect.left = bullet[1]
            bulletrect.top = bullet[2]
            if badrect.colliderect(bulletrect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index_bullet)
            index_bullet += 1

        badguy[0] -= 7
        index += 1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 绘制时钟
    font = pygame.font.Font(None, 24)
    time = pygame.time.get_ticks()
    survivedtext = font.render(str((90000 - time) / 60000) + ":" + str((90000 - time) / 1000 % 60).zfill(2), True,
                               (0, 0, 0))
    textrect = survivedtext.get_rect()
    textrect.topright = [635, 5]
    screen.blit(survivedtext, textrect)

    # 绘制血条
    screen.blit(healthbar, (5, 5))
    for h in range(healthvalue):
        screen.blit(health, (h + 8, 8))

    # 更新屏幕 update和flip的效果差不多好像
    # pygame.display.flip()
    pygame.display.update()

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
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((width, height), 0, 32)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(position[1] - (playertranspos[1] + 32), position[0] - (playertranspos[0] + 26)),
                           playertranspos[0] + 32, playertranspos[1] + 32])

    if keys[0]:
        playerpos[1] -= 5
        if playerpos[1] < 0:
            playerpos[1] = 0
    elif keys[2]:
        playerpos[1] += 5
        if playerpos[1] > height - player_h:
            playerpos[1] = height - player_h
    if keys[1]:
        playerpos[0] -= 5
        if playerpos[0] < 0:
            playerpos[0] = 0
    elif keys[3]:
        playerpos[0] += 5
        if playerpos[0] > width - player_w:
            playerpos[0] = width - player_w

    # 判断输赢
    if pygame.time.get_ticks() >= 90000:
        running = 0
        # win
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        # lose
        exitcode = 0
    if acc[1] != 0:
        accuracy = round(acc[0] * 1.0 / acc[1] * 100, 2)

pygame.font.init()
# font = pygame.font.Font(None, 24)
# 为了显示中文需要设置中文字体，可以使用字体文件和系统字体
font = pygame.font.SysFont('楷体', 24)
if exitcode:
    text = font.render(u'命中率：' + str(accuracy) + '%', True, (0, 255, 0))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery + 24
    screen.blit(youwin, (0, 0))
    screen.blit(text, textrect)
else:
    text = font.render(u'命中率：' + str(accuracy) + '%', True, (255, 0, 0))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery + 24
    screen.blit(gameover, (0, 0))
    screen.blit(text, textrect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    pygame.display.flip()
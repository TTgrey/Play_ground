from typing import Dict
import pygame
# Программа "Привет!" для проверки работы с библиотекой pygame 
import pygame, sys
from pygame.locals import *
pygame.init()
# Задание констант игры
WIN_WIDTH = 700
WIN_HEIGHT = 700
FPS = 40

vrem = 0
DID_TIME =0
#персонаж
#тут находятся переменные: -характеристика персонажа, -лимит,
#  -переменая для сокращения не круглого значения для поддержания параметров на одной линии.
#стамина
speed_stamin = 0
Sstamin = 1.3
stamin = 130
maxstamin = 130
#хп
Shp = 1
hp = 100
maxhp = 100
#щит
shield = 100
Sshield = 1
MAXshield = 100
#
vcv = 0
vcv1 = 0
speed = 2
speedST = 3
speedgob = 4
spend_stamin = 1
# цвета  R    G    B
#Надо переназвать
DOOP = (0,10,0)
BLACK = (0,   0,   255)
WHITE = (255, 255, 255)
RED =   (255, 0,   0)
BLACK_BACKGROUND = (50,50,50)
BACKGROUND = (180,180,180)
# инициализация модулей pygame
pygame.init()
# создание окна рисования
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# имя в верхнем углу
pygame.display.set_caption('PLAY GROUND')
# создание таймера для контроля фпс
clock = pygame.time.Clock()
f = 0
x = 100
y =500
x1 =100
xhead = 100
yhead = 500
gob = pygame.Rect(100,100,30,30)
head = pygame.Rect(xhead,yhead,15,15)
#Для написания текста
#шрифт
TexT =pygame.font.SysFont("comicsansms",12)
TexT2 =pygame.font.SysFont("comicsansms",45)
#Я нашел как писать текст, но это надо доработать и возможно разобрать


#
def load_image(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect = image.get_rect(center=(x, y))

    transparent = image.get_at((0,0))
    image.set_colorkey(transparent)

    return image, rect

while True:
   
    The_SAY = TexT.render(str(round(hp)),1,DOOP,RED)
    The_SAY2 = TexT.render(str(round(stamin/Sstamin)),1,DOOP,BLACK)
    The_SAY3 = TexT2.render("ВЫ ПОГИБЛИ: "+str(DID_TIME),1,RED,BACKGROUND)
    # цикл обработки событий
    #   for y1 in range(ygob) and x1 in range(xgob):
      #  gob.move_ip((0, speedgob))
        #  y1 += speedgob
    #система вышла из строя 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
    #команды(надо усовершенствовать)
    G = pygame.key.get_pressed()

    vrem += 1
    if vrem == 40:
        vrem = 0
        if G[K_s]:
            stamin = 130
            print("player: stamin full")
        elif G[K_f]:
            hp = 100
            print("player: hp full")
        elif G[K_d]:
            sys.exit()
        elif G[K_x]:
            shield = 0
            print("player: nullify shield")
        elif G[K_c]:
            hp = 10
            print("player: nullify hp")
    #передвижение персонажа
    if G[K_UP] and DID_TIME==0:
        if G[K_LSHIFT] and stamin > 0:
            head.move_ip((0, -(speed +speedST)))
            stamin -= spend_stamin
            y -= speed
        else:
            head.move_ip((0, -speed))
            y -= speed
            speed_stamin = 1
    elif G[K_DOWN] and DID_TIME==0:
        if G[K_LSHIFT] and stamin > 0:
            head.move_ip((0, (speed +speedST)))
            stamin -= spend_stamin
            y += speed
        else:
            head.move_ip((0, speed))
            y += speed
            speed_stamin = 1
    elif G[K_RIGHT] and DID_TIME==0:
        if G[K_LSHIFT] and stamin > 0:
            head.move_ip(((speed +speedST),0))
            stamin -= spend_stamin
            x += speed
        else:
            head.move_ip((speed, 0))
            x += speed
            speed_stamin = 1
    elif G[K_LEFT] and DID_TIME==0:
        if G[K_LSHIFT] and stamin > 0:
            head.move_ip((-(speed +speedST),0 ))
            stamin -= spend_stamin
            x -= speed
        else:
            head.move_ip((-speed, 0))
            x -= speed
            speed_stamin = 1
    #трата и воспалнение единиц
    else:
        vcv += 1
        if vcv == 1:
            stamin += 0.4
            vcv = 0
    if speed_stamin == 1:
        stamin += 0.2
        speed_stamin = 0  
    if stamin < 0 or stamin == 0:
        hp -= 1 
    if shield < -1:
        shield = 0
    if stamin < 0:
        stamin = 0
    #смерть
    if hp < 1:
        DID_TIME = DID_TIME + 500
        hp = 1
        #sys.exit()
    if hp < -1:
        hp = 0
    if hp > maxhp:
        hp = maxhp 
    if stamin > maxstamin:
        stamin = maxstamin  
    if stamin == maxstamin:
        hp += 0.005
    if shield > MAXshield:
        hp-(MAXshield-shield)
        shield = MAXshield
    #телепортация
    #Надо доделать
    if head.bottom > (WIN_WIDTH+16):
        head.top = -15
    elif head.top < -16:
        head.bottom = WIN_HEIGHT +15
    elif head.left< -16:
        head.right = WIN_WIDTH +15
    elif head.right >  (WIN_WIDTH+16):
        head.left = -15
    #скрипт благодаря которому должено проходить востановление хп на определенной территории
    xd = xhead
    yd = yhead
    #if head.bottom>100 and head.top>100 and head.right<130 and head.left<130:
        #shield += 1
        # print("yes")
        
    # заливка экрана рисования
    screen.fill(WHITE)
    f += 1
    #Стабилизация линий показателей персонажей
    shield1 = (shield/Sshield)+20
    stamin2 = stamin
    stamin1 = (stamin2/Sstamin)+ 20
    hp1 = (hp/Shp)+ 20
    #персонаж
    pygame.draw.rect(screen,  RED, head)
    #отрисовка территории прохила
    #pygame.draw.rect(screen,  RED, gob)
    # типо обекты высвечевания данных
    pygame.draw.rect(screen,  BACKGROUND, ((0,0),(700,80)))
    pygame.draw.line(screen,  (110,110,110),(0,80),(700,80),3)
    pygame.draw.line(screen,  BLACK_BACKGROUND,(20,30),(120,30),20)
    pygame.draw.line(screen,  BLACK_BACKGROUND,(20,60),(118,60),20)
    #ОТресовка показателей персонажа
    pygame.draw.line(screen,  BLACK,(20,30),(stamin1,30),20)
    pygame.draw.line(screen,  RED,(20,60),(hp1,60),20)
    pygame.draw.line(screen,  (130,130,130),(20,70),(shield1,70),5)
    #текст!
    screen.blit(The_SAY,(60,51))
    screen.blit(The_SAY2,(60,22))
    #Отрисовка сообщения о смерти
    if DID_TIME > 0:
        DID_TIME -= 1
        screen.blit(The_SAY3,(200,10))
        #sys.exit()

    
    # обновление дисплея
    pygame.display.update()
    # установление задержки (скорости обновления кадров)
    clock.tick(FPS)

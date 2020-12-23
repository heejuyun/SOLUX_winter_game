# 초기화면 + 시작버튼
import pygame
import time
import sys

pad_width = 800
pad_height = 450

# 이미지 파일
bgImg = pygame.image.load("images/bg.png")
titleImg = pygame.image.load("images/title.png")
startImg = pygame.image.load("images/start.png")
quitImg = pygame.image.load("images/quit.png")
clickStartImg = pygame.image.load("images/clickstart.png")
clickQuitImg = pygame.image.load("images/clickquit.png")

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gamepad.blit(img_in, (x, y))

def runGame():
    global gamepad, clock

    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        gamepad.blit(bgImg, (0, 0)) # 배경 입히기

        titletext = gamepad.blit(titleImg, (100, 20))
        startButton = Button(startImg, 100, 300, 259, 131, clickStartImg, 100, 300, None)
        quitButton = Button(quitImg, 430, 305, 265, 134, clickQuitImg, 430, 305, quitgame)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('Magic Lab')

    clock = pygame.time.Clock()
    runGame()

def quitgame():
    pygame.quit()
    sys.exit()

initGame()

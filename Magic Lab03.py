# 게임화면+버튼 생성
import pygame
import time
import sys

pad_width = 800
pad_height = 450

# 이미지 파일
bgImg = pygame.image.load("images/bg.png")
titleImg = pygame.image.load("images/title.png")

startImg = pygame.image.load("images/start.png")
clickStartImg = pygame.image.load("images/clickstart.png")
quitImg = pygame.image.load("images/quit.png")
clickQuitImg = pygame.image.load("images/clickquit.png")

selectImg = pygame.image.load("images/select.png")

buttonImg1 = pygame.image.load("images/button1.png")
clickbuttonImg1 = pygame.image.load("images/clickbutton1.png")
buttonImg2 = pygame.image.load("images/button2.png")
clickbuttonImg2 = pygame.image.load("images/clickbutton2.png")
buttonImg3 = pygame.image.load("images/button3.png")
clickbuttonImg3 = pygame.image.load("images/clickbutton3.png")
buttonImg4 = pygame.image.load("images/button4.png")
clickbuttonImg4 = pygame.image.load("images/clickbutton4.png")
buttonImg5 = pygame.image.load("images/button5.png")
clickbuttonImg5 = pygame.image.load("images/clickbutton5.png")
buttonImg6 = pygame.image.load("images/button6.png")
clickbuttonImg6 = pygame.image.load("images/clickbutton6.png")
buttonImg7 = pygame.image.load("images/button7.png")
clickbuttonImg7 = pygame.image.load("images/clickbutton7.png")
buttonImg8 = pygame.image.load("images/button8.png")
clickbuttonImg8 = pygame.image.load("images/clickbutton8.png")
buttonImg9 = pygame.image.load("images/button9.png")
clickbuttonImg9 = pygame.image.load("images/clickbutton9.png")
buttonImg10 = pygame.image.load("images/button10.png")
clickbuttonImg10 = pygame.image.load("images/clickbutton10.png")
buttonImg11 = pygame.image.load("images/button11.png")
clickbuttonImg11 = pygame.image.load("images/clickbutton11.png")
buttonImg12 = pygame.image.load("images/button12.png")
clickbuttonImg12 = pygame.image.load("images/clickbutton12.png")
buttonImg13 = pygame.image.load("images/button13.png")
clickbuttonImg13 = pygame.image.load("images/clickbutton13.png")
buttonImg14 = pygame.image.load("images/button14.png")
clickbuttonImg14 = pygame.image.load("images/clickbutton14.png")
buttonImg15 = pygame.image.load("images/button15.png")
clickbuttonImg15 = pygame.image.load("images/clickbutton15.png")
buttonImg16 = pygame.image.load("images/button16.png")
clickbuttonImg16 = pygame.image.load("images/clickbutton16.png")

noonsongImg = pygame.image.load("images/noonsong.png")



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
        startButton = Button(startImg, 100, 300, 259, 131, clickStartImg, 100, 300, selectScreen)
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

def selectScreen():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gamepad.blit(selectImg, (0, 0))
        button1 = Button(buttonImg1, 82, 43, 64, 64, clickbuttonImg1, 82, 43, None)
        button2 = Button(buttonImg2, 188, 43, 64, 64, clickbuttonImg2, 188, 43, None)
        button3 = Button(buttonImg3, 294, 43, 64, 64, clickbuttonImg3, 294, 43, None)
        button4 = Button(buttonImg4, 442, 43, 64, 64, clickbuttonImg4, 442, 43, None)
        button5 = Button(buttonImg5, 548, 43, 64, 64, clickbuttonImg5, 548, 43, None)
        button6 = Button(buttonImg6, 654, 43, 64, 64, clickbuttonImg6, 654, 43, None)
        button7 = Button(buttonImg7, 82, 193, 64, 64, clickbuttonImg7, 82, 193, None)
        button8 = Button(buttonImg8, 188, 193, 64, 64, clickbuttonImg8, 188, 193, None)
        button9 = Button(buttonImg9, 548, 193, 64, 64, clickbuttonImg9, 548, 193, None)
        button10 = Button(buttonImg10, 654, 193, 64, 64, clickbuttonImg10, 654, 193, None)
        button11 = Button(buttonImg11, 82, 343, 64, 64, clickbuttonImg11, 82, 343, None)
        button12 = Button(buttonImg12, 188, 343, 64, 64, clickbuttonImg12, 188, 343, None)
        button13 = Button(buttonImg13, 294, 343, 64, 64, clickbuttonImg13, 294, 343, None)
        button14 = Button(buttonImg14, 442, 343, 64, 64, clickbuttonImg14, 442, 343, None)
        button15 = Button(buttonImg15, 548, 343, 64, 64, clickbuttonImg15, 548, 343, None)
        button16 = Button(buttonImg16, 654, 343, 64, 64, clickbuttonImg16, 654, 343, None)
        gamepad.blit(noonsongImg, (257, 82))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def quitgame():
    pygame.quit()
    sys.exit()

initGame()

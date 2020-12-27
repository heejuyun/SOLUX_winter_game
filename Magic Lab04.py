# 버튼 눌리게 하기+완료 버튼 누르면 결과화면 생성
import pygame
import time
import sys

pad_width = 800
pad_height = 450
number1 = -1
number2 = -1
number3 = -1
number4 = -1
number5 = -1
number6 = -1

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

donebuttonImg = pygame.image.load("images/donebutton.png")
clickdonebuttonImg = pygame.image.load("images/clickdonebutton.png")

resultImg = pygame.image.load("images/result.png")

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

class Button1:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number1
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number1 = num
        elif number1 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number2
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number2 = num
        elif number2 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button3:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number3
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number3 = num
        elif number3 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button4:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number4
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number4 = num
        elif number4 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button5:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number5
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number5 = num
        elif number5 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button6:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number6
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number6 = num
        elif number6 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

def runGame():
    global gamepad, clock

    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        gamepad.blit(bgImg, (0, 0)) # 시작화면 배경 입히기

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

        gamepad.blit(selectImg, (0, 0)) # 게임화면 배경 입히기
        button1 = Button1(buttonImg1, 82, 43, 64, 64, clickbuttonImg1, 82, 43, 1)
        button2 = Button1(buttonImg2, 188, 43, 64, 64, clickbuttonImg2, 188, 43, 2)
        button3 = Button1(buttonImg3, 294, 43, 64, 64, clickbuttonImg3, 294, 43, 3)
        button4 = Button2(buttonImg4, 442, 43, 64, 64, clickbuttonImg4, 442, 43, 4)
        button5 = Button2(buttonImg5, 548, 43, 64, 64, clickbuttonImg5, 548, 43, 5)
        button6 = Button2(buttonImg6, 654, 43, 64, 64, clickbuttonImg6, 654, 43, 6)
        button7 = Button3(buttonImg7, 82, 193, 64, 64, clickbuttonImg7, 82, 193, 7)
        button8 = Button3(buttonImg8, 188, 193, 64, 64, clickbuttonImg8, 188, 193, 8)
        button9 = Button4(buttonImg9, 548, 193, 64, 64, clickbuttonImg9, 548, 193, 9)
        button10 = Button4(buttonImg10, 654, 193, 64, 64, clickbuttonImg10, 654, 193, 10)
        button11 = Button5(buttonImg11, 82, 343, 64, 64, clickbuttonImg11, 82, 343, 11)
        button12 = Button5(buttonImg12, 188, 343, 64, 64, clickbuttonImg12, 188, 343, 12)
        button13 = Button5(buttonImg13, 294, 343, 64, 64, clickbuttonImg13, 294, 343, 13)
        button14 = Button6(buttonImg14, 442, 343, 64, 64, clickbuttonImg14, 442, 343, 14)
        button15 = Button6(buttonImg15, 548, 343, 64, 64, clickbuttonImg15, 548, 343, 15)
        button16 = Button6(buttonImg16, 654, 343, 64, 64, clickbuttonImg16, 654, 343, 16)
        gamepad.blit(noonsongImg, (257, 82))

        donebutton = Button(donebuttonImg, 368, 378, 64, 64, clickdonebuttonImg, 368, 378, resultScreen)

        pygame.display.update()
        clock.tick(60)

def resultScreen():
    result = True

    while result:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gamepad.blit(resultImg, (0, 0)) # 결과화면 배경 입히기
        
        pygame.display.update()
        clock.tick(60)

def quitgame():
    pygame.quit()
    sys.exit()

initGame()

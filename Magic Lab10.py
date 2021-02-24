# 경우별 그림 지정
import pygame
import time
import sys

pygame.init()

game_font = pygame.font.Font(None, 40)

total_time = 15 # 15초

pad_width = 800
pad_height = 450

number1 = -1
number2 = -1
number3 = -1
number4 = -1
number5 = -1

hair = 0
body = 0
character = 0
concept = 0
deco = 0

noonsong_y = 82
cnt = 0

# 이미지 파일
bgImg = pygame.image.load("images/bg1.png")
titleImg = pygame.image.load("images/title.png")

startImg = pygame.image.load("images/start_.png")
clickStartImg = pygame.image.load("images/clickstart_.png")
quitImg = pygame.image.load("images/quit_.png")
clickQuitImg = pygame.image.load("images/clickquit_.png")
restartImg = pygame.image.load("images/restart_.png")
clickRestartImg = pygame.image.load("images/clickrestart_.png")


selectImg = pygame.image.load("images/bg1.png")

buttonImg1 = pygame.image.load("images/1.png")
clickbuttonImg1 = pygame.image.load("images/1_.png")
buttonImg2 = pygame.image.load("images/2.png")
clickbuttonImg2 = pygame.image.load("images/2_.png")
buttonImg3 = pygame.image.load("images/3.png")
clickbuttonImg3 = pygame.image.load("images/3_.png")
buttonImg4 = pygame.image.load("images/4.png")
clickbuttonImg4 = pygame.image.load("images/4_.png")
buttonImg5 = pygame.image.load("images/5.png")
clickbuttonImg5 = pygame.image.load("images/5_.png")
buttonImg6 = pygame.image.load("images/6.png")
clickbuttonImg6 = pygame.image.load("images/6_.png")
buttonImg7 = pygame.image.load("images/7.png")
clickbuttonImg7 = pygame.image.load("images/7_.png")
buttonImg8 = pygame.image.load("images/8.png")
clickbuttonImg8 = pygame.image.load("images/8_.png")
buttonImg9 = pygame.image.load("images/9.png")
clickbuttonImg9 = pygame.image.load("images/9_.png")
buttonImg10 = pygame.image.load("images/10.png")
clickbuttonImg10 = pygame.image.load("images/10_.png")
buttonImg11 = pygame.image.load("images/11.png")
clickbuttonImg11 = pygame.image.load("images/11_.png")
buttonImg12 = pygame.image.load("images/12.png")
clickbuttonImg12 = pygame.image.load("images/12_.png")
buttonImg13 = pygame.image.load("images/13.png")
clickbuttonImg13 = pygame.image.load("images/13_.png")
buttonImg14 = pygame.image.load("images/14.png")
clickbuttonImg14 = pygame.image.load("images/14_.png")

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
        global number1, hair
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number1 = num
                hair = num
        elif number1 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number2, body
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number2 = num
                body = num
        elif number2 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button3:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number3, character
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number3 = num
                character = num
        elif number3 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button4:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number4, concept
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number4 = num
                concept = num
        elif number4 == num:
            gamepad.blit(img_act, (x_act, y_act))
        else:
            gamepad.blit(img_in, (x, y))

class Button5:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, num):
        global number5, deco
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x + width > mouse[0] > x) and (y + height > mouse[1] > y):
            gamepad.blit(img_act, (x_act, y_act))
            if click[0]:
                number5 = num
                deco = num
        elif number5 == num:
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
        startButton = Button(startImg, 195, 300, 205, 88, clickStartImg, 185, 295, selectScreen)
        quitButton = Button(quitImg, 435, 300, 160, 88, clickQuitImg, 425, 295, quitgame)

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
    global noonsong_y, cnt, hair, body, character, concept, deco, number1, number2, number3, number4, number5, total_time
    select = True
    
    number1 = -1
    number2 = -1
    number3 = -1
    number4 = -1
    number5 = -1
    
    hair = 0
    body = 0
    character = 0
    concept = 0
    deco = 0

    start_ticks = pygame.time.get_ticks()

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gamepad.blit(selectImg, (0, 0)) # 게임화면 배경 입히기
        
        button1 = Button1(buttonImg1, 82, 43, 100, 100, clickbuttonImg1, 82, 43, 1)
        button2 = Button1(buttonImg2, 188, 43, 100, 100, clickbuttonImg2, 188, 43, 2)
        button3 = Button1(buttonImg3, 294, 43, 100, 100, clickbuttonImg3, 294, 43, 3)

        button4 = Button2(buttonImg4, 442, 43, 100, 100, clickbuttonImg4, 442, 43, 1)
        button5 = Button2(buttonImg5, 548, 43, 100, 100, clickbuttonImg5, 548, 43, 2)

        button6 = Button3(buttonImg6, 654, 43, 100, 100, clickbuttonImg6, 654, 43, 1)
        button7 = Button3(buttonImg7, 82, 193, 100, 100, clickbuttonImg7, 82, 193, 2)

        button8 = Button4(buttonImg8, 188, 193, 100, 100, clickbuttonImg8, 188, 193, 1)
        button9 = Button4(buttonImg9, 548, 193, 100, 100, clickbuttonImg9, 548, 193, 2)
        button10 = Button4(buttonImg10, 654, 193, 100, 100, clickbuttonImg10, 654, 193, 3)
        button11 = Button4(buttonImg11, 82, 343, 100, 100, clickbuttonImg11, 82, 343, 4)

        button12 = Button5(buttonImg12, 188, 343, 100, 100, clickbuttonImg12, 188, 343, 1)
        button13 = Button5(buttonImg13, 294, 343, 100, 100, clickbuttonImg13, 294, 343, 2)
        button14 = Button5(buttonImg14, 442, 343, 100, 100, clickbuttonImg14, 442, 343, 3)

        gamepad.blit(noonsongImg, (257, noonsong_y))

        donebutton = Button(donebuttonImg, 368, 378, 64, 64, clickdonebuttonImg, 368, 378, resultScreen)

        # 눈송이 움직이기
        if cnt == 0:
            noonsong_y -= 0.3
            if noonsong_y < 55:
                cnt = 1
        elif cnt == 1:
            noonsong_y += 0.3
            if noonsong_y > 82:
                cnt = 0

        elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000 # ms -> s

        timer = game_font.render("Time : {}".format(str(int(total_time - elapsed_time))), True, (255, 255, 255))

        gamepad.blit(timer, (10, 10))

        if total_time - elapsed_time <= 0:
            resultScreen()

        pygame.display.update()
        clock.tick(60)

def resultScreen():
    global hair, body, character, concept, deco
    result = True

    while result:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gamepad.blit(resultImg, (0, 0)) # 결과화면 배경 입히기

        if(hair == 0 or body == 0 or character == 0 or concept == 0 or deco == 0):
            gamepad.blit(pygame.image.load("images/noonsong0.png"), (330, 110)) # case 0
        elif (hair == 1 and body == 1 and character == 1 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong1.png"), (257, 82)) # case 1
        elif (hair == 1 and body == 1 and character == 2 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong2.png"), (257, 82)) # case 2
        elif (hair == 1 and body == 2 and character == 1 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 3
        elif (hair == 1 and body == 2 and character == 2 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong4.png"), (257, 82)) # case 4
        elif (hair == 1 and body == 1 and character == 1 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong5.png"), (257, 82)) # case 5
        elif (hair == 1 and body == 1 and character == 2 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong6.png"), (257, 82)) # case 6
        elif (hair == 1 and body == 2 and character == 1 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong7.png"), (257, 82)) # case 7
        elif (hair == 1 and body == 2 and character == 2 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong8.png"), (257, 82)) # case 8
        elif (hair == 1 and body == 1 and character == 1 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong9.png"), (257, 82)) # case 9
        elif (hair == 1 and body == 1 and character == 2 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong10.png"), (257, 82)) # case 10
        elif (hair == 1 and body == 2 and character == 1 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong11.png"), (257, 82)) # case 11
        elif (hair == 1 and body == 2 and character == 2 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong12.png"), (257, 82)) # case 12
        elif (hair == 2 and body == 1 and character == 1 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong13.png"), (257, 82)) # case 13
        elif (hair == 2 and body == 1 and character == 2 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong14.png"), (257, 82)) # case 14
        elif (hair == 2 and body == 2 and character == 1 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 15
        elif (hair == 2 and body == 2 and character == 2 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong2.png"), (257, 82)) # case 16
        elif (hair == 2 and body == 1 and character == 1 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong13.png"), (257, 82)) # case 17
        elif (hair == 2 and body == 1 and character == 2 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong4.png"), (257, 82)) # case 18
        elif (hair == 2 and body == 2 and character == 1 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 19
        elif (hair == 2 and body == 2 and character == 2 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong20.png"), (257, 82)) # case 20
        elif (hair == 2 and body == 1 and character == 1 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong14.png"), (257, 82)) # case 21
        elif (hair == 2 and body == 1 and character == 2 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 22
        elif (hair == 2 and body == 2 and character == 1 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 23
        elif (hair == 2 and body == 2 and character == 2 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 24
        elif (hair == 3 and body == 1 and character == 1 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong20.png"), (257, 82)) # case 25
        elif (hair == 3 and body == 1 and character == 2 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 26
        elif (hair == 3 and body == 2 and character == 1 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 27
        elif (hair == 3 and body == 2 and character == 2 and concept == 1 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 28
        elif (hair == 3 and body == 1 and character == 1 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 29
        elif (hair == 3 and body == 1 and character == 2 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 30
        elif (hair == 3 and body == 2 and character == 1 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong7.png"), (257, 82)) # case 31
        elif (hair == 3 and body == 2 and character == 2 and concept == 1 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong12.png"), (257, 82)) # case 32
        elif (hair == 3 and body == 1 and character == 1 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 33
        elif (hair == 3 and body == 1 and character == 2 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong34.png"), (257, 82)) # case 34
        elif (hair == 3 and body == 2 and character == 1 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 35
        elif (hair == 3 and body == 2 and character == 2 and concept == 1 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong34.png"), (257, 82)) # case 36
        elif (hair == 1 and body == 1 and character == 1 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong37.png"), (257, 82)) # case 37
        elif (hair == 1 and body == 1 and character == 2 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong8.png"), (257, 82)) # case 38
        elif (hair == 1 and body == 2 and character == 1 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong39.png"), (257, 82)) # case 39
        elif (hair == 1 and body == 2 and character == 2 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 40
        elif (hair == 1 and body == 1 and character == 1 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 41
        elif (hair == 1 and body == 1 and character == 2 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong42.png"), (257, 82)) # case 42
        elif (hair == 1 and body == 2 and character == 1 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong39.png"), (257, 82)) # case 43
        elif (hair == 1 and body == 2 and character == 2 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 44
        elif (hair == 1 and body == 1 and character == 1 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 45
        elif (hair == 1 and body == 1 and character == 2 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 46
        elif (hair == 1 and body == 2 and character == 1 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 47
        elif (hair == 1 and body == 2 and character == 2 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 48
        elif (hair == 2 and body == 1 and character == 1 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong49.png"), (257, 82)) # case 49
        elif (hair == 2 and body == 1 and character == 2 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 50
        elif (hair == 2 and body == 2 and character == 1 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 51
        elif (hair == 2 and body == 2 and character == 2 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 52
        elif (hair == 2 and body == 1 and character == 1 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 53
        elif (hair == 2 and body == 1 and character == 2 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong42.png"), (257, 82)) # case 54
        elif (hair == 2 and body == 2 and character == 1 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 55
        elif (hair == 2 and body == 2 and character == 2 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong56.png"), (257, 82)) # case 56
        elif (hair == 2 and body == 1 and character == 1 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 57
        elif (hair == 2 and body == 1 and character == 2 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 58
        elif (hair == 2 and body == 2 and character == 1 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 59
        elif (hair == 2 and body == 2 and character == 2 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 60
        elif (hair == 3 and body == 1 and character == 1 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong37.png"), (257, 82)) # case 61
        elif (hair == 3 and body == 1 and character == 2 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 62
        elif (hair == 3 and body == 2 and character == 1 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 63
        elif (hair == 3 and body == 2 and character == 2 and concept == 2 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong64.png"), (257, 82)) # case 64
        elif (hair == 3 and body == 1 and character == 1 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 65
        elif (hair == 3 and body == 1 and character == 2 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 66
        elif (hair == 3 and body == 2 and character == 1 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 67
        elif (hair == 3 and body == 2 and character == 2 and concept == 2 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong68.png"), (257, 82)) # case 68
        elif (hair == 3 and body == 1 and character == 1 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 69
        elif (hair == 3 and body == 1 and character == 2 and concept == 2 and deco == 3):  
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 70
        elif (hair == 3 and body == 2 and character == 1 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 71
        elif (hair == 3 and body == 2 and character == 2 and concept == 2 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong64.png"), (257, 82)) # case 72
        elif (hair == 1 and body == 1 and character == 1 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong73.png"), (257, 82)) # case 73
        elif (hair == 1 and body == 1 and character == 2 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 74
        elif (hair == 1 and body == 2 and character == 1 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 75
        elif (hair == 1 and body == 2 and character == 2 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 76
        elif (hair == 1 and body == 1 and character == 1 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 77
        elif (hair == 1 and body == 1 and character == 2 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 78
        elif (hair == 1 and body == 2 and character == 1 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong79.png"), (257, 82)) # case 79
        elif (hair == 1 and body == 2 and character == 2 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 80
        elif (hair == 1 and body == 1 and character == 1 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong0.png"), (257, 82)) # case 81
        elif (hair == 1 and body == 1 and character == 2 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 82
        elif (hair == 1 and body == 2 and character == 1 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong79.png"), (257, 82)) # case 83
        elif (hair == 1 and body == 2 and character == 2 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 84
        elif (hair == 2 and body == 1 and character == 1 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong85.png"), (257, 82)) # case 85
        elif (hair == 2 and body == 1 and character == 2 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 86
        elif (hair == 2 and body == 2 and character == 1 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 87
        elif (hair == 2 and body == 2 and character == 2 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 88
        elif (hair == 2 and body == 1 and character == 1 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong85.png"), (257, 82)) # case 89
        elif (hair == 2 and body == 1 and character == 2 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 90
        elif (hair == 2 and body == 2 and character == 1 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 91
        elif (hair == 2 and body == 2 and character == 2 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 92
        elif (hair == 2 and body == 1 and character == 1 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong93.png"), (257, 82)) # case 93
        elif (hair == 2 and body == 1 and character == 2 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 94
        elif (hair == 2 and body == 2 and character == 1 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong1.png"), (257, 82)) # case 95
        elif (hair == 2 and body == 2 and character == 2 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 96
        elif (hair == 3 and body == 1 and character == 1 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong97.png"), (257, 82)) # case 97
        elif (hair == 3 and body == 1 and character == 2 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 98
        elif (hair == 3 and body == 2 and character == 1 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong73.png"), (257, 82)) # case 99
        elif (hair == 3 and body == 2 and character == 2 and concept == 3 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong100.png"), (257, 82)) # case 100
        elif (hair == 3 and body == 1 and character == 1 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong97.png"), (257, 82)) # case 101
        elif (hair == 3 and body == 1 and character == 2 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 102
        elif (hair == 3 and body == 2 and character == 1 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 103
        elif (hair == 3 and body == 2 and character == 2 and concept == 3 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 104
        elif (hair == 3 and body == 1 and character == 1 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong9.png"), (257, 82)) # case 105
        elif (hair == 3 and body == 1 and character == 2 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 106
        elif (hair == 3 and body == 2 and character == 1 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong0.png"), (257, 82)) # case 107
        elif (hair == 3 and body == 2 and character == 2 and concept == 3 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong100.png"), (257, 82)) # case 108
        elif (hair == 1 and body == 1 and character == 1 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong109.png"), (257, 82)) # case 109
        elif (hair == 1 and body == 1 and character == 2 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong110.png"), (257, 82)) # case 110
        elif (hair == 1 and body == 2 and character == 1 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 111
        elif (hair == 1 and body == 2 and character == 2 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong112.png"), (257, 82)) # case 112
        elif (hair == 1 and body == 1 and character == 1 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong20.png"), (257, 82)) # case 113
        elif (hair == 1 and body == 1 and character == 2 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong114.png"), (257, 82)) # case 114
        elif (hair == 1 and body == 2 and character == 1 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong115.png"), (257, 82)) # case 115
        elif (hair == 1 and body == 2 and character == 2 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong56.png"), (257, 82)) # case 116
        elif (hair == 1 and body == 1 and character == 1 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong117.png"), (257, 82)) # case 117
        elif (hair == 1 and body == 1 and character == 2 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 118
        elif (hair == 1 and body == 2 and character == 1 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 119
        elif (hair == 1 and body == 2 and character == 2 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong112.png"), (257, 82)) # case 120
        elif (hair == 2 and body == 1 and character == 1 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 121
        elif (hair == 2 and body == 1 and character == 2 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong110.png"), (257, 82)) # case 122
        elif (hair == 2 and body == 2 and character == 1 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 123
        elif (hair == 2 and body == 2 and character == 2 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong10.png"), (257, 82)) # case 124
        elif (hair == 2 and body == 1 and character == 1 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 125
        elif (hair == 2 and body == 1 and character == 2 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 126
        elif (hair == 2 and body == 2 and character == 1 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong115.png"), (257, 82)) # case 127
        elif (hair == 2 and body == 2 and character == 2 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong128.png"), (257, 82)) # case 128
        elif (hair == 2 and body == 1 and character == 1 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong93.png"), (257, 82)) # case 129
        elif (hair == 2 and body == 1 and character == 2 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 130
        elif (hair == 2 and body == 2 and character == 1 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong131.png"), (257, 82)) # case 131
        elif (hair == 2 and body == 2 and character == 2 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong128.png"), (257, 82)) # case 132
        elif (hair == 3 and body == 1 and character == 1 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong109.png"), (257, 82)) # case 133
        elif (hair == 3 and body == 1 and character == 2 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong68.png"), (257, 82)) # case 134
        elif (hair == 3 and body == 2 and character == 1 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/noonsong131.png"), (257, 82)) # case 135
        elif (hair == 3 and body == 2 and character == 2 and concept == 4 and deco == 1):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 136
        elif (hair == 3 and body == 1 and character == 1 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong137.png"), (257, 82)) # case 137
        elif (hair == 3 and body == 1 and character == 2 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong114.png"), (257, 82)) # case 138
        elif (hair == 3 and body == 2 and character == 1 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong117.png"), (257, 82)) # case 139
        elif (hair == 3 and body == 2 and character == 2 and concept == 4 and deco == 2):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 140
        elif (hair == 3 and body == 1 and character == 1 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong137.png"), (257, 82)) # case 141
        elif (hair == 3 and body == 1 and character == 2 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/boom.png"), (257, 82)) # case 142
        elif (hair == 3 and body == 2 and character == 1 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong49.png"), (257, 82)) # case 143
        elif (hair == 3 and body == 2 and character == 2 and concept == 4 and deco == 3):
            gamepad.blit(pygame.image.load("images/noonsong3.png"), (257, 82)) # case 144
            

        restartButton = Button(restartImg, 180, 300, 221, 88, clickRestartImg, 170, 295, selectScreen)
        quitButton = Button(quitImg, 435, 300, 160, 88, clickQuitImg, 425, 295, quitgame)
        
        
        pygame.display.update()
        clock.tick(60)

def quitgame():
    pygame.quit()
    sys.exit()

initGame()

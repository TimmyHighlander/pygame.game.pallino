import random
import pygame
pygame.init()

listapari = [0, 2, 4, 6, 8]
listadispari = [1, 3, 5, 7, 9]

sfondo1 = pygame.image.load('backg.png')
screen = pygame.display.set_mode((700, 400))
running = True
pygame.mixer.music.load('251461__joshuaempyre__arcade-music-loop.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

point = pygame.mixer.Sound('point.wav')
game = pygame.mixer.Sound('game over.wav')
jump = pygame.mixer.Sound('jump.wav')

pygame.display.set_caption("Pallinuz")
icon = pygame.image.load('pallinonormal.png')
pygame.display.set_icon(icon)

monsterImg = pygame.image.load('monster1.png')
monsterY = 220
monsterX = 600
monsterX_change = 0
DEFAULT_IMAGE_SIZE = (64, 64)
monsterImg = pygame.transform.scale(monsterImg, DEFAULT_IMAGE_SIZE)
def monster(x, y):
    screen.blit(monsterImg, (x, y))

gameoverImg = pygame.image.load("gameover.png")
gameoverY = -1000
gameoverX = 50
def gameover(x, y):
    screen.blit(gameoverImg, (x, y))

spadaImg = pygame.image.load("spadagialla.png")
spadaY = 400
spadaX = 300
spadaY_change = 0
def spada(x, y):
    screen.blit(spadaImg, (x, y))

punteggio = 0
p = str(punteggio)
livello = 1
totpuntinecessari = 10
t = str(totpuntinecessari)
l = str(livello)
scorefont = pygame.font.Font('freesansbold.ttf', 16)
scoreX = 500
scoreY = 10
def score(x, y):
    score = scorefont.render("Lvl." + l + " Score: " + p + "/" + t, True, (0,0,0))
    screen.blit(score, (x, y))




font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = -1000
def text(x, y):
    text = font.render('press "R" to restart, score: ' + p, True, (0,0,0))
    screen.blit(text, (x,y))



playerImg = pygame.image.load('pallinonormal.png')
playerX = 200
playerY = 220
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open("dead", "w").write("")
            open("velocity", "w").write("")
            monsterX = 700
            playerX = 200
            playerY = 220
            playerY_change = 0
            playerX_change = 0
            monsterY = 220
            gameoverY = -1000
            textY = -1000
            p = "0"
            l = "1"
            t = "10"
            punteggio = 0
            open("spadatocco", "w").write("")

            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1

            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if event.key == pygame.K_SPACE:
                if open("spadatocco", "r").read() == "0":
                    open("spadatocco", "w").write("02")
                    open("tempospada", "w").write(str(monsterX))
                    print(int(open("tempospada", "r").read()))


            if event.key == pygame.K_UP and playerY==220:
                pygame.mixer.Sound.play(jump)
                open("velocity", "w").write("up")

            if event.key == pygame.K_w:
                running = False

            if event.key == pygame.K_r:
                open("dead", "w").write("")
                open("velocity", "w").write("")
                monsterX = 700
                playerX = 200
                playerY = 220
                playerY_change = 0
                playerX_change = 0
                monsterY = 220
                gameoverY = -1000
                textY = -1000
                p = "0"
                l = "1"
                t = "10"
                punteggio = 0
                open("spadatocco", "w").write("")



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                    playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                if open("spadatocco", "r").read() == "02":
                    open("spadatocco", "w").write("0")


    screen.fill((255, 203, 255))
    monsterX_change = -1
    if open("dead", "r").read()=="":
        if monsterX == -50:
            monsterX = 700
        if playerX<11:
            playerX = 11
        if playerX>650:
            playerX = 650
        if open("velocity", "r").read() == "up":
            if 121<playerY:
                playerY_change=(120-playerY)/22
            if int(playerY)==135:
                open("velocity", "w").write("down")
        if open("velocity", "r").read() == "down":
            if int(playerY)<220:
                playerY_change = -(120 - playerY) / 22
            else:
                open("velocity", "w").write("")
                playerY_change = 0
                playerY = 220
        if playerY == 220:
            if open("spadatocco", "r").read() == "":
                if int(str(playerX)[-2]) in listapari:
                    playerImg = pygame.image.load('pallino2.png')
                if int(str(playerX)[-2]) in listadispari:
                    playerImg = pygame.image.load('pallinonormal.png')
            if open("spadatocco", "r").read() == "0":
                if int(str(playerX)[-2]) in listapari:
                    playerImg = pygame.image.load('pallinospada1.png')
                if int(str(playerX)[-2]) in listadispari:
                    playerImg = pygame.image.load('pallinospada2.png')
            if open("spadatocco", "r").read() == "02":
                if int(str(playerX)[-2]) in listapari:
                    playerImg = pygame.image.load('pallinocolpo1.png')
                if int(str(playerX)[-2]) in listadispari:
                    playerImg = pygame.image.load('pallinocolpo2.png')

        if monsterX<10:
            monsterImg = pygame.image.load('monster2.png')
        if monsterX>=10:
            if int(str(monsterX)[-2]) in listapari:
                monsterImg = pygame.image.load('monster2.png')
            if int(str(monsterX)[-2]) in listadispari:
                monsterImg = pygame.image.load('monster1.png')

        if playerY-monsterY>-40:
            if open("spadatocco", "r").read()!="02":
                if abs(playerX-monsterX)<35:
                    open("dead", "w").write("yes")
    if open("dead", "r").read()=="yes":
        pygame.mixer.Sound.play(game)
        playerImg = pygame.image.load('pallinocry.png')
        monsterX_change=0
        playerX_change=0
        playerY_change=1
        if playerY>270:
            gameoverY = 50
            gameoverX = 50
            textY = 20

    if monsterX == 0:
        pygame.mixer.Sound.play(point)
        print("p")
        p = str(int(p)+1)

    if p == "1" and open("spadatocco", "r").read()=="":
        monsterX = 3000
        monsterX_change = 0
        l = "2"
        t = "∞"
        p = "0"
    if l == "2" and open("spadatocco", "r").read() == "":
        spadaY = -100
        spadaY_change += 1
        monsterX = 1000
        monsterY = 220


    if open("spadatocco", "r").read() != "":
        monsterX_change = -2
        if abs(monsterX-playerX)<35 and open("spadatocco", "r").read()=="02":
            p = str(int(p)+1)
            monsterX = 1000

    #if open("spadatocco", "r").read()!="":

    #if open("spadatocco", "r").read() == "0":
        #spadaY = 300














    screen.blit(sfondo1,(0,0))
    #playerY += playerY_change
    playerX += playerX_change
    playerY += playerY_change
    spadaY += spadaY_change
    if spadaY == 350:
        spadaY_change = 0
    if abs(playerX-300)<50 and abs(playerY-spadaY)<50:
        open("spadatocco", "w").write("0")
    monster(monsterX, monsterY)
    player(playerX, playerY)
    spada(spadaX, spadaY)
    gameover(gameoverX, gameoverY)
    text(textX, textY)
    score(scoreX, scoreY)
    monsterX += monsterX_change
    pygame.display.update()
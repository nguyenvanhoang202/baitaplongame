import math
import random
import sys
import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()
WHITE = (255, 255, 255)
BACK = (0, 0, 0)
RED = (205, 85, 85)
# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("image/background.png")

# Pause Background
pause_background = pygame.image.load("image/pause.png")
pause_background = pygame.transform.scale(pause_background, (800, 600))

# Gameover Backgound
gameover_background = pygame.image.load("image/gameover.png")

# Main Menu Backgound
mainmenu_background = pygame.image.load("image/mainmenu.png")
# Sound
mixer.music.load("audio/background.wav")
mixer.music.set_volume(0.5)
overSound = mixer.Sound("audio/gameover.wav")

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("image/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("image/player.png")
playerX = 370
playerY = 500
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Score
score_value = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("image/enemy.png"))
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(10, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


def add_enemy():
    global score_value, num_of_enemies, enemyImg, enemyX, enemyY, enemyX_change, enemyY_change
    if score_value % 10 == 0:
        num_of_enemies += 1
        enemyImg.append(pygame.image.load("image/enemy.png"))
        enemyX.append(random.randint(0, 730))
        enemyY.append(random.randint(10, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


# boss
bossImg = pygame.image.load("image/boss.png")
bossX = random.randint(0, 730)
bossY = random.randint(10, 150)
bossX_change = 4
bossY_change = 40
boss_state = "ready"  # Set boss_state to "ready" initially
boss_life = 2


def boss(x, y):
    screen.blit(bossImg, (x, y))


def boss_collision(bossX, bossY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bossX - bulletX, 2) + (math.pow(bossY - bulletY, 2)))
    if distance < 35:
        return True
    else:
        return False


# Big Boss
big_bossImg = pygame.image.load("image/big_boss.png")
big_bossX = random.randint(0, 730)
big_bossY = random.randint(10, 150)
big_bossX_change = 4
big_bossY_change = 40
big_boss_state = "ready"  # Set big_boss_state to "ready" initially
big_boss_life = 20


def big_boss(x, y):
    screen.blit(big_bossImg, (x, y))


def big_boss_collision(big_bossX, big_bossY, bulletX, bulletY):
    distance = math.sqrt(
        math.pow(big_bossX - bulletX, 2) + (math.pow(big_bossY - bulletY, 2))
    )
    if distance < 45:
        return True
    else:
        return False


# Boom
boomImg = pygame.image.load("image/boom.png")  # Load an image for the boom
boomX = random.randint(0, 730)
boomY = random.randint(10, 150)
boomX_change = 4
boomY_change = 40
boom_state = "ready"  # Set boom_state to "ready" initially
boom_life = 3  # Set boom_life to 3


def boom(x, y):
    screen.blit(boomImg, (x, y))


def bocollision(boomX, boomY, bulletX, bulletY):
    distance = math.sqrt(math.pow(boomX - bulletX, 2) + (math.pow(boomY - bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False


# Bullet
# Speed
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load("image/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def speed_bullet():
    global score_value, bulletY_change
    if score_value % 50 == 0:
        bulletY_change += 1


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# font
font = pygame.font.Font("Pixeboy-z8XGD.ttf", 50)
fontp = pygame.font.Font("Pixeboy-z8XGD.ttf", 35)
over_font = pygame.font.Font("Pixeboy-z8XGD.ttf", 90)

# HighScore
highscore = 0

# Score in game
textX = 10
textY = 10


def show_score(x, y):
    pause = fontp.render("Pause : P", True, (WHITE))
    bdpause = fontp.render("Pause : P", True, (BACK))
    screen.blit(bdpause, (x + 3, 47))
    screen.blit(pause, (x, 45))
    score = font.render("Score : " + str(score_value), True, (WHITE))
    bdscore = font.render("Score : " + str(score_value), True, (BACK))
    screen.blit(bdscore, (x + 3, y + 3))
    screen.blit(score, (x, y))
    score = font.render("High Score : " + str(highscore), True, (WHITE))
    bdscore = font.render("High Score : " + str(highscore), True, (BACK))
    screen.blit(bdscore, (403, y + 3))
    screen.blit(score, (400, y))


def new_game():
    global running, score_value, playerX_change, num_of_enemies
    global bossX, bossY, boomX, boomY, boom_state, boom_life, big_bossX, big_bossY, big_boss_life
    global boss_state, big_boss_state

    score_value = 0
    playerX_change = 0
    mixer.music.load("audio/background.wav")
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    num_of_enemies = 7
    # Reset enemy positions
    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, 730)
        enemyY[i] = random.randint(10, 150)
    bossX = random.randint(0, 730)
    bossY = random.randint(10, 150)
    boomX = random.randint(0, 730)
    boomY = random.randint(10, 150)
    big_bossX = random.randint(0, 730)
    big_bossY = random.randint(10, 150)
    # Reset bullet state
    bullet_state = "ready"
    boom_state = "ready"
    boss_state = "ready"
    big_boss_state = "ready"
    boom_life = 3
    big_boss_life = 20

    running = True


def game_start():
    playSound = mixer.Sound("audio/intro.wav")
    playSound.play(-1)
    global running, mainmenu_background
    start = True
    while start:
        # Blit the main menu background image
        screen.blit(mainmenu_background, (0, 0))
        namegame = over_font.render("Space Invaders", True, (WHITE))
        bdnamegame = over_font.render("Space Invaders", True, (BACK))
        screen.blit(bdnamegame, (123, 173))
        screen.blit(namegame, (120, 170))
        resume = font.render("Start: S", True, (WHITE))
        bdresume = font.render("Start: S", True, (BACK))
        screen.blit(bdresume, (323, 253))
        screen.blit(resume, (320, 250))
        exitgame = font.render("Exit Game: ESC", True, (WHITE))
        bdexitgame = font.render("Exit Game: ESC", True, (BACK))
        screen.blit(bdexitgame, (263, 313))
        screen.blit(exitgame, (260, 310))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                running = False
                start = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    playSound.stop()
                    start = False

        pygame.display.update()
    if start == False:
        pygame.mixer.music.play(-1)


def game_pause():
    global running, pause_background
    paused = True
    while paused:
        # Blit the pause background image
        screen.blit(pause_background, (0, 0))
        resume = font.render("Resume: P", True, (WHITE))
        bdresume = font.render("Resume: P", True, (BACK))
        screen.blit(bdresume, (313, 203))
        screen.blit(resume, (310, 200))
        newgame = font.render("New Game: X", True, (WHITE))
        bdnewgame = font.render("New Game: X", True, (BACK))
        screen.blit(bdnewgame, (303, 303))
        screen.blit(newgame, (300, 300))
        exitgame = font.render("Exit Game: ESC", True, (WHITE))
        bdexitgame = font.render("Exit Game: ESC", True, (BACK))
        screen.blit(bdexitgame, (263, 403))
        screen.blit(exitgame, (260, 400))
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    paused = False
                    new_game()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                running = False
                paused = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        pygame.display.update()
    if paused == False:
        pygame.mixer.music.play(-1)


def game_over():
    overexplosion = mixer.Sound("audio/explosion.wav")
    overexplosion.play()
    overSound = mixer.Sound("audio/gameover.wav")
    pygame.time.delay(1500)
    overSound.play()
    global running, gameover_background
    over = True
    while over:
        screen.blit(gameover_background, (0, 0))
        over_text = over_font.render("GAME OVER", True, (WHITE))
        bdover_text = over_font.render("GAME OVER", True, (BACK))
        screen.blit(bdover_text, (243, 143))
        screen.blit(over_text, (240, 140))
        over_text = font.render("Press the 'X' key to start again", True, (WHITE))
        bdover_text = font.render("Press the 'X' key to start again", True, (BACK))
        screen.blit(bdover_text, (103, 323))
        screen.blit(over_text, (100, 320))
        over_text = font.render("High Score: " + str(highscore), True, (RED))
        bdovertext = font.render("High Score: " + str(highscore), True, (WHITE))
        bdover_text = font.render("High Score: " + str(highscore), True, (BACK))
        screen.blit(bdover_text, (283, 243))
        screen.blit(bdovertext, (281, 241))
        screen.blit(over_text, (280, 240))
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    over = False
                    new_game()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                running = False
                over = False

        pygame.display.update()
    if over == False:
        pygame.mixer.music.play(-1)


# Game Loop
running = True
if running == True:
    game_start()
    pygame.display.update()
while running:
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("audio/laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_p:
                game_pause()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Limit player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement

    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 465 and enemyY[i] < 1000:
            for j in range(num_of_enemies):
                enemyY[j] = 3000
            game_over()
        # move
        enemyX[i] += enemyX_change[i]
        # way of moving
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 730:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collision enemy
        ecollision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if ecollision:
            explosionSound = mixer.Sound("audio/beep.wav")
            explosionSound.play()
            bulletY = 500
            bullet_state = "ready"
            score_value += 1
            if score_value > highscore:
                highscore = score_value
            enemyX[i] = random.randint(0, 730)
            enemyY[i] = random.randint(50, 150)
            add_enemy()
            speed_bullet()

        enemy(enemyX[i], enemyY[i], i)
    # boss
    if score_value > 0:
        if score_value % 5 == 0 and boss_state == "ready":
            boss_state = "appear"
            boss_life = 3  # Reset boss_life each time a new boss appears
            bossY = 0
        if bossY > 465 and bossY < 1000:
            game_over()
        if boss_state == "appear":
            boss(bossX, bossY)
            bossX += bossX_change
            if bossX <= 0:
                bossX_change = 2
                bossY += bossY_change
            elif bossX >= 730:
                bossX_change = -2
                bossY += bossY_change

            # Check for collision with boss
            boss_collision = isCollision(bossX, bossY, bulletX, bulletY)
            if boss_collision:
                explosionSound = mixer.Sound("audio/beep.wav")
                explosionSound.play()
                bulletY = 500
                bullet_state = "ready"
                boss_life -= 1
                if boss_life == 0:
                    score_value += 5
                    boss_state = "ready"
                    if score_value > highscore:
                        highscore = score_value
    # boom
    if score_value > 0:
        if score_value % 10 == 0 and boom_state == "ready":
            boom_state = "appear"
            boom_life = 3  # Reset boom_life each time a new boom appears
            boomY = 0
    if boomY > 465:
        boomY = 2000
        boom_state = (
            "ready"  # Boom disappears when it crosses the limit, no points added
        )
    if boom_state == "appear":
        boom(boomX, boomY)
        boomX += boomX_change
        if boomX <= 0:
            boomX_change = 2
            boomY += boomY_change
        elif boomX >= 730:
            boomX_change = -2
            boomY += boomY_change

        # Check for collision with boom
        boom_collision = bocollision(boomX, boomY, bulletX, bulletY)
        if boom_collision:
            boomSound = mixer.Sound("audio/boop.wav")
            boomSound.set_volume(1.0)
            boomSound.play()
            bulletY = 500
            bullet_state = "ready"
            boom_life -= 1
            if boom_life == 0:
                game_over()  # Game over when boom is hit 3 times
    # bigboss
    if score_value > 0:
        if score_value % 50 == 0 and big_boss_state == "ready":
            big_boss_state = "appear"
            big_boss_life = 20  # Reset big_boss_life each time a new big boss appears
            big_bossY = 0
            # Make all enemies and small boss disappear
            for i in range(num_of_enemies):
                enemyY[i] = 2000
            bossY = 2000
        if big_bossY > 465 and big_bossY < 1000:
            score_value = 0
            game_over()
        if big_boss_state == "appear":
            big_boss(big_bossX, big_bossY)
            big_bossX += big_bossX_change
            if big_bossX <= 0:
                big_bossX_change = 2
                big_bossY += big_bossY_change
            elif big_bossX >= 730:
                big_bossX_change = -2
                big_bossY += big_bossY_change

            # Check for collision with big boss
            bigbosscollision = big_boss_collision(
                big_bossX, big_bossY, bulletX, bulletY
            )
            if bigbosscollision:
                explosionSound = mixer.Sound("audio/beep.wav")
                explosionSound.play()
                bulletY = 500
                bullet_state = "ready"
                big_boss_life -= 1
                if big_boss_life == 0:
                    score_value += 15
                    big_boss_state = "ready"
                    if score_value > highscore:
                        highscore = score_value
                    # Make all enemies and small boss appear again
                    for i in range(num_of_enemies):
                        enemyY[i] = random.randint(10, 150)
                    bossY = random.randint(10, 150)
            hpbigboss = font.render("Hp: " + str(big_boss_life), True, (RED))
            bdhpbigboss = font.render("Hp: " + str(big_boss_life), True, (BACK))
            screen.blit(bdhpbigboss, (353, 558))
            screen.blit(hpbigboss, (350, 555))
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    def save_highscore():
        with open("highscore.txt", "w") as file:
            file.write(str(highscore))

    pygame.draw.line(screen, WHITE, (0, 500), (800, 500), 1)
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

import pygame
import random
import math

screen = pygame.display.set_mode((800, 600))
# bg
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (800, 600))
# headings and images
pygame.display.set_caption("Tiny invader")
icon = pygame.image.load('enemy.png')
pygame.display.set_icon(icon)

# hero positioning
playerImg = pygame.image.load('ufo.png')
playerX = 370
playerY = 480
playerXchange = 0

# enemy
enemyImg = pygame.image.load('enemy.png')
enemyImg = pygame.transform.rotate(enemyImg, 180)
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyXchange = 1
enemyYchange = 20

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 5
bullet_state = "ready"
score=0
# score_value = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
# textX = 10
# textY = 10


def show_score(x, y):
    score = font.render("Score= " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Movement
def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))


def enemy(enemyX, enemyY):
    screen.blit(enemyImg, (enemyX, enemyY))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# collision
def collide(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerXchange += 2.3
            if event.key == pygame.K_LEFT:
                playerXchange -= 2.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    playerX += playerXchange
    enemyX += enemyXchange
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if enemyX <= 0:
        enemyY += enemyYchange
        enemyXchange = 1
    elif enemyX >= 736:
        enemyY += enemyYchange
        enemyXchange = -1

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange
    # collision
    collision = collide(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 400
        bullet_state = "ready"
        # score_value += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
        print(score)
    # show_score(textX, textY)
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

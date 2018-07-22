from pygame.locals import *
from sys import exit

import pygame
import random

WHITE = (255, 255, 255)
BlACK = (0, 0, 0)
RED = (255, 0, 0, 255)
MOVE_UP_SPEED = 0.4
MOVE_DOWN_SPEED = 0.2
OBSTACLESPEED = 0.16

pygame.init()
screen = pygame.display.set_mode((400, 560), 0, 32)
pygame.display.set_caption('Flappy Bird')
bird = pygame.image.load('bird.png')
integral = pygame.font.SysFont('arial', 32)

bird_x, bird_y = 180, 220
obstacle_high = random.randint(200, 400)
obstacle_wide = random.randint(40, 80)
obstacle_x = 500
obstacle_y = 0
count = 0
moveup = False
start = False
start_count = True

def restart():
    global bird_y
    global obstacle_x
    global obstacle_high
    global obstacle_wide
    global start
    global count
    global start_count

    bird_y = 220
    obstacle_x = 500
    count = 0
    obstacle_high = random.randint(200, 400)
    obstacle_wide = 50
    start = False
    start_count = True

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                moveup = True
                start = True

        elif event.type == KEYUP:
            if event.key == K_SPACE:
                moveup = False

    if start:
        bird_y += MOVE_DOWN_SPEED

        if moveup and bird_y > 0:
            bird_y -= MOVE_UP_SPEED

        if obstacle_x > 0:
            obstacle_x -= OBSTACLESPEED
            if bird_x > obstacle_x + obstacle_wide and start_count:
                count += 1
                start_count = False
        else:
            start_count = True
            obstacle_x = 500
            obstacle_high = random.randint(200, 400)
            obstacle_wide = random.randint(40, 60)
    try:
        if screen.get_at((int(bird_x + 17), int(bird_y + 5))) == (255, 0, 0, 255) or screen.get_at((int(bird_x + 17), int(bird_y + 25))) == (255, 0, 0, 255):
            restart()
    except IndexError:
        restart()

    screen.fill(WHITE)
    screen.blit(bird, (bird_x, bird_y))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_wide, obstacle_high), 5)
    pygame.draw.rect(screen, RED, (obstacle_x, 90 + obstacle_high, obstacle_wide, 90 + obstacle_high), 5)
    screen.blit(integral.render(str(count), True, BlACK, WHITE), (20, 20))

    pygame.display.update()

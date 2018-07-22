import pygame
from pygame.locals import *
from sys import exit
from random import randint
from PIL import Image

flag = True
im1 = Image.open('image1')
im2 = Image.open('image2')
wide = im1.size[0] if im1.size[0] > im2.size[0] else im2.size[0]
high = im1.size[1] if im1.size[1] > im2.size[1] else im2.size[1]
im1 = im1.resize((wide, high))
im2 = im2.resize((wide, high))

pygame.init()
screen = pygame.display.set_mode((wide, high), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 20, 20)

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                screen.fill((0, 0, 0))

            if event.key == K_s:
                pygame.image.save(screen, 'img.png')

    for _ in range(10000):
         rand_pos = (randint(0, wide - 1), randint(0, high - 1))
         screen.set_at(rand_pos, im1.getpixel(rand_pos))

    for _ in range(10000):
         rand_pos = (randint(0, wide - 1), randint(0, high - 1))
         screen.set_at(rand_pos, im2.getpixel(rand_pos))

    pygame.display.update()
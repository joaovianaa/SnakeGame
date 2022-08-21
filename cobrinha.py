from pickle import TRUE
from tkinter import EventType
import pygame
from pygame.locals import *
import random 


windowSize = (600, 600)
pixelSize = 10

def collision(pos1, pos2):
    return pos1 == pos2

def offlimits(pos):
    if 0 <= pos[0] < windowSize[0] and 0 <= pos[1] < windowSize[1]:
        return False
    else:
        return True        
        
def randomOnGrid():
    x = random.randint(0, windowSize[0])
    y = random.randint(0, windowSize[1])
    return x // pixelSize * pixelSize, y // pixelSize * pixelSize


pygame.init()
screen = pygame.display.set_mode((windowSize))
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((pixelSize, pixelSize))
snake_surface.fill((57, 255, 20))
snake_direction = K_LEFT


apple_surface = pygame.Surface((pixelSize, pixelSize))
apple_surface.fill((255, 0, 0))
apple_pos = randomOnGrid()

def restartGame():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = randomOnGrid ()

while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key
    
    screen.blit(apple_surface, apple_pos)

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, 0))
        apple_pos = randomOnGrid()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    for i in range (len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restartGame()
        snake_pos[i] = snake_pos[i-1]

    if offlimits(snake_pos[0]):
        restartGame()


    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - pixelSize)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + pixelSize)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - pixelSize, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        
        snake_pos[0] = (snake_pos[0][0] + pixelSize, snake_pos[0][1])

    pygame.display.update()

# IMPORTS E INITS 
import pygame
import random
from config import WIDTH, HEIGHT, FPS, INICIO, GAME, GAMEOVER, QUIT

pygame.init()

tela = pygame.display.set_mode((WIDTH,HEIGHT))

state= INICIO
while state != QUIT:
    if state == INICIO:
        #Rodar a tela inicial------
        
    
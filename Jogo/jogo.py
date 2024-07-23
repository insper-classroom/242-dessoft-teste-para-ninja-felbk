# IMPORTS E INITS 
import pygame
import random
from config import WIDTH, HEIGHT, FPS, INICIO, GAME, GAMEOVER, QUIT
from inicio import tela_incio
from fase import tela_fase

#Inicialização do pygame
pygame.init()

tela = pygame.display.set_mode((WIDTH,HEIGHT))
state= INICIO

while state != QUIT:
    if state == INICIO:
        #Rodar a tela inicial------
        state = tela_incio(tela)
    elif state == GAME:
        state = tela_fase(tela)
    
print("saindo")
pygame.quit()
    
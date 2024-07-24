# IMPORTS E INITS 
import pygame
import random
from config import WIDTH, HEIGHT, FPS, INICIO, GAME, GAMEOVER, QUIT
from inicio import tela_incio
from fase import tela_fase
from gameover import tela_gameover


#Inicialização do pygame
pygame.init()

tela = pygame.display.set_mode((WIDTH,HEIGHT))
state= INICIO

while state != QUIT:
    if state == INICIO:
        #Rodar a tela inicial------
        state = tela_incio(tela)
    elif state == GAME:
        state_Pontos = tela_fase(tela)
        state = state_Pontos[0]
        Pontos = state_Pontos[1]
    else:
        state = tela_gameover(tela,Pontos)
    

pygame.quit()
    
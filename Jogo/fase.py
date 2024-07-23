import pygame
from config import GAME, QUIT , INICIO, WIDTH,HEIGHT, GAMEOVER, FPS

def tela_fase(tela):
    clock= pygame.time.Clock()
    rodando = True

    while rodando:
        clock.tick(FPS)


        #Analisa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False

        

        #Preenche a tela
        tela.fill((255,255,255))
        
        #Atualiza tela
        pygame.display.flip()






    return state
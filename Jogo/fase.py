import pygame
from config import GAME, QUIT , INICIO, WIDTH,HEIGHT, GAMEOVER, FPS
from gerador import gera_numeros

def tela_fase(tela):
    clock= pygame.time.Clock()
    rodando = True


    while rodando:
        clock.tick(FPS)

        #Configura o Chão
        chãoHeight = 40 #Altura
        # Cria retangulo  pygame.Rect( Esquerda, Topo , Largura, Altura)
        chãoRect = pygame.Rect( 0,  HEIGHT-chãoHeight,  WIDTH ,  chãoHeight) 
        chãoCollor = (233,150,233) # Código RGB da cor

        #Cria grupo de blocos
        blocos = pygame.sprite.Group()

        

        #Analisa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False

        

        #Preenche a tela
        tela.fill((255,255,255))
        pygame.draw.rect(tela,chãoCollor, chãoRect) #Desenha chão
        
        #Atualiza tela
        pygame.display.flip()






    return state
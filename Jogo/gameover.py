import pygame
from config import GAME, FPS, QUIT, WIDTH, HEIGHT,GAME

def tela_gameover(tela):
    clock = pygame.time.Clock()
    rodando = True

    fonte = pygame.font.SysFont(None,40)
    textoPlay = fonte.render("Jogar novamente",True,(255,255,255))

    playwidth = textoPlay.get_width()
    playheight = textoPlay.get_height()

    buttonwidth = playwidth + 100
    buttonheight = playheight + 50
    
    rectbutton = pygame.Rect((WIDTH/2 - buttonwidth/2 , HEIGHT/2 - buttonheight/2, buttonwidth, buttonheight))

    
    while rodando:
        clock.tick(FPS)

        #Analisa eventos
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False
            #Detecta click no botão
            if pygame.Rect.collidepoint(rectbutton,mousePos):
                if pygame.mouse.get_pressed()[0]:
                    state = GAME
                    rodando = False
            

        #Preenche a tela
        tela.fill((255,255,255))
        pygame.draw.rect(tela,(255,0,0),rectbutton)
        tela.blit(textoPlay,(WIDTH/2 - playwidth/2, HEIGHT/2 - playheight/2))
        
        #Atualiza tela
        pygame.display.flip()

    return state
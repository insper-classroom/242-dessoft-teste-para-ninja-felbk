import pygame
from config import GAME, FPS, QUIT, WIDTH, HEIGHT

def tela_incio(tela):
    clock = pygame.time.Clock()
    rodando = True
    fonte = pygame.font.SysFont(None,40)
    textoPlay = fonte.render("Jogar ",True,(0,255,0))
    playwidth = textoPlay.get_width()
    playheight = textoPlay.get_height()
    buttonwidth = playwidth + 100
    buttonheight = playheight + 50
    rectbutton = pygame.Rect((WIDTH/2 - buttonwidth/2 , HEIGHT/2 - buttonheight/2, buttonwidth, buttonheight))

    
    while rodando:
        clock.tick(FPS)

        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False
            if pygame.Rect.collidepoint(rectbutton,mousePos) and pygame.mouse.get_pressed()[0]:
                state= GAME
                rodando = False
            


        tela.fill((255,0,255))
        pygame.draw.rect(tela,(0,0,0),rectbutton)
        tela.blit(textoPlay,(WIDTH/2 - playwidth/2, HEIGHT/2 - playheight/2))
        
        
        pygame.display.flip()

    return state
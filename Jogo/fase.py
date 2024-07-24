import pygame
from pygame.sprite import _Group
from config import GAME, QUIT , INICIO, WIDTH,HEIGHT, GAMEOVER, FPS
from gerador import gera_numeros

def tela_fase(tela):
    clock= pygame.time.Clock()
    rodando = True
    Timer = 60 # 60 segundos
    font = pygame.font.SysFont(None,35)

    #Classe do bloco
    class Bloco(pygame.sprite.Sprite):

        #Inicializa o objeto e configura seus atributos
        def __init__(self,valor,cor,pos,errado):
            pygame.sprite.Sprite.__init__(self) #Inicia a classe "superior" sprite.Sprite
            self.valor = valor
            self.cor = cor
            self.errado = errado
            #Adiciona o bloco criado ao grupo de blocos para facilitar o controle
            self.add(blocos)
            
            self.size = (120,120)
            self.pos = pos
            self.rect = (self.pos[0],self.pos[1],self.size[0],self.size[1])
            
            #Configura a mensagem a ser exibida ao clicar no bloco
            if errado:
                self.mensagem = "Errado!"
            else:
                self.mensagem = "Correto!"


        #Atualiza e analisa eventos com blocos 
        def update(self):
             
            if pygame.Rect.collidepoint(self.rect,pygame.mouse.get_pos()):

            


        
        


    while rodando:
        clock.tick(FPS)

        #subtrai tempo
        Timer -= 1/FPS

        #Texto do tempo 
        Tempo = font.render(f"Tempo restante: {str(int(Timer))}s",True,(0,0,0))
        TempoWidth = Tempo.get_width()
        

        #Configura o Chão
        chãoHeight = 40 #Altura
        # Cria retangulo  pygame.Rect( Esquerda, Topo , Largura, Altura)
        chãoRect = pygame.Rect( 0,  HEIGHT-chãoHeight,  WIDTH ,  chãoHeight) 
        chãoCollor = (233,150,233) # Código RGB da cor

        #Cria grupo de blocos
        blocos = pygame.sprite.Group()
            
        #Configura blocos
        CoresBlocos = [(255,0,0),(0,255,0),(0,0,255)]
        
        #Gera sequência de números e informa a posição errada
        if len(blocos.sprites()) < 1:
            Num_e_resposta = gera_numeros() #Retorna uma tupla ( [n1,n2,n3,soma] , N° da pos errada )
            num = Num_e_resposta[0] 
            PosErrada = Num_e_resposta[1]
        
        



        #Analisa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False

        #Analisa tempo
        if Timer <= 0 :
            rodando = False
            state = GAMEOVER

       


        

        #Preenche a tela
        tela.fill((255,255,255))
        pygame.draw.rect(tela,chãoCollor, chãoRect) #Desenha chão
        tela.blit(Tempo,(WIDTH - TempoWidth - 20, 0 ))
        
        #Atualiza tela
        pygame.display.flip()






    return state
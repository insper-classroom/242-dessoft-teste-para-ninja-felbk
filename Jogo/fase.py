import pygame
from config import GAME, QUIT , INICIO, WIDTH,HEIGHT, GAMEOVER, FPS
from gerador import gera_numeros

def tela_fase(tela):
    clock= pygame.time.Clock()
    rodando = True
    Timer = 60 # 60 segundos
    msgTimer = 0 # Tempo para poder clicar nos blocos e ficar exibindo a mensagem
    Pontos = 0
    vidas=3 #Inicia vidas
    font = pygame.font.SysFont(None,35)

    #Cria grupo de blocos
    blocos = pygame.sprite.Group()

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
            self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
            
            #Configura a mensagem a ser exibida ao clicar no bloco
            if not self.errado:
                self.mensagem = "Errado!" #Quando clicar em um numero q faz parte da soma, a pessoa erra
            else:
                self.mensagem = "Correto!" #Caso o numero não faça parte da soma a pessoa acerta 



        #Atualiza exibição de blocos 
        def update(self,tela):
             
            #Exibe o bloco e o valor
            pygame.draw.rect(tela,self.cor,self.rect)
            valor = font.render(str(self.valor),True,(0,0,0))
            valorWidth= valor.get_width()
            valorHeight= valor.get_height()
            tela.blit(valor,(self.pos[0]+ self.size[0]/2 - valorWidth/2 , self.pos[1] + self.size[1]/2 - valorHeight/2))
            return

    pygame.time.wait(200)
    while rodando:
        clock.tick(FPS)
        

        #Texto das vidas
        txtvidas = font.render(f"Vidas: {str(int(vidas))}",True,(0,0,0))
        txtvidasHeight = txtvidas.get_height() #Altura do texto

        #subtrai tempo
        Timer -= 1/FPS

        #Subtrai timer msg    
        msgTimer -= 1/FPS

        #Texto do tempo 
        Tempo = font.render(f"Tempo restante: {str(int(Timer))}s",True,(0,0,0))
        TempoWidth = Tempo.get_width()
        
        #Configura o Chão
        chãoHeight = 40 #Altura
        # Cria retangulo  pygame.Rect( Esquerda, Topo , Largura, Altura)
        chãoRect = pygame.Rect( 0,  HEIGHT-chãoHeight,  WIDTH ,  chãoHeight) 
        chãoCollor = (233,150,233) # Código RGB da cor

        #Configura blocos
        CoresBlocos = [(255,0,0),(0,255,0),(0,0,255)]
        
        #Gera sequência de números e coleta a posição errada sempre que houver menos de 3 blocos
        if len(blocos.sprites()) < 3 and msgTimer <=0:
            blocos.empty()
            mostramsg = False # Desativa mensagem
            Num_e_resposta = gera_numeros() #Retorna uma tupla ( [n1,n2,n3,soma] , N° da pos errada )
            num = Num_e_resposta[0] 
            PosErrada = Num_e_resposta[1]
            for i in range(3):
                if PosErrada == i:
                    errado = True
                else:
                    errado= False
                bloco = Bloco(num[i],CoresBlocos[i], (WIDTH/2 - 60 ,HEIGHT - chãoHeight - (120*(i+1))), errado )

        #Gera a imagem do valor da soma
        sm = font.render(str(num[3]),True,(0,0,0))

        #Analisa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False

        #Analisa tempo e vidas
        if Timer <= 0 or vidas <= 0 :
            rodando = False
            state = GAMEOVER
        
        #Analisa blocos caso msgTimer seja <= 0
        if msgTimer <= 0:

            for bloco in blocos.sprites():

                # Mouse encima de um bloco
                if pygame.Rect.collidepoint(bloco.rect,pygame.mouse.get_pos()):
                    #Clique esquerdo no bloco:
                    if pygame.mouse.get_pressed()[0]:
                        
                        #Exibe a mensagem correto ou errado:
                        
                        msg = font.render(bloco.mensagem,True,(0,0,0)) #Gera "imagem" com texto 
                        msgTimer= 1 
                        msgWidth = msg.get_width() #coleta largura 
                        msgHeight = msg.get_height() #coleta altura
                        mostramsg = True
                        msgPos = ( bloco.pos[0]+ bloco.size[0]/2 - msgWidth/2 , bloco.pos[1] + bloco.size[1]/2 - msgHeight/2 )
                        

                        #Adicona ponto se o bloco eliminado não fizer parte da soma 
                        if bloco.errado:
                            Pontos+=1
                        else:
                            #Tira vida caso o bloco faça parte da soma
                            vidas-=1

                        #Destroi o bloco
                        bloco.kill()

        #Preenche a tela
        tela.fill((255,255,255))
        pygame.draw.rect(tela,chãoCollor, chãoRect) #Desenha chão
        tela.blit(Tempo,(WIDTH - TempoWidth - 20, 0 )) #Exibe o tempo
        tela.blit(txtvidas,(5,HEIGHT - txtvidasHeight - 5)) # Exibe vidas
        tela.blit(sm,(5,5)) #Exibe a soma
        if mostramsg :
            tela.blit(msg, msgPos ) # Exibe a mensagem

        #desenha todos blocos
        blocos.update(tela)
        
        #Atualiza tela
        pygame.display.flip()

    return (state,Pontos)
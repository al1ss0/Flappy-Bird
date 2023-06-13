import pygame
import winsound
import random
pygame.init()
tamanho = (800,600)
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
direita = True
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('FlappyBird')
flappy = pygame.image.load("flappybird.png")
flappyoriginal = pygame.image.load("flappybird.png")
pygame.display.set_icon(flappy)
fundo = pygame.image.load("background.jpg")
running = True
posicaoxBolinha = 0
posicaoyBolinha = 300 
velocidade = 1
posicaoxBolinhaV = 400
posicaoyBolinhaV = 300
movimentobolinhaVX = 0
movimentobolinhaVY = 0
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Comandos
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:  #Faz o jogo fechar com o ESC
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT: #Faz a bolinha ir pra esquerda
            movimentobolinhaVX = -5
            flappy= flappyoriginal
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT: # Faz a bolinha ir pra direita
            movimentobolinhaVX = 5
            flappy = pygame.transform.flip(flappy, True,False)
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentobolinhaVX = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentobolinhaVY = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentobolinhaVY = -5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentobolinhaVY = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentobolinhaVY = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentobolinhaVY = 0
    tela.fill(branco)
    tela.blit(fundo,(0,0))
    if posicaoxBolinha >= 800:
        direita =  False
        velocidade = velocidade + 1
        posicaoyBolinha = random.randint(0,600)
    elif posicaoxBolinha <= 0:
        direita = True
        velocidade = velocidade + 1

    if direita:
        posicaoxBolinha = posicaoxBolinha + velocidade
    else:
        posicaoxBolinha = posicaoxBolinha - velocidade
    
    if posicaoxBolinhaV < 0:
        posicaoxBolinhaV = 0
    elif posicaoxBolinhaV > 700:
        posicaoxBolinhaV = 700
    else:
        posicaoxBolinhaV = posicaoxBolinhaV + movimentobolinhaVX

    if posicaoyBolinhaV < 0:
        posicaoyBolinhaV = 0
    elif posicaoyBolinhaV > 550:
        posicaoyBolinhaV = 550
    else:
        posicaoyBolinhaV = posicaoyBolinhaV + movimentobolinhaVY
    
    tela.blit(flappy,(posicaoxBolinhaV,posicaoyBolinhaV))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
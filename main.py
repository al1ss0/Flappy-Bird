import pygame
import winsound
import random
pygame.init()
tamanho = (800,600)
branco = (255,255,255)
vermelho = (255,0, 0)
preto = (0,0,0)
running = True
direita = True
velocidade = 1
posicaoXBolinha = 0
posicaoYBolinha = 300
posicaoXBolinhaV = 400
movimentoBolinhaVX = 0
movimentoBolinhaVY = 0
posicaoYBolinhaV = 300
clock = pygame.time.Clock()
tela =  pygame.display.set_mode( tamanho )
pygame.display.set_caption("FlappyBird")
flappy = pygame.image.load("flappybird.png")
flappyOriginal = pygame.image.load("flappybird.png")
pygame.display.set_icon(flappy)
fundo = pygame.image.load("background.jpg")
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoBolinhaVX = -5
            flappy = flappyOriginal
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoBolinhaVX = 5
            flappy = pygame.transform.flip(flappy, True,False)
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoBolinhaVX = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoBolinhaVX = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoBolinhaVY = -5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoBolinhaVY = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoBolinhaVY = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoBolinhaVY = 0


    tela.fill(branco)
    tela.blit(fundo, (0,0))
    pygame.draw.circle(tela,preto,(posicaoXBolinha,posicaoYBolinha),30)

    if posicaoXBolinha >= 800:
        direita = False
        velocidade = velocidade + 1
        posicaoYBolinha = random.randint(0,600)
        #winsound.Beep(500,300)
    elif posicaoXBolinha <= 0:
        direita = True
        velocidade = velocidade + 1
        #winsound.Beep(500,300)

    if direita :
        posicaoXBolinha = posicaoXBolinha + velocidade
    else:
        posicaoXBolinha = posicaoXBolinha - velocidade
    
    
    if posicaoXBolinhaV < 0:
        posicaoXBolinhaV = 0
    elif posicaoXBolinhaV > 700:
        posicaoXBolinhaV = 700
    else:
        posicaoXBolinhaV = posicaoXBolinhaV + movimentoBolinhaVX

    if posicaoYBolinhaV < 0:
        posicaoYBolinhaV = 0
    elif posicaoYBolinhaV > 550:
        posicaoYBolinhaV = 550
    else:
        posicaoYBolinhaV = posicaoYBolinhaV + movimentoBolinhaVY
    
    #pygame.draw.circle(tela, vermelho, (posicaoXBolinhaV,posicaoYBolinhaV) , 30 )
    tela.blit(flappy, (posicaoXBolinhaV,posicaoYBolinhaV))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
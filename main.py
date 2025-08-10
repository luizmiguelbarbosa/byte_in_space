#Código da janela do jogo.
#esse é o primeiro passo, vai ser na janela aonde o jogo será exibido

#vamos primeiro importar a biblioteca pygame
import pygame
#agora vou importar um submódulo que está dentro da biblioteca do pygame
from pygame.locals import * #esse submódulo ele contém todas as constantes e funções que a gente vai usar no nosso script. Esse asteristico no diz que dentro do meu submódulo locals, eu vou estar importando todas as funções e todas as constantes que o submódulo locals contém, e o submódulo locals, por sua vez, está dentro da biblioteca pygame
#agora vou importar uma função que está dentro do módulo sys
from sys import exit #Essa função que eu importei serve para fechar a janela 
from random import randint #para adicionar coisas aleatória heheh isso vai ser massa :)

#Agora que ja fizemos as importações, vamos começar o script de fato 
pygame.init() #inicializa o pygame
pygame.mixer.init() #inicializa o módulo de som

#tocar a música no menu do jogo 
pygame.mixer.music.load('musicas/musica_jogo.mp3') #subi a musica
pygame.mixer.music.play(-1) #-1 significa que a musica vai tocar em loop infinito
pygame.mixer.music.set_volume(0.4) #diminui um pouco o som do jogo (estava muito alto)

#carrega a música da fase 1
musica_fase1 = 'musicas/musica_start.mp3' #coloquei o caminho da música da fase 1

#configuração da tela
largura = 640 #largura inicial da janela do jogo
altura = 480 #altura inicial da janela do jogo
tela = pygame.display.set_mode((largura, altura), RESIZABLE) #criei a janela e deixei ela redimensionável
pygame.display.set_caption("Byte in Space") #dei um título à janela
icone = pygame.image.load('imagens/icone_janela.png') #carreguei o ícone da janela
pygame.display.set_icon(icone) #defini o ícone na janela

#carregar imagens
imagem_menu_original = pygame.image.load('imagens/imagem_menu.png') #carrega a imagem do menu principal (original)
imagem_menu = pygame.transform.scale(imagem_menu_original, (largura, altura)) #ajusto a imagem do menu ao tamanho atual da tela

cenario_original = pygame.image.load('imagens/cenario1.png').convert() #carrega a imagem do cenário do jogo
cenario = pygame.transform.scale(cenario_original, (largura, altura)) #ajusto o cenário ao tamanho da tela

#variáveis de controle do cenário
cenario_y1 = 0 #posição inicial do primeiro fundo do cenário
cenario_y2 = -altura #posição inicial do segundo fundo (logo acima da tela para efeito contínuo)

altura_base = 480 #essa vai ser a altura "original" da tela, para servir de referência
velocidade_base = 0.5 #aqui defino a velocidade que quero usar quando a altura da tela for igual à altura_base
velocidade_cenario = velocidade_base * (altura / altura_base) #aqui faço a velocidade se ajustar proporcionalmente à altura da janela

#função para criar botões proporcionais
def criar_botoes(largura, altura): #essa função recebe a largura e altura da tela para criar os botões com tamanhos e posições proporcionais
    botao_start = pygame.Rect(largura * 0.4, altura * 0.45, largura * 0.25, altura * 0.1) #botão "Iniciar Jogo"
    botao_diffcuty = pygame.Rect(largura * 0.4, altura * 0.6, largura * 0.25, altura * 0.1) #botão "Dificuldade"
    botao_credits = pygame.Rect(largura * 0.4, altura * 0.75, largura * 0.25, altura * 0.1) #botão "Créditos"
    return botao_start, botao_diffcuty, botao_credits

botao_start, botao_diffcuty, botao_credits = criar_botoes(largura, altura) #crio os botões usando a função acima

#estado do jogo
jogo_rodando = False  #variável que controla se o jogo está no menu ou rodando

#configurar a fonte para o texto "Fase 1"
pygame.font.init() #inicializa o módulo de fontes do pygame
fonte_fase = pygame.font.SysFont(None, 60) #None usa a fonte padrão do sistema, tamanho 60
texto_fase = fonte_fase.render('Fase 1', True, (255, 255, 255)) #cria o texto com cor branca

mostrar_texto_fase = False #controle para exibir o texto "Fase 1"
tempo_inicio_fase = 0 #tempo que a fase começou (usado para saber quando parar de mostrar o texto)

#largura e altura nave
nave_largura = 75
nave_altura = 75

#carrega a imagem da nave do jogador
sprite_nave = pygame.image.load('imagens/sprite_nave.png') #carrego o sprite da nave
sprite_nave = pygame.transform.scale(sprite_nave, (75, 75)) #ajusto o tamanho da nave

#posição inicial da nave (vou colocar no meio da tela na parte inferior)
nave_x = largura // 2 - 25 #a nave tem 50px de largura, então centralizei
nave_y = altura - 80 #coloquei a nave um pouco acima da borda inferior

velocidade_nave = 4 #define a velocidade com que a nave se move

#lista para armazenar os tiros disparados
tiros = [] #aqui vão ficar todos os tiros ativos na tela

#carrega o som do tiro
som_tiro = pygame.mixer.Sound('musicas/tiro.mp3') #carrego o som de tiro (formato WAV é melhor para efeitos curtos)
som_tiro.set_volume(1.0) #aqui aumentei o som do tiro (estava achando baixo)

#velocidade dos tiros
velocidade_tiro = 10 #velocidade com que os tiros sobem na tela

#cria um relógio para controlar a taxa de atualização (FPS)
clock = pygame.time.Clock()
fps = 60  # define 60 frames por segundo

#inimigos
# carrega sprite de inimigo
sprite_inimigo = pygame.image.load('imagens/sprite_inimigo.png')
sprite_inimigo = pygame.transform.scale(sprite_inimigo, (40, 40))  # ajusta tamanho conforme necessário

# carrega sprite do item coletável
sprite_item = pygame.image.load('imagens/item1.png')
sprite_item = pygame.transform.scale(sprite_item, (30, 30))

inimigos = []  # lista de inimigos ativos
itens = []     # lista de itens dropados

#altura máxima que os inimigos podem descer antes de parar (não quero que eles vão até o fim da tela)
y_max_inimigo = altura // 2  #aqui estou dizendo que os inimigos vão parar no meio da tela (metade da altura total)

#função para criar inimigos novos
def criar_inimigo(): #essa função serve para criar inimigos em posições aleatórias no topo da tela
    x = randint(0, largura - 40)  #aqui escolho uma posição X aleatória (lembrando que 40 é a largura do inimigo)
    y = randint(-200, -40)  #aqui coloco o inimigo fora da tela, para ele "descer" até o limite
    return [x, y]  #retorno um inimigo como [posição_x, posição_y]

#agora vou aumentar a quantidade inicial de inimigos
for _ in range(15):  #vou criar 15 inimigos logo no início (mais inimigos = mais ação hehe)
    inimigos.append(criar_inimigo())  #adiciono cada inimigo criado na lista de inimigos

#variáveis para controlar a aparição de novos inimigos durante o jogo
tempo_ultimo_inimigo = pygame.time.get_ticks()  #tempo do último inimigo criado (começa agora)
intervalo_spawn_inimigo = 1500  #tempo entre um inimigo e outro (em milissegundos) — 1500ms = 1,5 segundos

contagem_itens = 0  # contador de itens coletados
fonte_item = pygame.font.SysFont(None, 30)

#variáveis para controlar o Game Over
game_over = False  #começa como False porque o jogador ainda não perdeu
tempo_game_over = 0  #tempo que o game over começou
fonte_game_over = pygame.font.SysFont(None, 80)  #fonte grande para o texto de Game Over
texto_game_over = fonte_game_over.render('GAME OVER', True, (255, 0, 0))  #texto vermelho grandão

#loop principal
while True:
    clock.tick(fps)  # limita o jogo para não ultrapassar 60 FPS

    for event in pygame.event.get(): #verifica todos os eventos que ocorreram
        if event.type == QUIT: #se o evento for fechar a janela
            pygame.quit()
            exit()

        if event.type == VIDEORESIZE: #se a janela for redimensionada
            largura, altura = event.w, event.h
            tela = pygame.display.set_mode((largura, altura), RESIZABLE)
            imagem_menu = pygame.transform.scale(imagem_menu_original, (largura, altura))
            cenario = pygame.transform.scale(cenario_original, (largura, altura))
            botao_start, botao_diffcuty, botao_credits = criar_botoes(largura, altura)
            cenario_y1 = 0
            cenario_y2 = -altura
            velocidade_cenario = velocidade_base * (altura / altura_base)
            y_max_inimigo = altura // 2  # recalcula limite de descida

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if not jogo_rodando and not game_over:
                if botao_start.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musica_fase1)
                    pygame.mixer.music.play(-1)
                    jogo_rodando = True
                    mostrar_texto_fase = True
                    tempo_inicio_fase = pygame.time.get_ticks()
                    inimigos.clear()
                    itens.clear()
                    tiros.clear()
                    contagem_itens = 0
                    for _ in range(15):
                        inimigos.append(criar_inimigo())
                elif botao_diffcuty.collidepoint(event.pos):
                    print('dificuldade')
                elif botao_credits.collidepoint(event.pos):
                    print("Mostrar créditos")

        if event.type == KEYDOWN and jogo_rodando and not game_over:
            if event.key == K_z:
                tiros.append([nave_x + 23, nave_y])
                som_tiro.play()

    #se o jogo está rodando e o jogador não perdeu ainda
    if jogo_rodando and not game_over:
        
        #movimentação da nave
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT] or teclas[K_a]:
            nave_x -= velocidade_nave
        if teclas[K_RIGHT] or teclas[K_d]:
            nave_x += velocidade_nave
        if teclas[K_UP] or teclas[K_w]:
            nave_y -= velocidade_nave
        if teclas[K_DOWN] or teclas[K_s]:
            nave_y += velocidade_nave

        # limites
        if nave_x < 0:
            nave_x = 0
        if nave_x > largura - nave_largura:
            nave_x = largura - nave_largura
        if nave_y < 0:
            nave_y = 0
        if nave_y > altura - nave_altura:
            nave_y = altura - nave_altura

        # cenário
        cenario_y1 += velocidade_cenario
        cenario_y2 += velocidade_cenario
        if cenario_y1 >= altura:
            cenario_y1 = -altura
        if cenario_y2 >= altura:
            cenario_y2 = -altura
        tela.blit(cenario, (0, cenario_y1))
        tela.blit(cenario, (0, cenario_y2))

        # texto "Fase 1"
        if mostrar_texto_fase:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - tempo_inicio_fase <= 2000:
                texto_rect = texto_fase.get_rect(center=(largura // 2, altura // 2))
                tela.blit(texto_fase, texto_rect)
            else:
                mostrar_texto_fase = False

        #nave e retângulo para colisões
        tela.blit(sprite_nave, (nave_x, nave_y))
        rect_nave = pygame.Rect(nave_x, nave_y, nave_largura, nave_altura)

        #tiros
        for tiro in tiros[:]:
            tiro[1] -= velocidade_tiro
            if tiro[1] < 0:
                tiros.remove(tiro)
            else:
                pygame.draw.rect(tela, (255, 0, 0), (tiro[0], tiro[1], 4, 10))

        #inimigos
        for inimigo in inimigos[:]:
            if inimigo[1] < y_max_inimigo:
                inimigo[1] += 1
            tela.blit(sprite_inimigo, (inimigo[0], inimigo[1]))

            #colisão tiro × inimigo
            for tiro in tiros[:]:
                if pygame.Rect(inimigo[0], inimigo[1], 40, 40).collidepoint(tiro[0], tiro[1]):
                    tiros.remove(tiro)
                    inimigos.remove(inimigo)
                    if randint(1, 10) <= 3:
                        itens.append([inimigo[0], inimigo[1]])
                    break

            #colisão nave × inimigo
            if rect_nave.colliderect(pygame.Rect(inimigo[0], inimigo[1], 40, 40)):
                game_over = True
                tempo_game_over = pygame.time.get_ticks()
                break

        #spawn de novos inimigos
        if pygame.time.get_ticks() - tempo_ultimo_inimigo >= intervalo_spawn_inimigo:
            inimigos.append(criar_inimigo())
            tempo_ultimo_inimigo = pygame.time.get_ticks()

        #itens
        for item in itens[:]:
            tela.blit(sprite_item, (item[0], item[1]))
            rect_item = pygame.Rect(item[0], item[1], 30, 30)
            if rect_nave.colliderect(rect_item):
                itens.remove(item)
                contagem_itens += 1

        #contador de itens
        texto_contagem = fonte_item.render(f'Itens: {contagem_itens}', True, (255, 255, 0))
        tela.blit(texto_contagem, (largura - texto_contagem.get_width() - 10, 10))

    #se o jogador perdeu
    elif game_over:
        tela.blit(cenario, (0, 0))
        tela.blit(texto_game_over, (largura // 2 - texto_game_over.get_width() // 2,
                                    altura // 2 - texto_game_over.get_height() // 2))
        if pygame.time.get_ticks() - tempo_game_over >= 2000:
            game_over = False
            jogo_rodando = False

    else:
        tela.blit(imagem_menu, (0, 0))

    pygame.display.update()

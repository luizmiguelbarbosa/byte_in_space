# Código da janela do jogo.
# esse é o primeiro passo, vai ser na janela aonde o jogo será exibido

# vamos primeiro importar a biblioteca pygame
import pygame
# agora vou importar um submódulo que está dentro da biblioteca do pygame
from pygame.locals import * # esse submódulo ele contém todas as constantes e funções que a gente vai usar no nosso script. Esse asteristico no diz que dentro do meu submódulo locals, eu vou estar importando todas as funções e todas as constantes que o submódulo locals contém, e o submódulo locals, por sua vez, está dentro da biblioteca pygame
# agora vou importar uma função que está dentro do módulo sys
from sys import exit # Essa função que eu importei serve para fechar a janela 

from random import randint # para adicionar coisas aleatória heheh isso vai ser massa :)

# Novo import para a cutscene de vídeo
import cv2 # essa é a biblioteca OpenCV, que vamos usar para ler o vídeo

# Classe para representar itens coletáveis que substituem "item"
class Coletavel:
    TAM = 30

    def __init__(self, x, y, tipo):
        # tipo deve ser 'computador', 'circuito' ou 'dados'
        self.tipo = tipo
        self.rect = pygame.Rect(x, y, self.TAM, self.TAM)

    def desenhar(self, superficie):
        # desenha usando sprite específico do tipo
        superficie.blit(sprite_coletaveis[self.tipo], self.rect.topleft)

# Agora que ja fizemos as importações, vamos começar o script de fato 
pygame.init() # inicializa o pygame
pygame.mixer.init() # inicializa o módulo de som

# a música do menu só vai tocar depois da cutscene, então vou comentar essa parte
# pygame.mixer.music.load('musicas/musica_jogo.mp3') # subi a musica
# pygame.mixer.music.play(-1) # -1 significa que a musica vai tocar em loop infinito
pygame.mixer.music.set_volume(0.4) # diminui um pouco o som do jogo (estava muito alto)

# carrega a música da fase 1
musica_fase1 = 'musicas/musica_start.mp3' # coloquei o caminho da música da fase 1

# configuração da tela
largura = 640 # largura inicial da janela do jogo
altura = 480 # altura inicial da janela do jogo
tela = pygame.display.set_mode((largura, altura), RESIZABLE) # criei a janela e deixei ela redimensionável
pygame.display.set_caption("Byte in Space") # dei um título à janela
icone = pygame.image.load('imagens/icone_janela.png') # carreguei o ícone da janela
pygame.display.set_icon(icone) # defini o ícone na janela

# carregar imagens
imagem_menu_original = pygame.image.load('imagens/imagem_menu.png') # carrega a imagem do menu principal (original)
imagem_menu = pygame.transform.scale(imagem_menu_original, (largura, altura)) # ajusto a imagem do menu ao tamanho atual da tela

cenario_original = pygame.image.load('imagens/cenario1.png').convert() # carrega a imagem do cenário do jogo
cenario = pygame.transform.scale(cenario_original, (largura, altura)) # ajusto o cenário ao tamanho da tela

# variáveis de controle do cenário
cenario_y1 = 0 # posição inicial do primeiro fundo do cenário
cenario_y2 = -altura # posição inicial do segundo fundo (logo acima da tela para efeito contínuo)

altura_base = 480 # essa vai ser a altura "original" da tela, para servir de referência
velocidade_base = 0.5 # aqui defino a velocidade que quero usar quando a altura da tela for igual à altura_base
velocidade_cenario = velocidade_base * (altura / altura_base) # aqui faço a velocidade se ajustar proporcionalmente à altura da janela

# função para criar botões proporcionais
def criar_botoes(largura, altura): # essa função recebe a largura e altura da tela para criar os botões com tamanhos e posições proporcionais
    botao_start = pygame.Rect(largura * 0.4, altura * 0.45, largura * 0.25, altura * 0.1) # botão "Iniciar Jogo"
    botao_diffcuty = pygame.Rect(largura * 0.4, altura * 0.6, largura * 0.25, altura * 0.1) # botão "Dificuldade"
    botao_credits = pygame.Rect(largura * 0.4, altura * 0.75, largura * 0.25, altura * 0.1) # botão "Créditos"
    return botao_start, botao_diffcuty, botao_credits

botao_start, botao_diffcuty, botao_credits = criar_botoes(largura, altura) # crio os botões usando a função acima

# estado do jogo
# agora temos um novo estado, a cutscene, que começa como True
cutscene_ativa = True
jogo_rodando = False  # variável que controla se o jogo está no menu ou rodando

# configurar a fonte para o texto "Fase 1"
pygame.font.init() # inicializa o módulo de fontes do pygame
fonte_fase = pygame.font.SysFont(None, 60) # None usa a fonte padrão do sistema, tamanho 60
texto_fase = fonte_fase.render('Fase 1', True, (255, 255, 255)) # cria o texto com cor branca

mostrar_texto_fase = False # controle para exibir o texto "Fase 1"
tempo_inicio_fase = 0 # tempo que a fase começou (usado para saber quando parar de mostrar o texto)

# largura e altura nave
nave_largura = 75
nave_altura = 75

# carrega a imagem da nave do jogador
sprite_nave = pygame.image.load('imagens/sprite_nave.png') # carrego o sprite da nave
sprite_nave = pygame.transform.scale(sprite_nave, (75, 75)) # ajusto o tamanho da nave

# posição inicial da nave (vou colocar no meio da tela na parte inferior)
nave_x = largura // 2 - 25 # a nave tem 50px de largura, então centralizei
nave_y = altura - 80 # coloquei a nave um pouco acima da borda inferior

velocidade_nave_base = 4  # velocidade base da nave
velocidade_nave = velocidade_nave_base  # velocidade atual (afetada por TURBO)

# lista para armazenar os tiros disparados
tiros = [] # aqui vão ficar todos os tiros ativos na tela

# carrega o som do tiro
som_tiro = pygame.mixer.Sound('musicas/tiro.mp3') # carrego o som de tiro (formato WAV é melhor para efeitos curtos)
som_tiro.set_volume(1.0) # aqui aumentei o som do tiro (estava achando baixo)

# velocidade dos tiros
velocidade_tiro = 10 # velocidade com que os tiros sobem na tela

# cria um relógio para controlar a taxa de atualização (FPS)
clock = pygame.time.Clock()
fps = 60  # define 60 frames por segundo

# inimigos
# carrega sprite de inimigo
sprite_inimigo = pygame.image.load('imagens/sprite_nave.png')
sprite_inimigo = pygame.transform.scale(sprite_inimigo, (40, 40))  # ajusta tamanho conforme necessário


inimigos = []  # lista de inimigos ativos
coletaveis = []      # lista de coletáveis ativos
velocidade_coletavel = 2 #aqui defino a velocidade de queda dos coletáveis, como se fosse a gravidade :)

# altura máxima que os inimigos podem descer antes de parar (não quero que eles vão até o fim da tela)
y_max_inimigo = altura // 2  # aqui estou dizendo que os inimigos vão parar no meio da tela (metade da altura total)

# função para criar inimigos novos
def criar_inimigo(): # essa função serve para criar inimigos em posições aleatórias no topo da tela
    x = randint(0, largura - 40)  # aqui escolho uma posição X aleatória (lembrando que 40 é a largura do inimigo)
    y = randint(-200, -40)  # aqui coloco o inimigo fora da tela, para ele "descer" até o limite
    return [x, y]  # retorno um inimigo como [posição_x, posição_y]

# agora vou aumentar a quantidade inicial de inimigos
for _ in range(15):  # vou criar 15 inimigos logo no início (mais inimigos = mais ação hehe)
    inimigos.append(criar_inimigo())  # adiciono cada inimigo criado na lista de inimigos

# variáveis para controlar a aparição de novos inimigos durante o jogo
tempo_ultimo_inimigo = pygame.time.get_ticks()  # tempo do último inimigo criado (começa agora)
intervalo_spawn_inimigo = 1500  # tempo entre um inimigo e outro (em milissegundos) — 1500ms = 1,5 segundos

fonte_item = pygame.font.SysFont(None, 30)

# contagem separada por tipo
contagem_coletaveis = {'computador': 0, 'circuito': 0, 'dados': 0}

# efeitos temporários (em milissegundos)
EFEITO_DURACAO = 10000
imune_ate = 0
turbo_ate = 0
furia_ate = 0

# sprites dos coletáveis
sprite_computador = pygame.image.load('imagens/computador.png')
sprite_circuito   = pygame.image.load('imagens/circuito.png')
sprite_dados      = pygame.image.load('imagens/dados.png')

sprite_coletaveis = {
    'computador': pygame.transform.scale(sprite_computador, (Coletavel.TAM, Coletavel.TAM)),
    'circuito':   pygame.transform.scale(sprite_circuito,   (Coletavel.TAM, Coletavel.TAM)),
    'dados':      pygame.transform.scale(sprite_dados,      (Coletavel.TAM, Coletavel.TAM)),
}

# variáveis para controlar o Game Over
game_over = False  # começa como False porque o jogador ainda não perdeu
tempo_game_over = 0  # tempo que o game over começou
fonte_game_over = pygame.font.SysFont(None, 80)  # fonte grande para o texto de Game Over
texto_game_over = fonte_game_over.render('GAME OVER', True, (255, 0, 0))  # texto vermelho grandão

# Carrega o vídeo da cutscene com o OpenCV
cutscene_video = cv2.VideoCapture('videos/cutscene1.mp4')

# loop principal
while True:
    clock.tick(fps)  # limita o jogo para não ultrapassar 60 FPS

    for event in pygame.event.get(): # verifica todos os eventos que ocorreram
        if event.type == QUIT: # se o evento for fechar a janela
            # --- ADIÇÃO PARA LIBERAR O VÍDEO ---
            if cutscene_ativa:
                cutscene_video.release() # libera os recursos do vídeo
            # --------------------------------
            pygame.quit()
            exit()
        
        # se a cutscene estiver ativa, permite pular com um clique ou tecla
        if cutscene_ativa and (event.type == KEYDOWN or (event.type == MOUSEBUTTONDOWN and event.button == 1)):
            cutscene_ativa = False
            cutscene_video.release() # libera os recursos do vídeo
            # e agora sim, inicia a música do menu
            pygame.mixer.music.load('musicas/musica_jogo.mp3') 
            pygame.mixer.music.play(-1)

        if event.type == VIDEORESIZE: # se a janela for redimensionada
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
            if not jogo_rodando and not game_over and not cutscene_ativa: # verifica se não está no menu ou na cutscene
                if botao_start.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musica_fase1)
                    pygame.mixer.music.play(-1)
                    jogo_rodando = True
                    mostrar_texto_fase = True
                    tempo_inicio_fase = pygame.time.get_ticks()
                    inimigos.clear()
                    coletaveis.clear()
                    tiros.clear()
                    contagem_coletaveis = {'computador': 0, 'circuito': 0, 'dados': 0}
                    imune_ate = 0
                    turbo_ate = 0
                    furia_ate = 0
                    for _ in range(15):
                        inimigos.append(criar_inimigo())
                elif botao_diffcuty.collidepoint(event.pos):
                    print('dificuldade')
                elif botao_credits.collidepoint(event.pos):
                    print("Mostrar créditos")

        if event.type == KEYDOWN and jogo_rodando and not game_over:
            if event.key == K_SPACE:
                agora = pygame.time.get_ticks()
                centro_tiro = nave_x + nave_largura // 2 - 2
                if agora < furia_ate:
                    # tiro triplo durante FÚRIA
                    tiros.append([centro_tiro - 12, nave_y])
                    tiros.append([centro_tiro, nave_y])
                    tiros.append([centro_tiro + 12, nave_y])
                else:
                    tiros.append([centro_tiro, nave_y])
                som_tiro.play()

    # bloco para a cutscene
    if cutscene_ativa:
        # lê um novo frame do vídeo
        ret, frame = cutscene_video.read() 
        
        # se o vídeo ainda tiver frames para ler, desenha na tela
        if ret:
            # converte o frame do OpenCV para uma imagem do Pygame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # converte a cor (o OpenCV usa BGR e o Pygame usa RGB)
            frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")
            
            # redimensiona e desenha na tela
            tela.blit(pygame.transform.scale(frame, (largura, altura)), (0, 0))
        else:
            # se não houver mais frames, o vídeo acabou.
            cutscene_ativa = False
            cutscene_video.release() # libera o vídeo
            pygame.mixer.music.load('musicas/musica_jogo.mp3') 
            pygame.mixer.music.play(-1)

    # se o jogo está rodando e o jogador não perdeu ainda
    elif jogo_rodando and not game_over:
        # atualiza efeitos temporários
        agora = pygame.time.get_ticks()
        velocidade_nave = velocidade_nave_base * (2 if agora < turbo_ate else 1)
        
        # movimentação da nave
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

        # nave e retângulo para colisões
        tela.blit(sprite_nave, (nave_x, nave_y))
        rect_nave = pygame.Rect(nave_x, nave_y, nave_largura, nave_altura)
        # aura visual de ESCUDO quando ativo
        if pygame.time.get_ticks() < imune_ate:
            pygame.draw.rect(tela, (0, 200, 255), rect_nave.inflate(10, 10), 3, border_radius=6)

        # tiros
        for tiro in tiros[:]:
            tiro[1] -= velocidade_tiro
            if tiro[1] < 0:
                tiros.remove(tiro)
            else:
                pygame.draw.rect(tela, (255, 0, 0), (tiro[0], tiro[1], 4, 10))

        # inimigos
        for inimigo in inimigos[:]:
            if inimigo[1] < y_max_inimigo:
                inimigo[1] += 1
            tela.blit(sprite_inimigo, (inimigo[0], inimigo[1]))

            # colisão tiro × inimigo
            for tiro in tiros[:]:
                if pygame.Rect(inimigo[0], inimigo[1], 40, 40).collidepoint(tiro[0], tiro[1]):
                    tiros.remove(tiro)
                    inimigos.remove(inimigo)
                    if randint(1, 10) <= 3:
                        tipo_sorteado = ('computador', 'circuito', 'dados')[randint(0, 2)]
                        coletaveis.append(Coletavel(inimigo[0], inimigo[1], tipo_sorteado))
                    break

            # colisão nave × inimigo
            if rect_nave.colliderect(pygame.Rect(inimigo[0], inimigo[1], 40, 40)):
                if pygame.time.get_ticks() >= imune_ate:
                    game_over = True
                    tempo_game_over = pygame.time.get_ticks()
                # se está imune, ignora a colisão
                break

        # spawn de novos inimigos
        if pygame.time.get_ticks() - tempo_ultimo_inimigo >= intervalo_spawn_inimigo:
            inimigos.append(criar_inimigo())
            tempo_ultimo_inimigo = pygame.time.get_ticks()

        # coletáveis
        for c in coletaveis[:]:
            # adiciona gravidade, fazendo os itens descerem pela tela
            c.rect.y += velocidade_coletavel
            c.desenhar(tela)
            
            # se o coletável sair da tela, a gente remove ele da lista pra não pesar o jogo
            if c.rect.top > altura:
                coletaveis.remove(c)
                continue # pula para o próximo item, porque esse aqui já era!
            
            if rect_nave.colliderect(c.rect):
                coletaveis.remove(c)
                contagem_coletaveis[c.tipo] += 1
                # ativa efeito ao acumular 3
                if contagem_coletaveis[c.tipo] >= 3:
                    agora = pygame.time.get_ticks()
                    if c.tipo == 'computador':
                        imune_ate = agora + EFEITO_DURACAO  # escudo
                    elif c.tipo == 'circuito':
                        turbo_ate = agora + EFEITO_DURACAO  # turbo
                    elif c.tipo == 'dados':
                        furia_ate = agora + EFEITO_DURACAO  # tiro triplo
                    contagem_coletaveis[c.tipo] = 0

        # HUD: contadores por tipo no topo esquerdo
        texto_e = fonte_item.render(f'Computadores: {contagem_coletaveis["computador"]}/3', True, (0, 200, 255))
        texto_t = fonte_item.render(f'Circuitos: {contagem_coletaveis["circuito"]}/3',   True, (255, 200, 0))
        texto_f = fonte_item.render(f'Dados: {contagem_coletaveis["dados"]}/3',         True, (255, 80, 80))

        x_hud, y_hud = 10, 10

        tela.blit(texto_e, (x_hud, y_hud))
        tela.blit(texto_t, (x_hud, y_hud + texto_e.get_height() + 4))
        tela.blit(texto_f, (x_hud, y_hud + texto_e.get_height() + texto_t.get_height() + 8))

    # se o jogador perdeu
    elif game_over:
        tela.blit(cenario, (0, 0))
        tela.blit(texto_game_over, (largura // 2 - texto_game_over.get_width() // 2,
                                     altura // 2 - texto_game_over.get_height() // 2))
        if pygame.time.get_ticks() - tempo_game_over >= 2000:
            game_over = False
            jogo_rodando = False

    else:
        # Agora o menu só aparece depois da cutscene
        tela.blit(imagem_menu, (0, 0))

    pygame.display.update()
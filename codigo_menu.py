#Código da janela do jogo.
#esse é o primeiro passo, vai ser na janela aonde o jogo será exibido

#vamos primeiro importar a biblioteca pygame
import pygame
#agora vou importar um submódulo que está dentro da biblioteca do pygame
from pygame.locals import * #esse submódulo ele contém todas as constantes e funções que a gente vai usar no nosso script. Esse asteristico no diz que dentro do meu submódulo locals, eu vou estar importando todas as funções e todas as constantes que o submódulo locals contém, e o submódulo locals, por sua vez, está dentro da biblioteca pygame
#agora vou importar uma função que está dentro do módulo sys
from sys import exit #Essa função que eu importei serve para fechar a janela 

#Agora que ja fizemos as importações, vamos começar o script de fato 
#Primeiramente vamos inicializar todas as funções e variáveis da biblioteca pygame
pygame.init()

#vou inicializar o módulo do som (para por músicas)
pygame.mixer.init()

#tocar a música no menu do jogo 
pygame.mixer.music.load('D:/Users/lmsbn/Desktop/Projeto IP/Musicas do jogo/Musica Menu do jogo.mp3') #subi a musica
pygame.mixer.music.play(-1) #-1 significa que a musica vai tocar em loop infinito 

#agora vamos definir o objeto que será a nossa tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura), RESIZABLE) #Essa flag RESIZABLE, serve para permitir que a jenela seja redimensionável/maximizável

#aqui vou dar um nome para a janela
pygame.display.set_caption("Byte in Space")

#vou fazer aqui a parte do icone da janela do jogo 
icone = pygame.image.load('D:/Users/lmsbn/Desktop/Projeto IP/Imagens/Icone da janela do jogo.png')  #Caminho do icone do jogo
pygame.display.set_icon(icone)

#Agora vou programar o menu principal do jogo com base nas suas coordenadas
#primeiro vou carregar a imagem do menu
#aqui carreguei a imagem (sem redimensionar ainda)
imagem_menu_original = pygame.image.load('D:/Users/lmsbn/Desktop/Projeto IP/Imagens/Imagem menu do jogo.png')
imagem_menu = pygame.transform.scale(imagem_menu_original,(largura,altura)) #coloquei na escala das variaveis que defini antes

#agora vou fazer as variaveis das coordenadas (fiz isso para fazer retângulos)
botao_start = pygame.Rect(420, 439, 625, 101)
botao_continue = pygame.Rect(420, 571, 625, 110)
botao_settings = pygame.Rect(420, 710, 625, 110)
botao_credits = pygame.Rect(420, 860, 625, 100)

#agora vou criar o loop principal do jogo
while True:
    for event in pygame.event.get(): #Esse loop for vai ter a tarefa de a cada interação do meu loop principal, de checar se algum eveneto ocorreu 

        if event.type == QUIT: #como eu quero que a minha janela feche quando eu apertar em fechar, eu vou criar essa condição 
            pygame.quit()
            exit() #chamo a função que importei para fechar o jogo

        if event.type == VIDEORESIZE:#atualiza a largura e a altura da janela redimensionada
            largura,altura = event.w, event.h #aqui a gente pega o novo tamanho da janela após o redimensionamento, o event.w é a nova largura da janela. e o event.h é a nova altura da janela
            tela = pygame.display.set_mode((largura, altura), RESIZABLE) #aqui nos estamos recriando a tela do jogo com um novo tamanho

            #redimensiona a imagem do menu para o novo tamanho
            imagem_menu = pygame.transform.scale(imagem_menu_original, (largura, altura))

        if event.type == MOUSEBUTTONDOWN and event.button ==1: #verifica se o evento é o clique de um mouse e se o botão precionado do mause é o esquerdo
            if botao_start.collidepoint(event.pos): #verifica se a posição do clique está dentro da área do botão "Start game", a função retorna true se o ponto clicado está dentro do retângulo
                print("iniciar jogo") #so coloquei esse print temporariamente, para saber se está funcionando
            elif botao_continue.collidepoint(event.pos):#mesma ideia que escrevi anteriormente
                print('continuar jogo')
            elif botao_settings.collidepoint(event.pos): 
                print("Abrir configurações")
            elif botao_credits.collidepoint(event.pos):
                print("Mostrar créditos")

    #desenha a imagem do menu como o fundo da janela
    tela.blit(imagem_menu, (0, 0))

    pygame.display.update() #Essa linha faz com que a cada interação do meu loop principal do jogo, ela atualiza a tela do jogo. Se não tiver essa linha, meu jogo vai rodar uma vez e vai travar, sendo assim, o jogo tem que ser um processo contínuo, tem que estar sempre atualizando
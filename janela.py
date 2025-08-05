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

#agora vamos definir o objeto que será a nossa tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura), RESIZABLE) #Essa flag RESIZABLE, serve para permitir que a jenela seja redimensionável/maximizável

#aqui vou dar um nome para a janela
pygame.display.set_caption("Byte in Space")

#vou fazer aqui a parte do icone da janela do jogo 
icone = pygame.image.load('D:/Users/lmsbn/Desktop/Projeto IP/Imagens/Icone da janela do jogo.png')  #Caminho do icone do jogo
pygame.display.set_icon(icone)

#agora vou criar o loop principal do jogo
while True:
    for event in pygame.event.get(): #Esse loop for vai ter a tarefa de a cada interação do meu loop principal, de checar se algum eveneto ocorreu 
        if event.type == QUIT: #como eu quero que a minha janela feche quando eu apertar em fechar, eu vou criar essa condição 
            pygame.quit()
            exit() #chamo a função que importei para fechar o jogo
    pygame.display.update() #Essa linha faz com que a cada interação do meu loop principal do jogo, ela atualiza a tela do jogo. Se não tiver essa linha, meu jogo vai rodar uma vez e vai travar, sendo assim, o jogo tem que ser um processo contínuo, tem que estar sempre atualizando
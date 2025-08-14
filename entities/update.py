import pygame
from config import *
from random import randint
from entities.coletavel import Coletavel
from entities.inimigo import Inimigo
from entities.explosion import Explosion
from entities.mensagem import Mensagem
from entities.bullets_enemies import Bullet

explosions_group = pygame.sprite.Group()

def atualizar(estado): #FUNÇÃO CHAMADA POR ITERAÇÃO DE LOOPING PRINCIPAL
    if estado["jogo_rodando"] and not estado["game_over"]:
        agora = pygame.time.get_ticks()
        estado["velocidade_nave"] = VELOCIDADE_NAVE_BASE * (2 if agora < estado["turbo_ate"] else 1)

        teclas = pygame.key.get_pressed()
        # Movimento nave
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            estado["nave_x"] -= estado["velocidade_nave"]
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            estado["nave_x"] += estado["velocidade_nave"]
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            estado["nave_y"] -= estado["velocidade_nave"]
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            estado["nave_y"] += estado["velocidade_nave"]

        # Limites da nave
        if estado["nave_x"] < 0:
            estado["nave_x"] = 0
        if estado["nave_x"] > estado["largura"] - NAVE_LARGURA:
            estado["nave_x"] = estado["largura"] - NAVE_LARGURA
        if estado["nave_y"] < 0:
            estado["nave_y"] = 0
        if estado["nave_y"] > estado["altura"] - NAVE_ALTURA:
            estado["nave_y"] = estado["altura"] - NAVE_ALTURA

        # Atualiza cenário
        estado["cenario_y1"] += estado["velocidade_cenario"]
        estado["cenario_y2"] += estado["velocidade_cenario"]
        if estado["cenario_y1"] >= estado["altura"]:
            estado["cenario_y1"] = -estado["altura"]
        if estado["cenario_y2"] >= estado["altura"]:
            estado["cenario_y2"] = -estado["altura"]
        
        
        #TRATA DE ATUALIZAR O ESTADO DOS INIMIGOS
        for inimigo in estado["inimigos"][:]:
            inimigo.atualizar()
            if inimigo.y > ALTURA:
                 estado["inimigos"].remove(inimigo)

            #COLISÃO TIRO X INIMIGO
            for tiro in estado["tiros"][:]:
                if inimigo.get_rect().collidepoint(tiro[0], tiro[1]):
                    #APAGA O TIRO E O INIMIGO COLIDIDO DOS ARRAYS E, PORTANTO, DA RENDERIZAÇÃO E ATUALIZAÇÕES DE MOVIMENTOS
                    estado["tiros"].remove(tiro)
                    estado["inimigos"].remove(inimigo)
                    #GERA UM OBJETO EXPLOSÃO
                    explosion = Explosion(inimigo.x, inimigo.y)
                    explosions_group.add(explosion)
                    estado["mensagens"].add(Mensagem("+15", (255, 255, 0), inimigo.x, inimigo.y))
                    
                    #CONDIÇÃO DE VITÓRIA
                    estado["pontuacao"] += 15
                    if estado["pontuacao"] >= MAX_PONTUACAO:
                        estado["game_win"] = True
                        estado["tempo_game_win"] = pygame.time.get_ticks()
                        break
                    
                    #CHANCE DE 3/10 DE DROPAR UM COLETÁVEL
                    if randint(1, 10) <= 3:
                        tipo_sorteado = ('computador', 'circuito', 'dados')[randint(0, 2)]
                        estado["coletaveis"].append(Coletavel(inimigo.x, inimigo.y, tipo_sorteado))
                    break
            
            #COLISÃO NAVE x INIMIGO
            rect_nave = pygame.Rect(estado["nave_x"]+10, estado["nave_y"]+20, NAVE_LARGURA-20, NAVE_ALTURA-35) 
            if rect_nave.colliderect(inimigo.get_rect()):
                if agora >= estado["imune_ate"]:
                    estado["game_over"] = True
                    estado["tempo_game_over"] = pygame.time.get_ticks()
                break
        #COLISÃO NAVE x BULLET
        rect_nave = pygame.Rect(estado["nave_x"]+10, estado["nave_y"]+20, NAVE_LARGURA-20, NAVE_ALTURA-35) 
        for bullet in estado["bullets"]:
            if agora >= estado["imune_ate"]:
                if rect_nave.colliderect(bullet.rect):
                    estado["game_over"] = True
                    estado["bullets"].empty()
                    estado["tempo_game_over"] = pygame.time.get_ticks()
                break

        estado["bullets"].update()
        #ATUALIZA OS OBJETOS MENSAGENS DENTRO DO GRUPO ESTADO["MENSAGENS"]
        estado["mensagens"].update()

        #RESPONSÁVEL POR SPAWNAR INIMIGOS
        if agora - estado["tempo_ultimo_inimigo"] >= INTERVALO_SPAWN_INIMIGO and len(estado["inimigos"]) <= QUANT_INIMIGOS_MAX:
            estado["inimigos"].append(Inimigo(estado["largura"], estado["altura"], estado["sprite_inimigo"]))
            estado["tempo_ultimo_inimigo"] = agora
        
        for inimigo in estado["inimigos"][:]:
            if inimigo.y > 0:
                num = randint(1, 500)
                if num == 1:
                    estado["bullets"].add(Bullet(5, inimigo.x+30, inimigo.y+30))
        # Atualiza tiros
        for tiro in estado["tiros"][:]:
            tiro[1] -= VELOCIDADE_TIRO
            if tiro[1] < 0:
                estado["tiros"].remove(tiro)

        # Atualiza coletáveis
        for c in estado["coletaveis"][:]:
            c.rect.y += VELOCIDADE_COLETAVEL
            if c.rect.top > estado["altura"]:
                estado["coletaveis"].remove(c)
                continue

            rect_nave = pygame.Rect(estado["nave_x"], estado["nave_y"], NAVE_LARGURA, NAVE_ALTURA)
            if rect_nave.colliderect(c.rect):
                estado["coletaveis"].remove(c)
                estado["contagem_coletaveis"][c.tipo] += 1
                if estado["contagem_coletaveis"][c.tipo] >= 3:
                    if c.tipo == 'computador':
                        estado["imune_ate"] = agora + EFEITO_DURACAO
                    elif c.tipo == 'circuito':
                        estado["turbo_ate"] = agora + EFEITO_DURACAO
                    elif c.tipo == 'dados':
                        estado["furia_ate"] = agora + EFEITO_DURACAO
                    estado["contagem_coletaveis"][c.tipo] = 0
    
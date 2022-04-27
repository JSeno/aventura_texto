"""
Um rpg de aventura em texto com uma simples história de um héroi que vai salvar uma princes de um dragão.
Farei uma pequena alteração no jogo, ele será um aventureiro de uma guilda que deve completar missões dependendo de rank.

Os rank serão F,



"""
# Importando pygame
import pygame

# Inicializando o pygame
pygame.init()

# Tela de título
pygame.display.set_caption("Heroi cliche")

print('Seja bem vindo ao:')
print('+-------------------------------------------------+')
print('|                                                 |')
print('|                 Heroi Clichê                    |')
print('|                                                 |')
print('+-------------------------------------------------+')
print('\n')
print('Gostaria de jogar?')
print('\n')
print('Digite 1 para sim e 2 para não')
print('\n')

primeira_resposta = int(input())
if primeira_resposta == 1:
    print('Vamos começar!')
else:
    print('Tchau!')
    exit()

print('Qual o seu nome?')
nome = input()
print('Olá, ' + nome + '!')

print('Você é um cavaleiro, um arqueiro ou um mago?')
print('Digite 1 para cavaleiro, 2 para arqueiro ou 3 para mago')

classe_escolhida = int(input())
if classe_escolhida == 1:
    print('Você escolheu a classe cavaleiro!')
elif classe_escolhida == 2:
    print('Você escolheu a classe arqueiro!')
elif classe_escolhida == 3:
    print('Você escolheu a classe mago!')
else:
    print('Você não escolheu nenhuma classe!')
    exit()







"""
Você é um aventureiro em um mundo de fantasia, para conseguir seu ganha pão você deve trabalhar fazendo missões
para a guilda de aventureiros.

Colocarei um sistema de rank conforme você cumpre suas missões. ganha pontos para subir de rank.
Os rank serão F, E, D, C, B, A, S.
implementarei um pequeno sistema de batalha, conforme sobe o rank terá missões de batalha.
sitema de batalha será formado pelas funções:
destreza x agilidade para acerto e esquiva
ataque fisíco x defesa fisíca
ataque magico x defesa magica

Estarei usando um atributo fixo dependendo dos atributos dos personagens e um numero aleatório de 1 a 6 similando um dado.

"""
from missoes import Missoes

# Herói Clichê v.0.1
# Tela de título
print('Seja bem vindo ao:')
print('+-------------------------------------------------+')
print('|                                                 |')
print('|                 Heroi Clichê                    |')
print('|                                                 |')
print('+-------------------------------------------------+')
print('\n')
print('Gostaria de jogar?')
print('Por favor digite sim ou não')

enter_play = input('Digite: ')
if enter_play == 'sim' or enter_play == 'Sim' or enter_play == 's' or enter_play == 'S':
    print('Ok, vamos começar!')
else:
    print('Tchau!')
    exit()


name_hero = input('Por favor me diga qual é seu nome aventureiro:\n ')
hero_class = {1: 'Guerreiro', 2: 'Mago', 3: 'Arqueiro'}

print('Posso saber qual é sua classe de personagem?')
hero_class_choice = input('Digite 1 para Guerreiro, 2 para Mago e 3 para Arqueiro: ')
if hero_class_choice == '1':
    hero_class_choice = hero_class[1]
elif hero_class_choice == '2':
    hero_class_choice = hero_class[2]
elif hero_class_choice == '3':
    hero_class_choice = hero_class[3]
else:
    print('Você não escolheu uma classe válida, vamos começar de novo')
    exit()
print('Vamos confirmar seu registro então, seu nome é: ' + name_hero.title() + ' e sua classe é: ' + hero_class_choice)
print('Como você está começando agora, você pertence ao RANK: F')
print('Só posso te passar pequenas missões dependendo de seu rank, quando você completar 10 missões do seu rank, você subirá de rank')
print('Vamos começar!')
print('\n')

# Missões  de Rank concluidas, começa em 0 cada vez que completa soma +1 quando chega a 10 muda de rank
rank_f = 0
rank_e = 0
rank_d = 0
rank_c = 0
rank_b = 0
rank_a = 0
rank_s = 0


print('Hoje temos somente essas missões para você, escolha qual deseja começar a fazer')

# As missões estão na classe Missoes, vou importar de lá elas

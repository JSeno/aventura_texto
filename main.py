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

name_hero = input('Por favor me diga qual é seu nome aventureiro: ')
print(f'Prazer em te conhecer {name_hero}')
print('\n')
print('Então vamos começar a sua aventura!')
print('\n')
print('Qual tipo de personagem você é?')
print('Por acaso um tipo guerreiro, um tipo mago ou um tipo ladino?')
print('\n')

# TODO: colocar escolha de job como dicionário e escolher pelo .values() e .keys()
job_hero_choice = input('Digite: ')
if job_hero_choice == 'guerreiro' or job_hero_choice == 'Guerreiro' or job_hero_choice == 'g' or job_hero_choice == 'G':
    job_hero_choice = 'guerreiro'
    print('Então você é um guerreiro, gosta de ir com tudo esmagando seus inimigos!')
elif job_hero_choice == 'mago' or job_hero_choice == 'Mago' or job_hero_choice == 'm' or job_hero_choice == 'M':
    job_hero_choice = 'mago'
    print('Então você é um mago, gosta de seus poderes mágicos!')
elif job_hero_choice == 'ladino' or job_hero_choice == 'Ladino' or job_hero_choice == 'l' or job_hero_choice == 'L':
    job_hero_choice = 'ladino'
    print('Então você é um ladino, gosta de correr atrás de tesouros e andar silenciosamente!')
else:
    print('Você não é um personagem válido!')
    exit()

# TODO: o copilot ajudou no dicionário mas não são todos atributos do jeito que quero pensarei e farei uma correção
# Atributos base do personagem
hero_b_atributos = {
        'nome': name_hero,
        'classe': job_hero_choice,
        'vida': 100,
        'mana': 100,
        'força': 10,
        'destreza': 10,
        'agilidade': 10,
        'inteligência': 10,
        'resistencia': 10,
}

# TODO: mudarei o formato das classes com dicionário ai dependendo da classe será acrestentado ou retirado atributos.
# Caso seu personagem seja um guerreiro
hero_c_guerreiro = {
        'nome': name_hero,
        'classe': job_hero_choice[0],
        'vida': hero_b_atributos['vida'] + 25,
        'mana': hero_b_atributos['mana'] / 3,
        'força': hero_b_atributos['força'] + 5,
        'destreza': hero_b_atributos['destreza'],
        'agilidade': hero_b_atributos['agilidade'],
        'inteligência': hero_b_atributos['inteligência'] - 5,
        'resistencia': hero_b_atributos['resistencia'] + 5,
}
print(hero_c_guerreiro.values())

import random

def jogar_dado():
    return random.randint(1, 6)

def avancar(posicao, quantidade):
    return posicao + quantidade

def recuar(posicao, quantidade):
    return posicao - quantidade

def jogar_novamente(posicao):
    dado = jogar_dado()
    print(f"Avante! Pule {dado} posições.")
    return posicao + dado

def cadeia(posicao):
    print("Cadeia! Fique uma rodada sem jogar.")
    return posicao

def pergunta(posicao):
    print('Pensa rapido! Para continuar responda corretamente:')
    resposta = input('Qual o menor país do mundo? Mônaco ou Vaticano? ')
    if resposta == 'Vaticano':
        print("Resposta correta! Continue.")
    else:
        print("Resposta incorreta! Volte para a posição inicial.")
        return 1

def recuar_dez(posicao):
    print("Mar de azar! Retroceda 10 posições.")
    return posicao - 10

def trocar_posicao(posicao):
    print("Troque de posição com outro jogador.")
    return random.randint(1, 63)

def duplicacao(posicao):
    dado = jogar_dado()
    print(f"Avance o dobro do valor que saiu no dado: {2 * dado} posições.")
    return posicao + 2 * dado

def jogar_jogo_da_gloria():
    N_jogadores = int(input('insira a quatidade de jogadores: '))
    while not 2 <= N_jogadores <= 4:
        N_jogadores = int(input('Quantidade inválida. Digite novamente: '))
    posicoes = [1] * N_jogadores
    turno = 0

    while max(posicoes) < 63:
        print(f"\nTurno do Jogador {turno + 1}")
        input("Pressione Enter para jogar o dado...")
        dado = jogar_dado()
        print(f'\nJogador {turno + 1} em posição {posicoes[turno]}')
        print(f"Jogador {turno + 1} jogou o dado e obteve: {dado}")

        if posicoes[turno] == 3 or posicoes[turno] == 57:
            posicoes[turno] = avancar(posicoes[turno], 3)
        elif posicoes[turno] == 11 or posicoes[turno] == 58:
            posicoes[turno] = recuar(posicoes[turno], 3)
        elif posicoes[turno] == 18:
            posicoes[turno] = jogar_novamente(posicoes[turno])
        elif posicoes[turno] == 22:
            posicoes[turno] = cadeia(posicoes[turno])
        elif posicoes[turno] == 32:
            posicoes[turno] = pergunta(posicoes[turno])
        elif posicoes[turno] == 37:
            posicoes[turno] = recuar_dez(posicoes[turno])
        elif posicoes[turno] == 46:
            posicoes[turno] = trocar_posicao(posicoes[turno])
        elif posicoes[turno] == 51:
            posicoes[turno] = duplicacao(posicoes[turno])
        else:
            posicoes[turno] = avancar(posicoes[turno], dado)

        turno = (turno + 1) % N_jogadores

    print(f"\nJogador {posicoes.index(max(posicoes)) + 1} venceu o Jogo da Glória!")
#jogar_jogo_da_gloria()
 
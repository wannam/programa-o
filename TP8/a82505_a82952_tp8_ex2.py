#a82505
#a82952
#tp8
#ex2

import json

def salvar_jogo(tabu, jogadores, simb):

    with open('jogo_salvo.txt', 'w') as save:
        json.dump({
            'tabu': tabu,
            'jogadores': jogadores,
            'simb': simb
        }, save)
        print('Jogo salvo com sucesso!')

def load_jogo():
    jogo = input('Deseja retomar o jogo anterior? (S/N) ').upper()
    print()
    if jogo == 'S':
            try: 
                with open('jogo_salvo.txt') as save:
                    dados = json.load(save)                   
                    resultado = None
                    simb = dados['simb']
                    tabu = dados['tabu']
                    jogadores = dados['jogadores']
                    print('O estado do jogo anterior foi carregado.')
                    jogo_do_galo(resultado, simb, tabu, jogadores)
            except FileNotFoundError:
                print('Não existem jogos salvos, começando um novo jogo.')
                iniciar_jogo(novo_jogo=True)
    else:
        iniciar_jogo(novo_jogo=True)


def iniciar_jogo(novo_jogo=False):
    if novo_jogo == True:
        resultado = None
        simb = 'X'
        tabu = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        jogadores = '1'
        jogo_do_galo(resultado, simb, tabu, jogadores)

def tabu_atual(tabu):
        for row in tabu:
            for i in range(len(row)):
                print(row[i], end='')
                if i != len(row) - 1:
                    print(' | ', end='')
            print('\n---------')
    

def jogo_do_galo(resultado, simb, tabu, jogadores):

    jogo = True

    while jogo:
        for row in tabu:
            for i in range(len(row)):
                print(row[i], end='')
                if i != len(row) - 1:
                    print(' | ', end='')
            print('\n---------')

        print(f"Jogador {jogadores}, é a sua vez:" , end=" ")
        jogada = (input())
        
        while jogada != '':
            print('\n____________________')
            print('Para salvar e sair, ')
            print('aperte ENTER')
            print('')
            break

        if jogada == '':
            print('\nConfira os dados do jogo atual:')
            tabu_atual(tabu)
            if jogadores == '1':
                jogadores = '2'
                simb = 'O'
            else:
                jogadores = '1'
                simb = 'X'
                print(f'jogador na vez: {jogadores}')  
            salvar = input('Salvar e sair? (S/N): ').upper()
            if salvar == 'S':
                salvar_jogo(tabu, jogadores, simb)
                break
            else: 
                continue

        if not 1 <= int(jogada) <= 9:
            print(f'Jogada inválida! Jogador {jogadores}, escolha outra posição: ')
            continue

        jogada = int(jogada)
        row = (jogada - 1) // 3
        col = (jogada - 1) % 3


        if tabu[row][col] in ['X', 'O']:
            print(f'Jogada inválida! Jogador {jogadores}, escolha outra posição:' )
            continue

        tabu[row][col] = simb

        for row in tabu:
            if row == [simb, simb, simb]:
                resultado = f'O Jogo terminou. O jogador {jogadores} venceu!'
                jogo = False 
        
        
        for i in range(3): 
            if all(tabu[j][i] == simb for j in range(3)):
                resultado = f"O Jogo terminou. O Jogador {jogadores} venceu!"
                jogo = False 
                

        if tabu[0][0] == tabu[1][1] == tabu[2][2] == simb or tabu[0][2] == tabu[1][1] == tabu[2][0] == simb:
            resultado = f"O Jogo terminou. O Jogador {jogadores} venceu!"
            jogo = False
        
        

        if all(cell in ["X", "O"] for row in tabu for cell in row):
            resultado = "Empate!"
            jogo = False 
        

        if jogo == False:
            for row in tabu:
                for i in range(len(row)):
                    print(row[i], end='')
                    if i != len(row) - 1:
                        print(' | ', end='')
                print('\n---------')
            print(resultado)

        if simb == 'X':
            simb = 'O'
            jogadores = '2'
        else:
            simb = 'X'
            jogadores = '1'

load_jogo()



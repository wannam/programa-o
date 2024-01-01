#a82505
#a82952
#tp4
#ex4


def jogar_jogo():
    tabu = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    jogo = True
    jogadores = '1'
    resultado = None
    simb = 'X'

    while jogo:
        for row in tabu:
            for i in range(len(row)):
                print(row[i], end='')
                if i != len(row) - 1:
                    print(' | ', end='')
            print('\n---------')
            
        

        print(f"Jogador {jogadores}, é a sua vez: ", end="")
        jogada = int(input())
        
        if not 1 <= int(jogada) <= 9:
            print(f'Jogada inválida! Jogador {jogadores}, escolha outra posição: ')
            continue

        jogada = int(jogada)
        row = (jogada - 1) // 3
        col = (jogada - 1) % 3

        if tabu[row][col] in ['X', 'O']:
            print(f'Jogada inválida! Jogador {jogadores}, escolha outra posição: ')
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

if __name__ == "__main__":
    jogar_jogo()

        






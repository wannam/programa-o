#a82505
#a82952
#tp8
#ex1


tabu = [[' - ' for _ in range(7)] for _ in range(7)]
jogo = True
jogadores = '1'
resultado = None
simb = ' X '


def jogar_jogo(): 
    tabu = [[' - ' for _ in range(7)] for _ in range(7)]
    jogo = True
    jogadores = '1'
    resultado = None
    simb = ' X '
    while jogo:
        for linha in tabu:
            print(' | '.join(linha))
            print()


        jogada = print(f"Jogador {jogadores}, é a sua vez: ", end="") 
        jogada = int(input())

        if not 1 <= jogada <= 7:
            print(f'Jogada inválida! Jogador {jogadores}, escolha outra posição: ')
            continue

            
        jogada = jogada - 1

        for i in range(6, -1 ,-1):
            if tabu[i][jogada] == ' - ':
                tabu[i][jogada] = simb
                break
        else:
            print(f'Jogada inválida! Jogador {jogadores}, escolha outra posição: ')
            continue


        for linha in tabu:
            if  ''.join(linha).count(simb * 4) > 0:
                resultado = f'O Jogo terminou. O jogador {jogadores} venceu!'
                jogo = False

        else:
            for i in range(7):
                if  ''.join(tabu[j][i] for j in range(7)).count(simb *4) > 0:
                    resultado = f'O Jogo terminou. O jogador {jogadores} venceu!'
                    jogo = False
            
            else:
                for i in range(4):
                    for j in range(4):
                        if ''.join(tabu[i + k][j + k] for k in range(4)).count(simb * 4) > 0:
                            resultado = f'O Jogo terminou. O jogador {jogadores} venceu!'
                            jogo = False
                        if ''.join(tabu[i + k][j + 3 - k] for k in range(4)).count(simb * 4) > 0:
                            resultado = f'O Jogo terminou. O jogador {jogadores} venceu!'
                            jogo = False

        
        if all(cell in ["X", "O"] for linha in tabu for cell in linha):
            resultado = "Empate!"
            jogo = False 


        if jogo == False:
                for linha in tabu:
                    print(' | '.join(linha))
                    print()
                print(resultado)

    

        if simb == ' X ':
            simb = ' O '
            jogadores = '2'
        else:
            simb = ' X '
            jogadores = '1'

if __name__ == "__main__":
    jogar_jogo()

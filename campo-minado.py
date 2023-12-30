
import random

def tabu_jogo(linhas, colunas):
    tabu = [[' ' for _ in range(linhas)] for _ in range(colunas)]
    return tabu


def niveis_tabuleiro(nivel, tabu, revelar_minas=False):
    if nivel == 1:
        print('    0 1 2 3 4 5 6 7')
        print('  -----------------')
    elif nivel == 2:
        print('    0 1 2 3 4 5 6')
        print('  ---------------')
    elif nivel == 3:
        print('    0 1 2 3 4 5')
        print('  -------------')
    for i in range(len(tabu)):
        print(f'{i} |', end=' ')
        for j in range(len(tabu)-1):
            if tabu[i][j] == 'X' and not revelar_minas:
                print(' ', end=' ')
            else:
                print(tabu[i][j], end=' ')
        print()

def local_minas(tabu, minas, linhas, colunas):
    for _ in range(minas):
        linha = random.randint(0, (linhas-1))
        coluna = random.randint(0, (colunas-1))
        while tabu[linha][coluna] == 'X':
            linha = random.randint(0, (linhas-1))
            coluna = random.randint(0, (colunas-1))
        tabu[linha][coluna] = 'X'

def valor_minas_vizinhas(tabu, linha, coluna, linhas, colunas):
    minas_vizinhas = 0
    for i in range(max(0, linha - 1), min(linhas, linha + 2)):
        for j in range(max(0, coluna - 1), min(colunas, coluna + 2)):
            if tabu[i][j] == 'X':
                minas_vizinhas += 1
    return minas_vizinhas


def liberar_celula(tabu, linha, coluna, tabu_revelado, linhas, colunas):
    if tabu[linha][coluna] == 'X':
        print('Você perdeu! Uma mina foi detonada.')
        return True
    elif tabu_revelado[linha][coluna] > 0:
        print('Esta célula já foi revelada. Escolha outra.')
    else:
        minas_vizinhas = valor_minas_vizinhas(tabu, linha, coluna, linhas, colunas)
        tabu_revelado[linha][coluna] = True
        tabu[linha][coluna] = str(minas_vizinhas) if minas_vizinhas > 0 else ' '
        if minas_vizinhas == 0:
            for i in range(max(0, linha - 1), min(linhas, linha + 2)):
                for j in range(max(0, coluna - 1), min(colunas, coluna + 2)):
                    liberar_celula(tabu, i, j, tabu_revelado, linhas, colunas)
    return False

def revela_bombas(tabu, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            if tabu[i][j] == 'X':
                tabu[i][j] = '*'
    print(tabu)


def jogo():

    print('1 - Fácil')
    print('2 - Médio')
    print('3 - Difícil')
    nivel = int(input('Escolha uma dificuldade: '))
    colunas = 0
    linhas = 0
    minas = 0

    while 1 >= nivel >= 3:
        nivel = int(input('Opção inválida, tente novamente: '))
        continue
    if nivel == 1:
        colunas = 8
        linhas = 8
        minas = 3
        tabu = tabu_jogo(linhas, colunas)
    if nivel == 2:
        colunas = 7
        linhas = 7
        minas = 5
        tabu = tabu_jogo(linhas, colunas)
    if nivel == 3:
        colunas = 6
        linhas = 6
        minas = 8
        tabu= tabu_jogo(linhas, colunas)

    tabu_revelado = [[False for _ in range(linhas)] for _ in range(colunas)]
    local_minas(tabu, minas, linhas, colunas)

    final_de_jogo = False

    while not final_de_jogo:

        niveis_tabuleiro(nivel, tabu)
        
        try:
            linha = int(input('Digite o número da linha: '))
            coluna = int(input("Digite o número da coluna: "))
        except ValueError:
            print('Entrada inválida. Digite números inteiros.')
            continue

        if 0 <= linha < linhas and 0 <= coluna < colunas:
            final_de_jogo = liberar_celula(tabu, linha, coluna, tabu_revelado, linhas, colunas)
            if not final_de_jogo:
                todas_reveladas = all(all(revelado or valor == 'X' for revelado, valor in zip(linha_revelado, linha_tabuleiro))
                                      for linha_revelado, linha_tabuleiro in zip(tabu_revelado, tabu))
                if todas_reveladas:
                    print('Parabéns! Você venceu!')
            elif final_de_jogo:
                revela_bombas(tabu, linhas, colunas)
        else:
            print('Posição inválida. Tente novamente.')

if __name__ == "__main__":
    jogo()


    
   






        



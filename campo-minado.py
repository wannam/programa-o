
import random

def tabuleiro(linhas, colunas, minas):
    tabu = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    local_minas(tabu, minas)
    valor_dicas(tabu)
    return tabu


def niveis_tabuleiro(nivel, tabu, revelar_minas=False):
    if nivel == 1:
        print("  | 0 1 2 3 4 5 6 7")
        print("--+----------------")
    elif nivel == 2:
        print("  | 0 1 2 3 4 5 6")
        print("--+--------------")
    elif nivel == 3:
        print("  | 0 1 2 3 4 5")
        print("--+------------")

        for i, linha in enumerate(tabu):
            print(f"{i} | {' '.join(str(celula) if celula != 'X' or revelar_minas else ' ' for celula in linha)}")

def local_minas(tabu, minas):
    minas_adicionadas = 0
    while minas_adicionadas < minas:
        linha = random.randint(0, len(tabu) - 1)
        coluna = random.randint(0 , len(tabu[0])- 1)
        if tabu[linha][coluna] != 'X':
            tabu[linha][coluna] = 'X'
            minas_adicionadas += 1

def valor_dicas(tabu):
    for i in range(len(tabu)):
        for j in range(len(tabu[0])):
            if tabu[i][j] != 'X':
                count_minas_vizinhas = valor_minas_vizinhas(tabu, i, j)
            tabu[i][j] = str(count_minas_vizinhas) if count_minas_vizinhas > 0 else ' '

def valor_minas_vizinhas(tabu, linha, coluna):
    valor = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if 0 <= linha + i < len(tabu) and 0 <= coluna + j < len(tabu[0]) and tabu[linha + i][coluna + j] == 'X':
                valor += 1
    return valor


def liberar_celula(tabu, linha, coluna, tabu_atual):
    if tabu_atual[linha][coluna] == ' ':
        tabu_atual[linha][coluna] == tabu[linha][coluna]
        if tabu[linha][coluna] == ' ':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= linha + i < len(tabu) and 0 <= coluna + j < len(tabu[0]):
                        liberar_celula(tabu, linha + i, coluna + j, tabu_atual)


def jogo():

    print('1 - Fácil')
    print('2 - Médio')
    print('3 - Difícil')

    nivel = int(input('Escolha a dificuldade: '))

    for nivel in range(0, 4):
        if 1 >= nivel >= 3:
            nivel = int(input('Opção inválida, tente novamente: '))
        if nivel == 1:
            linhas = 8
            colunas = 8
            minas = 3
        elif nivel == 2:
            linhas = 7
            colunas = 7
            minas = 5
        elif nivel == 3:
            linhas = 6
            colunas = 6
            minas = 8

    tabu = tabuleiro(linhas, colunas, minas)
    tabu_atual = [[' ' for _ in range(colunas)] for _ in range(linhas)]


    while True:
        
        niveis_tabuleiro(tabu_atual)

        try:
            linha = int(input('Digite o número da linha: '))
            coluna = int(input("Digite o número da coluna: "))
        except ValueError:
            print('Entrada inválida. Digite números inteiros.')
            continue

        if not (0 <= linha < linhas) or not (0 <= coluna < colunas):
            print('Posição inválida. Tente novamente.')
            continue

        if tabu[linha][coluna] == 'X':
            print('GAME OVER')
            niveis_tabuleiro(tabu, revelar_minas=True)
            break
        else:
            liberar_celula(tabu, linha, coluna, tabu_atual)

        liberar_celula = sum(row.count(' ') for row in tabu_atual)
        if liberar_celula == linhas * colunas - minas:
            print('Parabéns, você ganhou!')
            niveis_tabuleiro(tabu, revelar_minas=True)
            break

if __name__ == "__main__":
    jogo()


    
   






        



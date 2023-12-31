#a82505
#a82952
#tp7

import random

def carregar_palavras():
    with open('c:/Users//wanna/OneDrive/Área de Trabalho/UALG_LESTI 23-24/PROGRAMAÇÃO/TP7/a82505_a82952_tp7_jogo_da_forca/palavras.txt', 'r') as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip() for palavra in palavras]

def escolher_palavra():
    palavras = carregar_palavras()
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_adivinhadas):
    resultado = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

def mostrar_forca(tentativas_restantes):
    boneco = [("   |=====\n   |   \n   |\n   |\n   |\n ====="), ("   |=====\n   |   O\n   |\n   |\n   |\n ====="), ("   |=====\n   |   O\n   |   |\n   |   |\n   |\n ====="), ("   |=====\n   |   O\n   |  \|\n   |   |\n   |\n ====="), ("   |=====\n   |   O\n   |  \|/\n   |   |\n   |\n ====="), ("   |=====\n   |   O\n   |  \|/\n   |   |\n   |  /\n ====="), ("   |=====\n   |   O\n   |  \|/\n   |   |\n   |  / \ \n =====")]
    if tentativas_restantes == 6:
        forca = boneco[0]
    elif tentativas_restantes == 5:
        forca = boneco[1]
    elif tentativas_restantes == 4:
        forca = boneco[2]
    elif tentativas_restantes == 3:
        forca = boneco[3]
    elif tentativas_restantes == 2:
        forca = boneco[4]
    elif tentativas_restantes == 1:
        forca = boneco[5]
    elif tentativas_restantes == 0:
        forca = boneco[6]
    return forca

def jogar_jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    letras_erradas = []
    tentativas_restantes = 6

    print("JOGO DA FORCA\n")
    print(f"A palavra tem {len(exibir_palavra_oculta(palavra_secreta, letras_adivinhadas))} letras")
    print(exibir_palavra_oculta(palavra_secreta, letras_adivinhadas))
    print(" ")
    print("   |=====\n   |   \n   |\n   |\n   |\n =====\n")

    while tentativas_restantes > 0:
        letra = input("Adivinhe a letra: ").lower()

        if letra in letras_adivinhadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente novamente.")
        elif letra in palavra_secreta:
            letras_adivinhadas.append(letra)
            print(f"A letra {letra.upper()} existe na palavra.")
        else:
            tentativas_restantes -= 1
            letras_erradas.append(letra)
            print(f"A letra {letra.upper()} não existe na palavra. Tentativas restantes: {tentativas_restantes}")

        print(exibir_palavra_oculta(palavra_secreta, letras_adivinhadas))
        print(" ")
        print(f'Letras erradas: {letras_erradas}')
        print(" ")
        print(mostrar_forca(tentativas_restantes))

        if '_' not in exibir_palavra_oculta(palavra_secreta, letras_adivinhadas):
            print("Parabéns! Você ganhou!")
            break

    if '_' in exibir_palavra_oculta(palavra_secreta, letras_adivinhadas):
        print("GAME OVER. A palavra era:", palavra_secreta)
        
#jogar_jogo_da_forca()
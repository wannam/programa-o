#a82505
#a82952
#tp8
#ex1

from jogo_do_galo import jogar_jogo as jogo_galo
from quatro_linha import jogar_jogo as jogo_quatro_linha
from jogo_da_gloria import jogar_jogo as jogo_da_gloria
from jogo_da_forca import jogar_jogo as jogo_da_forca
from campo_minado import jogar_jogo as jogo_campo_minado

def menu():
    print("Opções:")
    print("A - Jogo do galo")
    print("B - Jogo 4 em linha")
    print("C - Jogo da glória")
    print("D - Jogo da forca")
    print("E - Jogo do campo de minas")

def selecionar_jogo(escolha):

    if escolha == 'A':
            print('Escolheu o jogo do galo. Vamos começar.')
            jogo = jogo_galo
    elif escolha == 'B':
            print('Escolheu o jogo 4 em linha. Vamos começar.')
            jogo = jogo_quatro_linha
    elif escolha == 'C':
            print('Escolheu o jogo da gloria. Vamos começar.')
            jogo = jogo_da_gloria
    elif escolha == 'D':
            print('Escolheu o Jogo da forca. Vamos começar.')
            jogo = jogo_da_forca
    elif escolha == 'E':
            print('Escolheu o Jogo do campo de minas. Vamos começar.')
            jogo = jogo_campo_minado
    
    return jogo

if __name__ == "__main__":
    while True:
        menu()
        escolha = input("Que jogo deseja jogar? ").upper()

        jogo_selecionado = selecionar_jogo(escolha)

        if jogo_selecionado:
            jogo_selecionado()
        else:
            print("Opção inválida. Tente novamente.")

menu()

           
    



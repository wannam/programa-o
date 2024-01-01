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

def selecionar_jogo(opcao):
    jogos = {
        'A': jogo_galo,
        'B': jogo_quatro_linha,
        'C': jogo_da_gloria,
        'D': jogo_da_forca,
        'E': jogo_campo_minado
    }
    
    return jogos.get(opcao, None)

if __name__ == "__main__":
    while True:
        menu()
        escolha = input("Que jogo deseja jogar? ").upper()

        jogo_selecionado = selecionar_jogo(escolha)

        if jogo_selecionado:
            print(f"Escolheu o jogo {escolha}. Vamos começar.")
            jogo_selecionado()
        else:
            print("Opção inválida. Tente novamente.")

menu()

           
    



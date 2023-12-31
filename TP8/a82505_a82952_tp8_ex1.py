#a82505
#a82952
#tp8
#ex1

import quatro_linha as quatro_linha
import jogo_da_gloria as jogo_da_gloria
import jogo_da_forca as jogo_da_forca
import campo_minado as campo_minado
import jogo_do_galo as jogo_do_galo

escolha = ' '

while True:
    print('opções:')
    print('A - jogo do galo')
    print('B - jogo 4 em linha')
    print('C - jogo da gloria')
    print('D - Jogo da forca')
    print('E - Jogo do campo de minas')
    escolha = input('Que jogo deseja jogar? ').upper()


    if escolha == 'A':
            print('Escolheu o jogo do galo. Vamos começar.')
            jogo_do_galo.jogar_jogo_do_galo()
    elif escolha == 'B':
            print('Escolheu o jogo 4 em linha. Vamos começar.')
            quatro_linha.jogar_quatro_linha()
    elif escolha == 'C':
            print('Escolheu o jogo da gloria. Vamos começar.')
            jogo_da_gloria.jogar_jogo_da_gloria()
    elif escolha == 'D':
           print('Escolheu o jogo da forca. Vamos começar.')
           jogo_da_forca.jogar_jogo_da_forca()
    elif escolha == 'E':
           print('Escolheu o jogo do campo de minas. Vamos começar.')
           campo_minado.jogar_campo_minado()
           
           
    



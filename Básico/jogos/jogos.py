import forca
import adivinhacao


def escolhe_jogo():
    print('****************************')
    print('**** Escolha o seu jogo ****')
    print('****************************')

    print('(1) Forca (2) Adivinhação')

    escolha_jogo = int(input())

    if escolha_jogo == 1:
        print('Você escolheu forca')
        forca.jogar()
    elif escolha_jogo == 2:
        print('Você escolheu adivinhação.')
        adivinhacao.jogar()


if __name__ == '__main__':
    escolhe_jogo()

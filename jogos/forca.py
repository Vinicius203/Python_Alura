import random


def jogar():
    print('**************************')
    print('Bem vindo ao jogo de Forca')
    print('**************************')

    palavra_secreta = selecionar_palavra()

    letras_acertadas = ['_' for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    qtd_erros = 0

    while not enforcou and not acertou:
        chute = chute_letra()

        if chute in palavra_secreta:
            armazena_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            qtd_erros += 1
            desenha_forca(qtd_erros)

        enforcou = qtd_erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

        if acertou:
            mensagem_vencedora()
        elif enforcou:
            mensagem_perdedora(palavra_secreta)


def selecionar_palavra():
    arquivo = open('jogos/palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    pos = random.randrange(0, len(palavras))
    palavra_secreta = palavras[pos].lower()

    return palavra_secreta


def chute_letra():
    chute = input('Entre com uma letra: ')
    chute = chute.lower().strip()
    return chute


def armazena_chute_correto(chute, letras_acertadas, palavra_secreta):
    for i, letra in enumerate(palavra_secreta):
        if letra == chute:
            letras_acertadas[i] = chute


def mensagem_vencedora():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedora(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print(f"A palavra secreta era: '{palavra_secreta}'.")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    jogar()

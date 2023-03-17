import random

# dia = 10
# mes = 4
# print(f'{dia:02d}/{mes:02d}') -> 10/04 (output)


def jogar():
    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')

    numero_secreto = random.randint(1, 100)
    print(numero_secreto)

    print('Em qual nível de dificuldade você quer jogar?')
    print('(1) Fácil (2) Médio (3) Difícil')
    pontos = 1000

    nivel = int(input())

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}:')

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print(f'Você digitou o número: {chute}')

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = not maior

        if acertou:
            print(
                f'PARABÉNS! Você acertou! A sua pontuação foi de {pontos} pontos.')
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior que o número secreto!')
            elif menor:
                print('Você errou! O seu chute foi menor que o número secreto!')

            pontos = pontos - abs(chute - numero_secreto)

    print('Fim de jogo!')
    if tentativas == rodada:
        print(
            f'O número secreto era {numero_secreto}, você fez {pontos} pontos.')

if __name__ == '__main__':
    jogar()
    
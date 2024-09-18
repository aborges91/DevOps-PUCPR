import random

def jogo_adivinhar_numero():
    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    print("Estou pensando em um número entre 1 e 100.")

    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    while tentativas < max_tentativas:
        try:
            # Solicita um palpite ao usuário
            palpite = int(input("Qual é o seu palpite? "))
            tentativas += 1

            if palpite < numero_secreto:
                print("O número é maior do que isso.")
            elif palpite > numero_secreto:
                print("O número é menor do que isso.")
            else:
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

    if palpite != numero_secreto:
        print(f"Você perdeu! O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhar_numero()

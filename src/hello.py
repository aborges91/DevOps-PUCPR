import random

def gerar_numero_secreto():
    return random.randint(1, 100)

def verificar_palpite(numero_secreto, palpite):
    if palpite < numero_secreto:
        return "maior"
    elif palpite > numero_secreto:
        return "menor"
    else:
        return "certo"

def jogo_adivinhar_numero(tentativas_max=10):
    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    print("Estou pensando em um número entre 1 e 100.")

    numero_secreto = gerar_numero_secreto()
    tentativas = 0

    while tentativas < tentativas_max:
        try:
            palpite = int(input("Qual é o seu palpite? "))
            tentativas += 1
            resultado = verificar_palpite(numero_secreto, palpite)

            if resultado == "maior":
                print("O número é maior do que isso.")
            elif resultado == "menor":
                print("O número é menor do que isso.")
            else:
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
                return True
        except ValueError:
            print("Por favor, insira um número válido.")

    print(f"Você perdeu! O número secreto era {numero_secreto}.")
    return False

if __name__ == "__main__":
    jogo_adivinhar_numero()

import random
import random as rd

def jogar_adivinhacao():

    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    #variavéis
    numero_secreto = random.randrange(1,101) #Gerando o número aleatorio
    total_de_tentativas = 0
    pontos = 1000

    #definindo nível de dificuldade
    while True:
        try:
            print("Qual nível de dificuldade?")
            print("(1) Fácil (2) Médio (3) Difícil")
            nivel = int(input("Define o nível: "))
            if (nivel < 1 or nivel > 3):
                raise #gera um erro se o 'nivel' for menor 1 ou maior que 3
            break
        except:
            print("Opção invalida, digite apenas numerais entre 1 e 3")

    #Lógica para cada nível
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    #iniciando laço de repetição
    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    #Entrada de dados / Convertendo para Int
        while True:
            try:
                chute = int(input("Digite um número entre 1 e 100: "))
                print("Você digitou", chute)

                break
            except ValueError as err:
                print("Opção invalida, digite apenas numerais entre 1 e 100 ")

    #Validando os dados inseridos
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue #continuar o laço

    #Condições
        acertou = chute == numero_secreto #Primeira condição
        chute_maior = chute > numero_secreto #Segunda condição
        chute_menor = chute < numero_secreto #Terceira condição

    #Iniciando a lógica
        if(acertou):
            print("**********************************")
            print("Você acertou e fez {} pontos".format(pontos))
            print("**********************************")
            break #Encerrando o laço
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior do que o número secreto")
            elif(chute_menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute) #Calculando a pontuação
                pontos = pontos - pontos_perdidos #associando a pontuação


    print("********************************")
    print("Fim do jogo")
    print("********************************")

if (__name__ == "__main__"):
    jogar_adivinhacao ()

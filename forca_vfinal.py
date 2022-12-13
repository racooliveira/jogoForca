import random

def jogar_forca():  # Criando a função

    mensagem_inicial()
    palavra_secreta = carregando_palavra_secreta()

    letras_acertadas = inicializando_letras_acertadas(palavra_secreta)

    nome = dados_do_player()
    print("Olá {}, vamos começar o jogo. A palavra contem {} letras, boa sorte.\n".format(nome, len(letras_acertadas)))

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = entrada_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


###Funções####

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")


    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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



def imprime_mensagem_perdedor(palavra_secreta):
    print("Poxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta.capitalize()))
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


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def entrada_chute():
    chute = input("Digite uma letra:\n ")
    chute = chute.strip().upper()

    letras_chutadas = []
    letras_chutadas.append(chute)
    return chute

def armazena_letras_chutada(chute):
    letras_chutadas = []
    for i in chute:
        letras_chutadas.append(i)
    return letras_chutadas

def inicializando_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def carregando_palavra_secreta():

    with open("palavras.txt", "r") as arquivo:
        arquivo = open("palavras.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta


def dados_do_player():
    nome = input("Para continuar, informe o seu nome:\n ")
    nome = nome.strip().capitalize()
    return nome


def mensagem_inicial():
    print(30 * "*")
    print("Bem vindo ao jogo de forca!")
    print(30 * "*")

if (__name__ == "__main__"):
    jogar_forca()



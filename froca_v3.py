import random



def jogar_forca():  # Criando a função

    mensagem_inicial()
    palavra_secreta = nivel_dificuldade()

    letras_acertadas = inicializando_letras_acertadas(palavra_secreta)

    nome = dados_do_player()
    #print("Olá {}, vamos começar o jogo. A palavra contem {} letras, boa sorte.\n".format(nome, len(letras_acertadas)))
    print("Definia o nível de dificuldade\n")
    print("1 (fácil) - Frutas | 2 (médio) - Animais | 3 - Profissões\n")
    nivel = int(input("Digite o nível escolhido: \n"))

    #dificuldade = nivel_dificuldade()

    enforcou = False
    acertou = False
    erros = 0

    print("Olá {}, vamos começar o jogo. O tema é {} e a palavra contem {} letras, boa sorte.\n".format(nome, nivel, len(letras_acertadas)))


    while(not enforcou and not acertou):

        print(palavra_secreta)

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



'''def carregando_palavra_secreta():

    with open("palavras.txt", "r") as arquivo:
        arquivo = open("palavras.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta'''

'''def dificuldade_media():

    with open("animais.txt", "r") as animais:
        animais = open("animais.txt", "r")
        palavras = []

        for linha in animais:
            linha = linha.strip()
            palavras.append(linha)

        animais.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta'''


def nivel_dificuldade():

    if (nivel == 1):
        with open("palavras.txt", "r") as frutas:
            frutas = open("palavras.txt", "r")
            palavras = []

            for linha in frutas:
                linha = linha.strip()
                palavras.append(linha)

            frutas.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

    if (nivel == 2):
        with open("animais.txt", "r") as animais:
            animais = open("animais.txt", "r")
            palavras = []

            for linha in animais:
                linha = linha.strip()
                palavras.append(linha)

            animais.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta


    if (nivel == 3):
        with open("profissoes.txt", "r") as profissoes:
            profissoes = open("profissoes.txt", "r")
            palavras = []

            for linha_profissoes in profissoes:
                linha_profissoes = linha_profissoes.strip()
                palavras.append(linha_profissoes)

            profissoes.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta




'''def validando_nivel_do_jogo(nivel):
    if (nivel == 1):

        with open("palavras.txt", "r") as frutas:
            frutas = open("palavras.txt", "r")
            tipo_frutas = []

            for linha_frutas in frutas:
                linha_frutas = linha_frutas.strip()
                tipo_frutas.append(linha_frutas)

            frutas.close()

        numero = random.randrange(0, len(tipo_frutas))
        palavra_secreta = tipo_frutas[numero].upper()
        return palavra_secreta


    if (nivel == 2):
        with open("animais.txt", "r") as animais:
            animais = open("animais.txt", "r")
            tipo_animais = []

            for linha in animais:
                linha = linha.strip()
                tipo_animais.append(linha)

            animais.close()

        numero = random.randrange(0, len(tipo_animais))
        palavra_secreta = tipo_animais[numero].upper()
        return palavra_secreta

    if (nivel == 3):
        with open("profissoes.txt", "r") as profissoes:
            profissoes = open("profissoes.txt", "r")
            tipo_profissoes = []

            for linha_profissoes in profissoes:
                linha_profissoes = linha_profissoes.strip()
                tipo_profissoes.append(linha_profissoes)

            profissoes.close()

        numero = random.randrange(0, len(tipo_profissoes))
        palavra_secreta = tipo_profissoes[numero].upper()
        return palavra_secreta '''





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



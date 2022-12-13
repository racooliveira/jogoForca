
def jogar_forca(): #Criando a função
    print(30 * "*")
    print("Bem vindo ao jogo de forca!") #Tela inicial
    print(30 * "*")

    palavra_secreta = "banana".upper() #Definindo variáveis
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    erros = 0

    print ("A palavra tem {} letras".format(len(letras_acertadas)))

    while (not enforcou and not acertou): #Iniciando o laço

        chute = input("Qual a letra? ") #Entrada de dados
        chute = chute.strip().upper() #Limpando os espaços e transformando em maisculo

        if (chute in palavra_secreta): #validando a logica
            index = 0
            for letra in palavra_secreta: #Aplicando a condição
                if (chute.upper() == letra.upper()): #convertendo toda a entrada em maiscula e comparando a entrada
                    letras_acertadas[index] = letra
                    print("A letra {} está na posição {}".format(chute,[index]))
                index += 1
        else:
            erros += 1
            print("Não contem a letra {} na palavra, você usou {} de 6 tentativas".format(chute, erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if (acertou):
            print("Você acertou a palavra é {}, parabéns!! ".format(palavra_secreta))


    print(30 * "*")
    print("Fim do jogo")
    print(30 * "*")

if (__name__ == "__main__"):
    jogar_forca()
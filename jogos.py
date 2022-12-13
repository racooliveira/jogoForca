import forca
import adivinhacao


def escolhe_jogo():
    while True:
        print("********************************")
        print("Escolha o seu jogo**************")
        print("********************************")

        print("(1) Forca (2) Advinhação (3) Sair")

        jogo = int(input("Qual jogo? "))

        if(jogo == 1):
             print("Jogando Forca")
             forca.jogar_forca()
        elif(jogo == 2):
             print("Jogando Advinhação")
             adivinhacao.jogar_adivinhacao()
        elif(jogo == 3):
             break

if(__name__ == "__main__"):
    escolhe_jogo()
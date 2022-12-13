'''idade1 = 10
idade2 = int("20")
print(idade1 + idade2)'''
import math
import random

'''nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)'''

'''idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
criança = idade < 12
adolescente = idade > 12

if(maior_idade):
    print("Você é maior de idade")
else:
    if(criança):
        print("Criança")
    elif(adolescente):
        print("Adolescente")'''

'''usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")'''

'''dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))'''

'''for rodada in range(1,10):
    print(rodada)'''
'''for rodada in range (1,10,2):
    print(rodada)'''

'''contador = 1
for contador in range(1, 11,3):
    print(contador)'''

'''print("R$ {:7.1f}".format(1000.12))
print("R$ {:07.2f}".format(4.11))'''

#print("Olá Mundo ! \n")



'''a = input()
b = input()

X = a + b

print ("X = ",  X)'''

'''n = 3.14159
raio = 2.00
area = ((raio ** 2) * n)

print("A= {:.4f}".format(area))'''

'''A = 30
B = 10
soma = A + B

print(f"SOMA = {soma}")'''

'''A = int(3)
B = int(9)
PROD = A, B
PROD = math.prod(PROD)

print(f"PROD = {PROD}")'''

'''import random as rd

aleatorio = rd.random() * 100
numero_aleatorio = round(int(aleatorio))
print(numero_aleatorio)'''

'''pontos_perdidos = round(abs(21 - 32) / 3)
type(pontos_perdidos)
print("é, {}".format(pontos_perdidos))
#dividindo por três'''


'''frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual a fruta ')

if fruta_pedida in frutas:
     print('Sim, temos a fruta')
else:
    print('Não temos a fruta')

#pessoas_familia =['Raul', 'Zene', 'Rafael', 'Mari']'''
'''print(pessoas_familia)'''

'''cidades =[]

cidade = input("Digite o nome da primeira cidade")
cidades.append(cidade)

cidades.append(input("Digite o nome da segunda cidade"))
cidades.append(input("Digite o nome da terceira cidade"))


print(cidades)'''


'''def jogar_forca(): #Criando a função
    #Tela inicial
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")
#Definindo variáveis
    palavra_secreta = "banana"
    palavra_secreta = palavra_secreta.capitalize()
    enforcou = False
    acertou = False'''

'''precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]

print(max(precos))'''

'''funcionarios = ['Astrid','Flavia','Talia', ... ,'Mauricio', 'Waldemar', 'Marina']

print(len(funcionarios))'''

## Restante do código que gera a lista de colocação...

'''print(colocacao)
#Resultado: ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']

campeao = colocacao[1]

print(' O grande campeão do torneio é o time ' + campeao)
#Resultado:  O grande campeão do torneio é o time Bruxos como Ronaldinho'''


'''def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_", "_", "_", "_"]


    erros = 0
    print(len(palavra_secreta))
    print(letras_acertadas)

    while(True):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)


    if("_" not in letras_acertadas):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")'''

'''with open("palavras.txt", "r") as arquivo:
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        print(palavras)

        #return palava_secreta'''

#def nivel_de_dificuldade():
nivel = input("Defina o nível de dificuldade")
if (nivel == 1):
        arquivo = open("palavras.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()


        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        print(palavras)
        #return palavra_secreta

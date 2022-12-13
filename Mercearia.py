
frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']
print(frutas)
while True:
    fruta_pedida = str(input('Qual a fruta '))
    if all (c.isalpha() or c.isspace() for c in fruta_pedida):
        break
    else:
        print("Digite um nome valido")

    if fruta_pedida in frutas:
            print('Sim, temos a fruta')
    else:
            print('Não temos a fruta')


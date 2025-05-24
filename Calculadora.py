# Fazer esse código com 'eval()' pode ser uma boa ideia
print('Isso agora é uma calculadora\n')

# Vou ver opções melhores de 'menu' quando tiver tempo
i = '0'
while (i != 'S'):
    print('\n1:  Soma')
    print('2:  Multiplicação')
    print('3:  Divisão')
    print('4:  Potencia')
    print('S:  Sair')
    i = input('\nEscolha: ')

    # Cade o 'switch()' no python pô T_T

    # Soma um número negativo se quiser subtração =_=
    if (i == '1'):
        n1 = int(input('\nPrimeiro número: '))
        n2 = int(input('Segundo número: '))
        print(n1 + n2)
    elif (i == '2'):
        n1 = int(input('\nPrimeiro número: '))
        n2 = int(input('Segundo número: '))
        print(n1 * n2)

    # Coloquei a divisão pois, fazer por multiplicação seria chato
    elif (i == '3'):
        n1 = int(input('\nNumerador: '))
        n2 = int(input('Divisor: '))
        print(n1/n2)

    # Não é possivel elevar a fracionario com esse código
    elif (i == '4'):
        n1 = int(input('\nNúmero: '))
        n2 = int(input('Expoente: '))
        print(n1**n2)
    elif (i == 'S'):
        continue
    else:
        print('\nOperação não reconhecida, tente novamente')
        continue
# Declaração inicial do dicionário
Estudantes = {'Pedrinho':1, 'Lana': 3, 'Apaguei o código sem querer, já é minha segunda vez escrevendo isso': 9, 'Raiva':6}

# Função para atribuir novos alunos no dicionário
def at_ests(d):
    while(True):
        E = input('Digite o nome do estudante: ')
        N = int(input('Digite sua nota: '))
        d[E] = N
        F = input('Adicionar outro? (S/N)\n')
        if (F != 'S'):
            break

# Loop principal
while(True):
    y = input('Quer adicionar algum aluno? (S/N)\n')
    if (y == 'S'):
        at_ests(Estudantes)
    else:
        i = input('De qual estudante quer saber a nota?: ')
        print('A nota é: ', Estudantes[i])

    T = input('Continuar? (S/N)\n')
    if (T != 'S'):
        break
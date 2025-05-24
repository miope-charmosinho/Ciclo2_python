# Criar lista de 10 alunos em que o programa responda quem está em cada posição
# Usúario dá a posição, o programa responde com o nome

lista = ['MC Pipokinha', 'Marcassa', 'Sportacus', 'Sr Sirigueijo', 'Peron (A)', 'Lisa', 'Pato oniciente', 'Pista do tubarão (Hot whells)', 'Rato do bandeco', 'Tibas']

print('Nessa sala tem ', len(lista), ' alunos')
print('Digite a posição do aluno, ou "0" para fechar o programa')

while (1 == 1):     # Loop infinito que para só quando vê o 'break'
    print()
    i = int(input('Posição: '))
    if (i == 0):
        break
    elif (0 < i <= len(lista)):
        print('O aluno nessa posição é: ', lista[i-1])
    else:
        print('Não tem essa posição na nossa incrivel salinha')
# Não sei como melhorar o "if...else" dessa função. Tá muito fácil de dar erro
def receber_vetor():
    V = []
    print('\nDigite os valores do vetor\nQuando quiser parar, digite "s"\n')
    while(True):
        a = input()
        if (a == 's'):
            break
        else:
            V += [int(a)]       # Tudo que não é número e não é um 's' vai dar erro.
    return V

# Alterando diretamente o "Vetor" por causa do comportamento de objeto em listas
# Dava para simplesmente criar outra lista somando "V" caso eu não quise-se alterar o vetor original
def mult_esca(V):
    E = int(input('Por quanto quer multiplicar seu vetor?: '))
    for i in range(0,len(V)):
        V[i] = V[i] * E

Vetor = receber_vetor()
mult_esca(Vetor)
print(Vetor)


# O exercício pedia para multiplicar um vetor e um escalar
# Teóricamente, fazer V*x não tá errado `\(°~°)/´
print(Vetor*2)
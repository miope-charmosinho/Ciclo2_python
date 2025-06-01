#Vou reutilizar as duas primeiras funções do código "Op_Matriz.py" por que eu me sentiria idiota reescrevendo a exata mesma coisa

def rec_tamanho():
    t = int(input('Qual será o tamanho de sua matriz? \nEx: "2" = matriz de duas linhas e duas colunas colunas\n'))
    return t

def rec_matriz(T):
    m = []
    for i in range(0,T):
        print('Digite a linha ', i+1, ': ', sep='', end='')
        while(True):
            v = input()
            V = v.split()
            if len(V) != T:
                print('A matriz tem', T, 'colunas. \nDigite novamente')
            else:
                for j in range(0, T):
                    V[j] = int(V[j])
                m.append(V)
                break
    return m

def test_iden(m,t):
    for i in range(0,t):
        if (m[i][i] != 1):
                print('Não é uma matriz identidade')
                return False
        for j in range(0,t):
            if ((j != i) and (m[i][j] != 0)):
                print('Não é uma matriz identidade')
                return False
    print('É uma matriz identidade!')
    return True

tam = rec_tamanho()
M = rec_matriz(tam)
test_iden(M, tam)
    
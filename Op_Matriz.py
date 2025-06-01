def rec_tamanho():
    t = input('Qual será o tamanho de sua matriz? \nEx: "2 3" = matriz de duas linhas e três colunas\n')
    T = t.split()
    for a in range(0,len(T)):
        T[a] = int(T[a])
    return T

def rec_matriz(T):
    m = []
    for i in range(0,T[0]):
        print('Digite a linha ', i+1, ': ', sep='', end='')
        while(True):
            v = input()
            V = v.split()
            if len(V) != T[1]:
                print('A matriz tem', T[1], 'colunas. \nDigite novamente')
            else:
                for j in range(0, T[1]):
                    V[j] = int(V[j])
                m.append(V)
                break
    return m

def soma(m1,m2,T):
    s = []
    for i in range(0,T[0]):
        v = []
        for j in range(0,T[1]):
            v.append(m1[i][j] + m2[i][j])
        s.append(v)
    return s

def subtr(m1,m2,T):
    s = []
    for i in range(0,T[0]):
        v = []
        for j in range(0,T[1]):
            v.append(m1[i][j] - m2[i][j])
        s.append(v)
    return s

def produto(m1,m2,T):
    if(T[0] != T[1]):
        print('Essas matrizes não podem se multiplicar')
        return 'null'
    p = []
    for i in range(0,T[0]):
        v = []
        s = 0
        x = -i
        while(x < (T[0]-i)):
            for j in range(0,T[0]):
                s += m1[i][j] * m2[j][i+x]
            v.append(s)
            s = 0
            x = x + 1
        p.append(v)
    return p
                
tam = rec_tamanho()
Matriz1 = rec_matriz(tam)
print('\nAgora descreva a segunda matriz\n')
Matriz2 = rec_matriz(tam)
ad = soma(Matriz1,Matriz2,tam)
print(ad)
prod = produto(Matriz1,Matriz2,tam)
print(prod)

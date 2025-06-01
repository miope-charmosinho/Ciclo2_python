#De novo, vou reutilizar o código das outras questões de matriz

def rec_tamanho():
    t = int(input('Qual será o tamanho de sua matriz? \nEx: "2" = matriz de duas linhas e duas colunas colunas\n'))
    if(t > 3 or t < 1):
        print('Tente outro tamanho')
        rec_tamanho()
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

def d_pos(m,t):
    x = 0
    s = 0
    if(t == 2):
        return (m[0][0] * m[1][1])
    while(x < t):
        r = 1
        for i in range(0,t):
            if(i + x >= t):
                j = i - t
            else:
                j = i
            r = r * m[j][j + x]
        s += r
        x += 1
    return s



def d_neg(m,t):
    x = 0
    s = 0
    if(t == 2):
        return (m[0][1] * m[1][0])
    while(x < t):
        r = 1
        z = 0
        for i in range(t-1,0-1,-1):
            if(i - x < 0):
                j = i + t
            else:
                j = i
            r = r * m[z][j - x]
            z += 1
        s += r
        x += 1
    return s


def det(m,t):
    if(t == 1):
        return m[0][0]
    p = d_pos(m,t)
    n = d_neg(m,t)
    return p - n

# Matrizes teste
#a = det([[1,0,2],[3,5,7],[1,4,1]],3)
#b = det([[1,2],[3,4]],2)
#c = det([[100]],1)
#print(a,b,c)

tam = rec_tamanho()
M = rec_matriz(tam)
D = det(M, tam)
print(D)
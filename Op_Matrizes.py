def recb_V (N):
    if(N == 0):
        print('Digite seu vetor: ')
    else:
        print('Digite seu outro vetor: ')
    R = input()
    Vet = R.split()
    if ((N == 0) or (N == len(Vet))):
        return Vet
    elif (N != len(Vet)):
        print('Digite um vetor de tamanho igual ao anterior.')
        recb_V(N)

def size (Vet):
    return len(Vet)

def soma(v1,v2,N):
    res = []
    for i in range(0,N):
        res.append(int(v1[i]) + int(v2[i]))
    return res

#Vou fazer produto escalar.
# |V| * |V| * cos(x) <-- considerando vetores paralelos (x = 0)
def prod_esc(v1,v2,N):
    R1 = R2 = 0
    for i in range(0,N):
        R1 += int(V1[i])**2
        R2 += int(V2[i])**2
    Resultado = R1**(1/2) * R2**(1/2)
    return Resultado

V1 = recb_V(0)
tam = size(V1)
V2 = recb_V(tam)   

while(True):
    e = input('Você quer somar, ou fazer o produto entre os dois vetores? (soma/produto)')
    if (e == 'soma'):
        print(soma(V1,V2,tam))
        break
    elif(e == 'produto'):
        print(prod_esc(V1,V2,tam))
        break
    else:
        print('Tente novamente\n')


    


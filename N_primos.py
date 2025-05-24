Num = int(input('Digite seu número: '))

# Não peguei a ideia da dica
def N_primos(N):

    # Não existem negativos primos pois todos podem ser divididos por -1 além de 1
    if (N < 2):
        print('Não há números primos em seu número')
        return 0
    
    count = 0

    # Contagem de 2 até N, verificando cada número para saber se ele é divisivel por todos seus anteriores
    for i in range(2,N+1):
        for j in range(2,i):
            if (i%j == 0):
                break   # Encontrou divisivel --> O 'i' analisado nessa iteração não é primo
            elif (j == i-1) and (i%j != 0):
                count += 1

    # Já que ambos começam em 2, a lógica do sistema não considera 2 como primo
    # Por isso retorno count+1 e tiro todos os números com menos de um primo (-50 teria 1 primo se não fosse aquele 'if')
    return count + 1 
    
print(N_primos(Num))

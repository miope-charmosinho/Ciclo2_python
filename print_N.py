Num = int(input('Digite seu número: '))

# Caso o número seja negativo, a contagem precisa ser invertida
if(Num >= 0):
    for i in range(0, Num+1):
        print(i,end='  ')
else:
    for i in range(Num, 1):
        print(i,end='  ')

l1 = int(input('Digite o primeiro lado do triângulo: '))
l2 = int(input('Digite o segundo lado do triângulo: '))
l3 = int(input('Digite o terceiro lado do triângulo: '))

# Só é possivel formar triângulos se a soma de dois lados é sempre maior que o terceiro
if (l1 + l2 < l3) or (l1 + l3 < l2) or (l3 + l2 < l1):
    print("Isso... nem é triângulo mano -_-'")

elif (l1 == l2) and (l2 == l3):
    print('Todos os lados são iguais\nEste triângulo é equilatero')
elif (l1 == l2) or (l2 == l3):
    print('Apenas dois lados são iguais\nEste triângulo é isóceles')
else:
    print('Todos os lados são diferentes\nO triângulo é escaleno')

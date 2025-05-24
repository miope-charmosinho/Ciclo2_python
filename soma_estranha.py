# Tem que somar todos estes termos sem usar loops e funções como sum()
l = [1, 7, 14, 15, 19, 24, 32, 56]

# Resolução 1: Idade das pedras
lerdo = l[0] + l[1] + l[2] + l[3] + l[4] + l[5] + l[6] + l[7]
print(lerdo)

# Resolução 2: O poder das 'strings'
string = str(l)
print(string)

st = string[1:29]
print(st)

termos = st.split(', ')
print(termos)

eq = ' + '.join(termos)
print(eq)

Resposta = eval(eq)
print(Resposta)

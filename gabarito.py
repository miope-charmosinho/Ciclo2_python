Gabarito = ['a','a','a','a','a','b','c','a','a','d']
Resposta = ['b','a','a','c','a','a','c','a','a','d']

def check_grade(G, R):
    grade = 0
    for i in range(0,len(G)):
        if (R[i] == G[i]):
            grade += 1
    return grade

print('A nota do aluno foi',check_grade(Gabarito,Resposta))

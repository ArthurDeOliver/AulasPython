#Letra a) PILHA DE PRATOS
pratos = [1,2,3,4,5,6,7,8,9,10]
n = len(pratos)-1

#lista vazia que será colocada os elementos da saída da pilha de pratos
saída = []

#ciclo while para colocar a lista saída como uma pilha de pratos
while(n >= 0):
    saída.append(pratos[n])
    n -= 1

print('''
lista dos pratos que chegaram: {}
lista dos pratos da saída: {}
'''.format(pratos,saída))

#letra b) FILA DE BANCO
fila_banco = [1,2,3,4,5,6,7,8,9,10]
saída_banco = []
n = 0

for n in range(len(fila_banco)):
    saída_banco.append(fila_banco[n])

print('''fila do banco: {}
saída da fila do banco: {}
'''.format(fila_banco,saída_banco))

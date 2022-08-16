'''
Gere uma lista de números, da qual não há elementos repetidos
'''

l = []

while True:
    entrada = int(input())
    l.append(entrada)

    if(entrada == 00):
        l.pop()
        break

#set é o método q descarta a repetição de termos em uma lista
print(set(l))
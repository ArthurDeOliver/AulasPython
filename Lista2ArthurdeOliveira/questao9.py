from operator import concat #biblioteca concat para concaternar 2 strings
import random as r #biblioteca random para gerar números aleatórios

lista_numeros = list(range(0,10)) #criação da lista com 10 valores de 1 à 9
#contador e acumulador de valores do ciclo
cont = 0
l = []

#ciclo while gerador de números aleatórios
while cont < 5 :
    r1 = r.randrange(0,10)# nesta parte do código há a geração de 2 números aleatórios esses números serão usados
    r2 = r.randrange(0,10)#para serem os índices da lista_numeros, dessa forma, há sempre números diferentes sendo 
    #gerador para entrar na lista acumuladora ' l '
    
    n1 = str(lista_numeros[r1]) #colocados como str para concatenar e criar uma dezena nova
    n2 = str(lista_numeros[r2])

    c = concat(n1,n2) #concatenação
    l.append(c) #atribuição a lista l
    cont += 1
    #caso a concatenação for o valor dito como 00 cont será o valor de -1 e tirará da lista l o valor 00 
    if(c == '00'):
        cont = 0 #cont = 0 resetando o valor de cont para obter mais outros valores de dezenas
        l.pop()

print('''
{}
'''.format(l))

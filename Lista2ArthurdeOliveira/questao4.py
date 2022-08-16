numeros = []
cont = 0

#ciclo de entrada dos números exatamente 10 valores 
while cont != 10:
    entrada = int(input())
    numeros.append(entrada)
    cont += 1

#organizando a lista numeros em ordem crescente
numeros.sort()
#transformando-a em uma tupla
numeros_tupla = tuple(numeros)
#contadores
contador_numero5 = 0
contador_par = 0
contador_impar = 0

#lista para as posições dos pares e ímpares
l_par = []
l_impar = []

#colocando elementos nulos em 10 posições nas listas de posições
for i in range(len(numeros)):
    l_par.append(0)
    l_impar.append(0)

#cliclo varrendo todos os números digitados em ordem averiguando onde ele se encaixa nas condições da questão
for i in range(len(numeros_tupla)):

    if(numeros_tupla[i] == 5):
        contador_impar += 1
        contador_numero5 += 1
    
    #colocando o números impar e par em suas posições na lista de posições
    if(numeros_tupla[i]%2 == 0):
        contador_par += 1
        l_par[i] = numeros_tupla[i]

    if(numeros_tupla[i]%2 != 0):
        contador_impar += 1
        l_impar[i] = numeros_tupla[i]

print('''
número de vezes que o número 5 aparece: {}
foram contados ao todo {} números pares e {} números ímpares
lista de números pares e suas posições {}
lista de números ímpares e suas posições {}
'''.format(contador_numero5,contador_par,contador_impar,l_par,l_impar))

#entrada da quantidade de números primos
quantidade_números_primos = int(input())

#criação da lista de 200 números
lista_numeros = list(range(1,200+1))

#lista resultante dos números primos
lista_num_primos = []

#contador e acumuladores
cont = 0
num = 0
l = []

#ciclo inicial, nele será depositado o valor respectivo do número de ciclo em num
for i in range(len(lista_numeros)):
    num = lista_numeros[i]

    #ciclo interno que irá percorrer o número num em todo a lista de 200 números, verificando se o resto da divisão por cada elemento
    #for 0, após isso, depositará em l
    for n in range(len(lista_numeros)):
        if(((num%lista_numeros[n]) == 0)):
            l.append(lista_numeros[n])

    #tamanho da lista l é 2? isso só é possível com números cujo resto da divisão foi por 1 e por ele mesmo, ou seja, é um número primo
    if((len(l) == 2)):
        #como 1 não é considerado primo, e em ordem a lista l será: l = [1, num_primo], será colocado apenas o índice 1 na lista resultante
        lista_num_primos.append(l[1])
        #contando quantas vezes o número primo entrou nesse if
        cont += 1

    #se esta quantidade igual ao número digitado inicialmente, todo o ciclo acaba
    if(cont == quantidade_números_primos):
        break
    
    #lista l zerada para ser usada mais uma vez com os próximos números
    l = []

print('''
lista de números primos:{}
'''.format(lista_num_primos,cont))
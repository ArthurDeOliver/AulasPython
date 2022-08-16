l1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
l2 = [0,0,0,0,1,8,2,2,2,10,12,53,7,4,12]


#listas ordenadas de forma crescente
l1.sort()
l2.sort()

nova_lista = []
cont = 0

for i in range(len(l1)):
    #condições entre as 2 listas: o elemento do índice do ciclo está em uma das listas? E esse elemento não se repete na própria lista?
    if((l2[i] in l1) and ((l2[i] is l2[i-1]) == False)):
        nova_lista.append(l2[i]) #com essas condições é possível aplicar na lista dos elementos intercalados
        cont += 1

print('''
quantidade de elementos da lista 1: {}
quantidade de elementos da lista 2: {}
quantidade de elementos da lista gerada com os elementos intercaladas entra a 1 e a 2: {}

lista com o elementos intercalados: {}
'''.format(len(l1),len(l2),len(nova_lista),nova_lista))


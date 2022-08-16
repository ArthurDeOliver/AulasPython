nomes = []
idades = []

#ciclo incrementando valores nas listas
while True:

    entrada_nome = input('digite o nome: ')
    entrada_idade = int(input('digite a idade: '))

    if(entrada_nome == 'encerrar' and entrada_idade == 0):
        break

    nomes.append(entrada_nome)
    idades.append(entrada_idade)

#concatenação das listas nomes e idades para criar um par chave-valor, ou seja, um dicionário
dicionário = dict(zip(nomes,idades))

idade_abaixo_30 = []
idade_acima_30 = []

#ciclo que percorrerá oa chaves do dicionário
for i in dicionário.keys():
    
    #condição que estabeleçe a diferença de idades percorrendo o dicionário
    if(dicionário[i] >= 30):
        idade_acima_30.append(i)
    else:
        idade_abaixo_30.append(i)

print('''
lista das pessoas com idade superior a 30: {}
lista das pessoas com idade inferior a 30: {}
'''.format(idade_acima_30,idade_abaixo_30))    
nomes_preços = ('chocolate','R$ 4,00','suco','R$ 1,50', 'maçã', 'R$ 0,40')

#código começa com o print do template do 
print('''
======================
  Produto   |  Preço
======================''')

#variáveis da qual será usadas no print para selecionar em ordem: nome / preço
i = 1
j = 0
cont = 0

while True:
    
    print(''' {}  |  {}'''.format(nomes_preços[j],nomes_preços[i]))

    i += 2
    j += 2
    cont += 1

    if(cont == (int(len(nomes_preços))/2)):
        break

print('''======================
''')

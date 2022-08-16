'''l = [1,2,3,4,5,6,7,8,9,10]

index = l.index(1,0,2)
#encontra o índice de um elemento na lista primeiro parâmetro o elemento que deseja encontrar
# os próximos 2 é o intervalo da busca através do índice

print(index)'''

produtos = {
    'chocolate': 4.50,
    'pão': 0.75,
    'refrigerante': 6 
}
print('-Esses são os nossos produtos ')
for i in produtos.keys():
    print(i)

while True:
    entrada = input('Qual o produto que deseja encontrar o preço? ')
    
    if(entrada == '00'):
        print('programa encerrado')
        break
    if(entrada in produtos.keys()):
        print('O produto {} tem o valor de R${}'.format(entrada, produtos[entrada]))
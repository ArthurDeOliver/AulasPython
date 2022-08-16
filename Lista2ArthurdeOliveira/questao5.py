carros = ['uno','onix','celta','x6','kwid','corolla','renegade','miller','compass','288gto']
consumo = [20,70,90,10,50,30,60,80,50,100]

for i in range(len(consumo)):

    cont = 0

    for n in range(len(consumo)):
        if(consumo[i] < consumo[n]):
            cont += 1

    if(cont == 0):
            resultado_economia = carros[i]

print('''
este é o modelo do carro mais econômico: {}
'''.format(resultado_economia))

#para X(km) = 2
for i in range(len(consumo)):
    print('''O modelo {} consome {:.2f} litros '''.format(carros[i],2/consumo[i]))

print('   ')
#consumo de gasolina 
for i in range(len(consumo)):
    print('''Para uma gasolina custando R$ 5,50 o modelo {} precisa gastar R${:.2f} '''.format(carros[i],(2/consumo[i])*5.5))
print('   ')
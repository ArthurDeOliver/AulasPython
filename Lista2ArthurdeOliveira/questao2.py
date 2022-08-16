#inputs dos valores como float
valor_casa = float(input('Qual o valor da casa que deseja comprar? '))
salário = float(input('Qual o seu salário? '))
anos_pagar = int(input('Quanto tempo, em anos, deseja-se pagar a casa? '))

#cálculo da prestação
prestação = float(valor_casa/(anos_pagar * 12))

#comparativo da prestação com 30% do salário
if(prestação < salário*0.3):
    print('Empréstimo aprovado!')
else: print('Empréstimo recusado')
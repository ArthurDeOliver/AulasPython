#tupla contendo as perguntas 
perguntas = (input("Telefonou para a vítima? "), input("Esteve no local do crime? "), input("Mora perto da vítima? "), input("Devia para a vítima? "), input("Já trabalhou com a vítima? "))
contador = 0

#ciclo que percorrerá a tupla buscando por respostas 'sim' ou 'não'
for i in range(len(perguntas)):
    if(perguntas[i] == 'sim'):
        contador += 1
    else:
        contador = contador

#mostragem do resultado frente a contagem do resultado obtido no ciclo acima
if(contador == 2):
    print("Você é SUSPEITO")
elif(contador == 3 or contador == 4):
    print("Você é CÚMPLICE")
elif(contador == 5):
    print("VOCÊ É O ASSASSINO!!!")
else:
    print('Você é INOCENTE')

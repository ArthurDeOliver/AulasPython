dicionário= {
    'chave1' : 'valor1',
    'chave2' : 'valor2',
    'chave3' : 'valor3'
}

#letra a)

lista_chaves = dicionário.keys()

#letra b)

lista_valores = dicionário.values()

#letra c)

converter_dicionaário_para_tupla = tuple(dicionário)

print(f'{lista_chaves} {lista_valores} {converter_dicionaário_para_tupla}')
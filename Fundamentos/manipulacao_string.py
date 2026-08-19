# MANIPULAÇÃO DE STRING

nome = 'João'

# Obs: O índice positivo começa sempre em zero o índice negativo começa sempre em -1. E o último índice é exclusivo, ou seja, (linha debaixo)
# se eu quiser pegar apenas o Jo da palavra João eu tenho que passar o range de 0:2 

print(nome[0]) # Acessando as partes da minha string pelo índice
print(nome[-1]) # Acessando o último caractere da minha string
print(nome[0:2]) # Acessando a minha string e pegando os valores da posição 0 até a posição 1 pois o último índice é exclusivo (0, 1)
print(nome[:3]) # Quando eu não passo nenhum parâmetro antes dos dois pontos ele pega desde o início da minha string
print(nome[2:]) # Quando eu não passo nenhum parâmetro depois dos dois pontos ele pega desde o final da minha string
print(nome[:]) # Quando eu não passo nenhum parâmetro nem antes e nem depois dos dois pontos, ele pega toda a string.
print(nome[:-1]) # Quando eu coloco o -1 depois do dois pontos eu falo que quero pegar toda a minha string exceto o último caractere dela
print(nome[0:4:2]) # Eu posso colocar mais um dois pontos e indicar os passos, ou seja, qual intervalo que eu quero pegar os caracteres
print(nome[::-1]) # Aqui eu estou invertendo a minha string, ou seja, pego ela toda e inverto colocando-a de traz para frente
print(len(nome)) # Aqui ele me retorna quantos caracteres tem a minha string e não quantos índices, pois o índice começa em zero e o len conta caractere então começa em 1
print(len(nome) - 1) # Aqui ele vai me retornar exatamente qual o meu último índice, pois eu uso o len -1 para compensar o índice que começa em 0


nome1 = """
João\nDoti\nMelo"""
print(nome1)

# Nesse acima eu fiz uma variável com string multilinha, posso usar essa multilinha para comentários também basta usar 3 aspas duplas antes e depois

nome2 = 'João'
nome3 = 'Melo'


# Aqui eu usei o recurso de Fstring para concatenar, basta colocar o F e as aspas e quando quiser usar a variável para concatenar eu só preciso colocar dentro de chaves
fullname = f"Meu nome é {nome2} e meu sobrenome é {nome3}"
print (fullname)

# Obs: Eu consigo usar multilinhas com fstring também

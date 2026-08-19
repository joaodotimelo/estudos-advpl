""""
🟢 FÁCIL — Exercício 6
Peça ao usuário o preço de um produto e um percentual de desconto (ambos números). 
Calcule e mostre o valor final com o desconto aplicado, usando f-string. 
Ex: preço 100, desconto 10 → "Valor final: 90.0".
"""

preco_produto = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o valor do desconto: '))

desconto_valor = (desconto / 100) * preco_produto

valor_final = preco_produto - desconto_valor
print(f"O valor final do seu produto já com o desconto aplicado é de R${valor_final}")



"""
🟡 MÉDIO — Exercício 7
Dada a variável cpf = "123.456.789-00", usando apenas slicing, separe e imprima em linhas diferentes:

Só os números antes do primeiro ponto ("123");
Só o número depois do traço ("00");
O CPF sem pontuação nenhuma (só os números, sem os pontos e o traço) — pode fazer com várias fatias concatenadas.
"""


cpf = "532.553.838-11"

print(cpf[0:3])

print(len(cpf) - 1) # Para descobrir quantos caracteres tem, tendo em vista que eu sei que eu preciso pegar apenas os últimos 2 sem ter que ficar contando manual
print(cpf[12:])

slice1 = cpf[0:3]
slice2 = cpf[4:7]
slice3 = cpf[8:11]
slice4 = cpf[12:]

slice_concatenado = slice1 + slice2 + slice3 + slice4
print(slice_concatenado)


"""
🔴 DIFÍCIL — Exercício 8
Peça ao usuário três números representando os lados de um triângulo (a, b, c). Verifique e informe:

Se eles formam um triângulo válido (regra: a soma de quaisquer dois lados deve ser maior que o terceiro lado —
precisa valer para as três combinações);
Se for válido, informe também se o triângulo é equilátero (todos os lados iguais), 
isósceles (exatamente dois lados iguais) ou escaleno (todos diferentes).

(Dica: você vai precisar combinar vários and/or com parênteses — 
pensa primeiro no papel/comentário quais são as condições antes de escrever o código, 
igual fizemos na correção do exercício 4.)"""

lado1 = int(input('Digite o lado do triângulo: '))
lado2 = int(input('Digite o lado do triângulo: '))
lado3 = int(input('Digite o lado do triângulo: '))


if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if (lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
        print('Seu triângulo é escaleno')
    elif (lado1 == lado2) and (lado1 == lado3):
        print('Seu triângulo é equilátero')
    else:
        print('Seu triângulo é Isósceles')
else:
    print('Esses lados não formam um triângulo válido')

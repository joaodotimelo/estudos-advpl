"""Exercício 1 — Tipos e conversão
   Peça ao usuário (via input()) para digitar dois números. Some os dois e mostre o resultado. 
   (Pense: input() sempre retorna que tipo? O que precisa acontecer antes da soma?)
"""

numero = int(input('Digite um número: '))
numero2 = int(input('Digite mais um número: '))
soma = f"A soma dos dois números é {numero + numero2}"
print(soma)



"""Exercício 2 — Operadores relacionais + lógicos
   Crie duas variáveis, idade e possui_cnh (bool). 
   Escreva uma condição que imprima "Pode dirigir" somente se a idade for maior ou igual a 18 e a pessoa possuir CNH.
"""

idade = int(input('Digite sua idade: '))
possui_cnh = True

if idade >= 18 and possui_cnh:
    print(f"A sua idade é {idade} e você pode dirigir")
else:
    print(f"A sua idade é {idade} e você não pode dirigir pois é menor de idade")


"""Exercício 3 — Aritmética (par/ímpar)
   Peça um número ao usuário e informe se ele é par ou ímpar. 
   (Dica: qual operador aritmético te dá o resto de uma divisão?)
"""

numerox = int(input('Digite um número: '))

if numerox % 2 == 0:
    print(f"O número {numerox} é par")
else:
    print(f"O número {numerox} é ímpar")


"""Exercício 4 — Slicing
   Dada a variável frase = "Auditoria de Sistemas", sem usar input, escreva código que imprima:

   só a palavra "Auditoria";
   só a palavra "Sistemas";
   a frase inteira invertida."""


frase = "Auditoria de Sistemas"

print(frase[0:9])
print(frase[13:21])
print(frase[::-1])



"""Exercício 5 — F-string + concatenação
   Peça ao usuário o nome e a idade (com o tipo certo). Monte e imprima uma frase usando f-string dizendo: 
   "Fulano tem X anos e daqui a 5 anos terá Y anos." (o Y precisa ser calculado, não digitado)."""


nome = (input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
idade_futura = idade + 5

print(f"O {nome} tem {idade} anos e daqui a 5 anos terá {idade_futura} anos.")

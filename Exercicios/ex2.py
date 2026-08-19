"""🟢 MUITO FÁCIL — Exercício 1
Peça a temperatura atual (número) ao usuário e informe se está "Calor" (acima de 30), 
"Ameno" (entre 15 e 30) ou "Frio" (abaixo de 15).
"""

temperatura_atual = int(input('Qual a temperatura atual?\n'))

if temperatura_atual > 30:
    print('Está calor')
elif temperatura_atual < 15:
    print('Está frio')
else:
    print('Está ameno')


"""🟢 FÁCIL — Exercício 2
Dada a variável email = "joao.silva@empresa.com.br", usando apenas slicing (sem nenhuma função pronta), 
extraia e imprima só a parte antes do @ (joao.silva). Dica: conte manualmente em qual índice o @ está.
"""

email = 'joao.silva@empresa.com.br'
print(email[:10])


"""🟡 INTERMEDIÁRIO — Exercício 3
Peça ao usuário dois números e um operador (como texto: "+", "-", "*" ou "/"). 
Com base no operador digitado, calcule e mostre o resultado correspondente usando if/elif/else. 
(Pense: o operador digitado vem em que tipo? Como comparar isso dentro do if?)
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
operador = input('Digite um operador para fazer a conta (+, -, *, /): ')

if operador == '+':
    resultado_final = num1 + num2
    print(resultado_final)
elif operador == '-':
    resultado_final = num1 - num2
    print(resultado_final)
elif operador == '*':
    resultado_final = num1 * num2
    print(resultado_final)
elif operador == '/':
    resultado_final = num1 / num2
    print(resultado_final)

"""🟠 DIFÍCIL — Exercício 4
Peça ao usuário: idade, se possui CNH (sim/não, como texto) e se está acompanhado por um adulto (sim/não).
As regras de acesso a um passeio são:
Maior de 18 e possui CNH → "Pode dirigir"
Menor de 18, mas está acompanhado → "Pode entrar, mas não dirigir"
Menor de 18 e não está acompanhado → "Acesso negado"

(Pense: como transformar a resposta "sim"/"não" digitada em algo que dê pra usar direto numa condição lógica?)
"""

idade = int(input('Digite sua idade: '))
possui_cnh = input('Você possui CNH? (Sim/Não)\n')
acompanhado_adulto = input('Você está acompanhado de algum adulto? (Sim/Não)\n')

if idade >= 18 and possui_cnh.lower() == 'sim':
    print('Pode dirigir')
elif idade < 18 and acompanhado_adulto.lower() == 'sim':
    print('Pode entrar, mas não dirigir')
else:
    print('Acesso negado')



"""🔴 MUITO DIFÍCIL — Exercício 5
Peça ao usuário uma frase qualquer (frase = input(...)). Sem usar nenhuma função pronta de contagem, 
usando apenas slicing e os operadores que já aprendeu, faça o programa informar:

O primeiro e o último caractere da frase;
Se a frase é um palíndromo (lê-se igual de trás para frente) — ex: "ovo", "arara". 
Dica: você já sabe inverter uma string com [::-1]; como comparar duas strings pra saber se são iguais?
A frase invertida, mas sem o primeiro e último caractere."""

frase = input('Digite uma frase qualquer: ')
frase_invertida = frase[::-1]

print(frase[0])
print(frase[-1])

frase_quebrada = frase[1:-1] # Remoção do primeiro e último caractere
print(frase_quebrada[::-1]) # Inversão da string já quebrada

if frase.lower() == frase_invertida.lower():
    print('Essa frase é um palíndromo, conseguimos ler ela igual de traz para frente')
else:
    print('Essa frase não é um palíndromo, pois não conseguimos ler ela de traz para frente igualmente')

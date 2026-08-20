# MÉTODOS DE STRING

texto = "Python"

print(texto.upper()) # Deixar todas as letras maiúsculas
texto_maiusculo = texto.upper() # Deixei tudo maiúsculo porém em uma variável
print(texto.lower()) # Deixar todas as letras minusculas
texto_minusculo = texto.lower() # Deixei tudo minusculo porém em uma variável

email = "joao@teste.com.br      "
print(email.strip()) # Remove os espaços do início e do fim
print(email.lstrip()) # Remove espaços a esquerda
print(email.rstrip()) # Remove os espaços a direita

# ex de uso: Quando for pedir o nome a um usuário

nome = input("Digite seu nome: ").strip()

texto2 = "Doti Melo"
print(texto2.replace("Doti", "João")) # Aqui eu troquei a palavra Doti por João

# OBS: A string é imutável, então se eu der um print texto2 abaixo ele vai retornar Doti Melo, para que me retorne João Melo eu preciso salvar o resultado em uma nova variável

texto3 = "Doti Melo Doti Doti"
print(texto3.replace("Doti", "João", 1)) # Aqui eu estou trocando somente a primeira palavra que aparece Doti, pois se eu tiver mais de uma palavra igual na frase e não passar o parâmetro de qualtidade ele altera todas que tiver no texto

print(texto3.find("i")) # Aqui ele me retorna o índice da primeira ocorrência que ele encontrar do parâmetro que eu passei. Caso ele não encontra nada ele retorna -1
print(texto3.find("i", 3, 10)) # Aqui eu pedi para ele me retornar o índice também, só que com um parâmetro adicional que é o intervalo que ele vai procurar que nesse caso é da posição 3 até a 10
print(texto3.find("i", 3)) # Aqui eu pedi para ele me retornar o índice também, só que com um parâmetro adicional que é o intervalo que ele vai procurar que no caso é a partir do índice 3 em diante

texto4 = "João Marcos Doti Melo"
print(texto4.count("o")) # Aqui ele retorna a quantidade de registros que ele encontrar do parâmetro que eu passei no count
print(texto.count("João")) # Aqui ele retorna a quantidade de registros que ele encontrar do parâmetro que eu passei no count


# MÉTODOS DE VALIDAÇÃO

print("123".isdigit()) # Valida se tem só números (True)
print("abc".isdigit()) # (False)
print("abc".isalpha()) # Valida se tem só letras (True)
print("abc123".isalpha()) # (False)
print("abc123".isalnum()) # Valida se tem letras e números (True)
print("abc 123".isalnum()) # (False porque tem o espaço)

# OBS: Ele não se importa com letras maiúsculas e minúscula

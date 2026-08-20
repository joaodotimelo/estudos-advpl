"""🟢 FÁCIL — Exercício 9
Peça ao usuário um e-mail (input). Usando .strip(), remova espaços acidentais no início/fim.
Depois, usando .lower(), garanta que fique tudo minúsculo. 
Por fim, use .find("@") para descobrir e imprimir o índice onde o @ está.
"""

email = input('Digite seu email: ').strip().lower()
print(email.find("@"))



"""🟡 MÉDIO — Exercício 10
Peça ao usuário para digitar um CPF (pode digitar com ou sem pontuação, ex: "123.456.789-00" ou "12345678900"). 
Usando .replace(), remova os pontos e o traço (se existirem), deixando só os números. 
Depois, use .isdigit() para validar se o resultado final contém apenas números — e informe se o CPF é válido
(só números, 11 dígitos) ou inválido.

(Dica: você vai precisar de mais de um .replace() encadeado, ou aplicado em sequência 
— pensa em como remover cada símbolo um de cada vez.)
"""

cpf_completo = input("Digite seu CPF: ")
cpf_limpo = cpf_completo.replace(".", "").replace("-", "")

if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')

"""
🔴 DIFÍCIL — Exercício 11
Peça ao usuário uma senha (input). Valide se ela atende a todas essas regras, 
usando os métodos e operadores que já aprendeu:

Tem pelo menos 8 caracteres (len());
Contém pelo menos 1 número (dica: percorra a string com um for e use .isdigit() em cada caractere — 
ou pense em outra forma sem loop, usando any() como desafio extra, se quiser pesquisar);
Não contém espaços (.find(" ") retorna -1 quando não encontra).

Informe se a senha é "Válida" ou, se inválida, qual regra especificamente não foi cumprida (pode ser mais de uma).

(Atenção: esse é o primeiro exercício que te exige combinar várias condições and com métodos de string 
dentro do próprio if — pensa com calma antes de codar, igual fizemos no do triângulo.)
"""

senha = input('Digite uma senha: ').strip().lower()

# Minimo 8 caracteres
tamanho_senha = len(senha)

# Checa se tem espaços
posicao_espaco = senha.find(" ")

# Checa se tem pelo menos 1 número
tem_numero = any(caractere.isdigit() for caractere in senha)

if tamanho_senha >= 8 and tem_numero and posicao_espaco == - 1:
    print('A sua senha é válida')
else:
    print('A sua senha é inválida')
    if tamanho_senha < 8:
        print('Sua senha deve ter no mínimo 8 caracteres.')
    if posicao_espaco != -1:
        print('Sua senha não pode ter espaços')
    if not tem_numero:
        print('Sua senha precisa ter pelo menos 1 número')

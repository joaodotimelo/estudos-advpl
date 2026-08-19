# Python — Manipulação de Strings

## Indexação

Cada caractere de uma string tem uma posição (índice).

- **Índice positivo** → começa em `0` (esquerda pra direita)
- **Índice negativo** → começa em `-1` (direita pra esquerda)

```python
nome = 'João'

print(nome[0])    # 'J'  → primeiro caractere
print(nome[-1])   # 'o'  → último caractere
```

---

## Slicing (fatiamento) — `string[inicio:fim]`

**Regra-chave: o índice final é EXCLUSIVO** — o fatiamento pega até a posição anterior ao número informado, nunca inclui o próprio número.

```python
nome = 'João'
#        J  o  ã  o
# índice 0  1  2  3

print(nome[0:2])   # 'Jo'   → pega índices 0 e 1 (o 2 fica de fora)
print(nome[:3])     # 'Joã'  → sem número antes dos ':' = começa do início
print(nome[2:])     # 'ão'   → sem número depois dos ':' = vai até o final
print(nome[:])      # 'João' → sem nada = string inteira
print(nome[:-1])    # 'Joã'  → toda a string, exceto o último caractere
```

### Terceiro parâmetro — passo (`string[inicio:fim:passo]`)

```python
print(nome[0:4:2])  # 'Jã'   → pega de 2 em 2 (índices 0 e 2)
print(nome[::-1])   # 'oãoJ' → passo -1 inverte a string inteira
```

---

## `len()`

Retorna a **quantidade de caracteres** da string (conta a partir de 1, diferente do índice que começa em 0).

```python
print(len(nome))        # 4  → João tem 4 caracteres
print(len(nome) - 1)    # 3  → índice do ÚLTIMO caractere (compensa o índice começar em 0)
```

---

## Strings multilinha

Usando três aspas (`'''` ou `"""`) antes e depois, a string pode ocupar várias linhas.

```python
nome1 = """
João\nDoti\nMelo"""
print(nome1)
```

Também é possível misturar quebras de linha reais (Enter dentro das aspas) com `\n` (quebra de linha "escrita").

**Observação:** uma string de três aspas "solta" (sem estar atribuída a nenhuma variável) é tecnicamente uma **docstring** — o Python a ignora por não ter efeito nenhum, então na prática funciona como um comentário de várias linhas. Mas não é um comentário "oficial" (comentário de verdade é só com `#`).

---

## F-string (formatação de string)

Forma moderna de inserir variáveis dentro de um texto — mais legível que concatenar com `+`.

**Sintaxe:** colocar `f` antes das aspas, e a variável entre `{}`.

```python
nome2 = 'João'
nome3 = 'Melo'

fullname = f"Meu nome é {nome2} e meu sobrenome é {nome3}"
print(fullname)   # Meu nome é João e meu sobrenome é Melo
```

F-string também aceita multilinha (combinando `f` com `"""`):
```python
mensagem = f"""
Nome: {nome2}
Sobrenome: {nome3}
"""
```

---

## Resumo rápido de sintaxe

```python
string[i]        # caractere na posição i
string[-1]       # último caractere
string[a:b]      # da posição a até b (b exclusivo)
string[:b]       # do início até b (exclusivo)
string[a:]       # de a até o final
string[:]        # string inteira (cópia)
string[a:b:p]    # de a até b, pulando de p em p
string[::-1]     # string invertida

len(string)          # quantidade de caracteres
len(string) - 1       # índice do último caractere

f"texto {variavel}"   # f-string
```

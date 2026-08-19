# Python — Fundamentos

## Tipos de Dados

| Tipo | Representa | Exemplo |
|---|---|---|
| `int` | Números inteiros | `idade = 25` |
| `float` | Números decimais | `altura = 1.75` |
| `str` | Texto (string) | `nome = "João"` |
| `bool` | Verdadeiro/Falso | `ativo = True` |
| `None` | Ausência de valor | `resultado = None` |

### int
Números inteiros, sem casas decimais, positivos ou negativos.
```python
idade = 25
saldo = -100
```

### float
Números com casas decimais (ponto, não vírgula).
```python
altura = 1.75
preco = 19.90
```

### str
Texto, sempre entre aspas simples `'` ou duplas `"`.
```python
nome = "João"
cargo = 'Auditor'
```

### bool
Só existem dois valores possíveis: `True` ou `False`. Usado em condições e validações.
```python
ativo = True
aprovado = False
```

### None
Representa "nenhum valor" — não é zero, não é vazio, é a ausência de valor. Usado, por exemplo, para inicializar uma variável que ainda não tem resultado definido.
```python
resultado = None
```

---

## Função `type()`

Retorna o tipo de dado de uma variável ou valor. Serve para **confirmar** com que tipo você está lidando, principalmente quando o dado vem de fora (input, arquivo, banco de dados).

```python
idade = 25
print(type(idade))        # <class 'int'>

nome = "João"
print(type(nome))         # <class 'str'>

print(type(3.14))         # <class 'float'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'>
```

**Aplicabilidades:**
- Depurar (debugar) código quando um erro de tipo acontece;
- Validar o tipo de um dado recebido via `input()` (que sempre vem como `str`, mesmo se o usuário digitar um número);
- Confirmar o tipo de retorno de uma função antes de usá-lo em outra operação;
- Checar o tipo de dado vindo de uma API, arquivo, ou banco de dados antes de processar.

---

## Conversão de Tipos (Type Casting)

Você pode converter um valor de um tipo para outro usando o **nome do tipo como função**: `int()`, `float()`, `str()`, `bool()`.

### Convertendo diretamente uma variável
```python
texto_numero = "10"
numero = int(texto_numero)   # agora numero é int, não str
print(type(numero))          # <class 'int'>
```

### Convertendo o retorno do `input()`
`input()` **sempre retorna `str`**, mesmo que o usuário digite um número. Para usar o valor como número, é preciso converter — geralmente já na hora de capturar:

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

Sem o `int()`/`float()` na frente, `idade` seria uma `str` e não daria pra fazer contas com ela (ex: `idade + 1` geraria erro).

---

## Concatenação com `+`

Junta strings usando o operador `+`. **Só funciona entre strings** — para misturar com números, é preciso converter para `str` antes.

```python
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)   # João Silva
```

Misturando com número (precisa converter):
```python
idade = 25
mensagem = "Idade: " + str(idade)
print(mensagem)   # Idade: 25
```

---

## Quebra de linha `\n`

Dentro de uma string, `\n` insere uma quebra de linha ao imprimir.

```python
print("Linha 1\nLinha 2")
# Saída:
# Linha 1
# Linha 2
```

---

## Resumo rápido de sintaxe

```python
# Tipos
int, float, str, bool, None

# Verificar tipo
type(variavel)

# Converter tipo
int("10")
float("3.14")
str(25)
bool(1)

# Input já convertido
idade = int(input("Idade: "))

# Concatenar
"texto" + "texto"
"texto" + str(numero)

# Quebra de linha
"texto\nmais texto"
```

# Python — Métodos de String

Diferente de slicing (que você já domina), esses são **métodos prontos** da própria string — funções que já vêm embutidas e você chama com `.metodo()`.

## Maiúsculas e minúsculas

```python
texto = "Python"

texto.upper()   # "PYTHON" — tudo maiúsculo
texto.lower()   # "python" — tudo minúsculo
```

**Aplicação prática:** padronizar texto antes de comparar (ex: `.lower()` para não diferenciar "Sim" de "sim" — já usamos isso no exercício da CNH e do palíndromo).

---

## Removendo espaços — `strip()`, `lstrip()`, `rstrip()`

| Método | Remove espaços... |
|---|---|
| `.strip()` | Do início **e** do fim |
| `.lstrip()` | Só do início (esquerda) |
| `.rstrip()` | Só do fim (direita) |

```python
email = "joao@teste.com.br      "
print(email.strip())    # "joao@teste.com.br" (sem os espaços do final)
```

**Aplicação prática — muito comum:** limpar o que o usuário digita, para evitar espaços acidentais que atrapalhariam comparações depois.
```python
nome = input("Digite seu nome: ").strip()
```

---

## Substituindo texto — `replace()`

```python
texto2 = "Doti Melo"
print(texto2.replace("Doti", "João"))   # "João Melo"
```

**⚠️ String é imutável:** o `replace()` **não altera** a variável original — ele **retorna uma nova string**. Se você não salvar o resultado em outra variável (ou sobrescrever a mesma), o valor original continua intacto:
```python
print(texto2)   # ainda imprime "Doti Melo", sem alteração
```

### Limitando quantas substituições — terceiro parâmetro

```python
texto3 = "Doti Melo Doti Doti"
print(texto3.replace("Doti", "João", 1))
# Troca só a PRIMEIRA ocorrência: "João Melo Doti Doti"
```
Sem esse terceiro parâmetro, `replace()` troca **todas** as ocorrências encontradas.

---

## Buscando texto — `find()`

Retorna o **índice** da primeira ocorrência do texto buscado. Se não encontrar, retorna `-1`.

```python
texto3 = "Doti Melo Doti Doti"
print(texto3.find("i"))          # índice da 1ª ocorrência de "i" em toda a string
```

### Limitando o intervalo de busca

```python
print(texto3.find("i", 3, 15))   # busca só entre os índices 3 e 15
print(texto3.find("i", 3))       # busca a partir do índice 3 até o final (sem limite de fim)
```

---

## Contando ocorrências — `count()`

```python
texto4 = "João Marcos Doti Melo"
print(texto4.count("o"))    # quantas vezes "o" aparece no texto
```

---

## Métodos de Validação

Retornam sempre `bool` (`True`/`False`). Úteis para validar dados de entrada antes de processar (ex: conferir se um campo é realmente numérico).

| Método | Valida se... |
|---|---|
| `.isdigit()` | A string contém **só números** |
| `.isalpha()` | A string contém **só letras** |
| `.isalnum()` | A string contém **só letras e/ou números** (sem espaço, sem símbolo) |

```python
"123".isdigit()      # True
"abc".isdigit()      # False

"abc".isalpha()      # True
"abc123".isalpha()   # False

"abc123".isalnum()   # True
"abc 123".isalnum()  # False (o espaço não é letra nem número)
```

**Observação:** esses métodos não diferenciam maiúsculas de minúsculas — `"ABC".isalpha()` também retorna `True`.

**Aplicação prática:** validar entrada de usuário antes de converter tipo — por exemplo, checar `if texto.isdigit():` antes de rodar `int(texto)`, evitando que o programa quebre se o usuário digitar uma letra onde deveria ser número.

---

## Resumo rápido de sintaxe

```python
string.upper()
string.lower()
string.strip()
string.lstrip()
string.rstrip()
string.replace(antigo, novo)
string.replace(antigo, novo, quantidade)
string.find(procurado)
string.find(procurado, inicio)
string.find(procurado, inicio, fim)
string.count(procurado)

string.isdigit()
string.isalpha()
string.isalnum()
```

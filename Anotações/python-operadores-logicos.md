# Python — Operadores Lógicos

Combinam ou invertem condições booleanas (`True`/`False`). Muito usados dentro de `if`/`while` quando uma decisão depende de mais de uma condição.

| Operador | Significado | Regra |
|---|---|---|
| `and` | E | **Todas** as condições precisam ser `True` |
| `or` | Ou | **Pelo menos uma** condição precisa ser `True` |
| `not` | Negação | **Inverte** o valor de uma condição (não combina duas) |

---

## `and` (E)

Só retorna `True` se **todas** as condições forem verdadeiras.

```python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
```

Tabela-verdade:
| A | B | A and B |
|---|---|---|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

---

## `or` (OU)

Retorna `True` se **pelo menos uma** condição for verdadeira.

```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Fim de semana")
```

Tabela-verdade:
| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

---

## `not` (Negação)

Inverte o valor de **uma única** condição/expressão — diferente de `and`/`or`, não combina duas coisas, só nega uma.

```python
ativo = True
print(not ativo)          # False

idade = 15
if not idade >= 18:
    print("Menor de idade")
```

Tabela-verdade:
| A | not A |
|---|---|
| True | **False** |
| False | **True** |

---

## Combinando operadores

Dá para combinar `and`, `or` e `not` na mesma condição. Parênteses ajudam a deixar claro o que é avaliado primeiro (mesma lógica de matemática):

```python
idade = 20
tem_ingresso = True
esta_acompanhado = False

if (idade >= 18 or esta_acompanhado) and tem_ingresso:
    print("Pode entrar")
```

# Python — Operadores

## Operadores Aritméticos

| Operador | Nome | Exemplo | Resultado |
|---|---|---|---|
| `+` | Soma | `5 + 2` | `7` |
| `-` | Subtração | `5 - 2` | `3` |
| `*` | Multiplicação | `5 * 2` | `10` |
| `/` | Divisão | `5 / 2` | `2.5` |
| `//` | Divisão inteira (piso) | `5 // 2` | `2` |
| `%` | Módulo (resto da divisão) | `5 % 2` | `1` |
| `**` | Potenciação | `5 ** 2` | `25` |

### Pontos de atenção

**`/` sempre retorna `float`**, mesmo quando o resultado é "redondo":
```python
10 / 2   # 5.0  (float, não 5)
```

**`//` (divisão inteira) faz divisão de piso — arredonda para baixo**, não é simplesmente "descartar a casa decimal". Para números positivos dá no mesmo resultado que truncar, mas para negativos NÃO:
```python
7 // 2    # 3
-7 // 2   # -4   (arredonda para baixo, não é -3)
```

**`%` (módulo)** é muito usado para descobrir se um número é par/ímpar, ou para verificar múltiplos:
```python
10 % 2   # 0  → 10 é par (resto da divisão por 2 é 0)
7 % 2    # 1  → 7 é ímpar
```

---

## Operadores Relacionais (Comparação)

Sempre retornam `bool` (`True` ou `False`). Usados em condições (`if`, `while`).

| Operador | Significado | Exemplo | Resultado |
|---|---|---|---|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Maior que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Maior ou igual | `5 >= 5` | `True` |
| `<=` | Menor ou igual | `5 <= 4` | `False` |

### ⚠️ Ponto de atenção — não confundir `=` com `==`

- `=` → **atribuição** (guarda um valor numa variável): `idade = 18`
- `==` → **comparação** (pergunta se são iguais): `idade == 18`

Usar `=` onde deveria ser `==` é o erro mais comum de iniciante. Dentro de um `if`, o Python vai acusar erro de sintaxe se você usar `=` por engano.

```python
idade = 18          # atribuição: idade agora VALE 18
if idade == 18:      # comparação: PERGUNTA se idade é igual a 18
    print("Maior de idade")
```

# Manual de Uso da Calculadora Científica

Este manual descreve a sintaxe e o uso das funções disponíveis na calculadora, incluindo funções básicas, científicas e estatísticas.

---

## Funções Básicas

### adicionar(a, b)
Retorna a soma de `a` e `b`.

**Exemplo:**
```python
resultado = adicionar(3, 5)  # Retorna 8
print(f"Soma: {resultado}")
```

### subtrair(a, b)
Retorna a subtração de `b` de `a`.

**Exemplo:**
```python
resultado = subtrair(10, 4)  # Retorna 6
print(f"Subtração: {resultado}")
```

### multiplicar(a, b)
Retorna a multiplicação de `a` por `b`.

**Exemplo:**
```python
resultado = multiplicar(6, 7)  # Retorna 42
print(f"Multiplicação: {resultado}")
```

### dividir(a, b)
Retorna a divisão de `a` por `b`. Lança erro se `b` for zero.

**Exemplo:**
```python
try:
    resultado = dividir(20, 4)  # Retorna 5.0
    print(f"Divisão: {resultado}")
except ValueError as e:
    print(e)
```

---

## Funções Científicas

### potencia(base, expoente)
Retorna `base` elevado ao `expoente`.

**Exemplo:**
```python
resultado = potencia(2, 3)  # Retorna 8
print(f"Potência: {resultado}")
```

### raiz(n, grau=2)
Retorna a raiz de grau `grau` do número `n`. Por padrão, raiz quadrada.

**Exemplo:**
```python
resultado = raiz(9)       # Retorna 3.0
print(f"Raiz quadrada: {resultado}")

resultado = raiz(27, 3)   # Retorna 3.0 (raiz cúbica)
print(f"Raiz cúbica: {resultado}")
```

### logaritmo(n, base=math.e)
Retorna o logaritmo de `n` na base especificada. Base padrão é o número de Euler (log natural).

**Exemplo:**
```python
resultado = logaritmo(10, 10)  # Retorna 1.0
print(f"Logaritmo base 10: {resultado}")

resultado = logaritmo(2.718)   # Aproximadamente 1.0 (log natural)
print(f"Logaritmo natural: {resultado}")
```

### seno(x)
Retorna o seno de `x` (em radianos).

**Exemplo:**
```python
import math
resultado = seno(math.pi / 2)  # Retorna 1.0
print(f"Seno: {resultado}")
```

### cosseno(x)
Retorna o cosseno de `x` (em radianos).

**Exemplo:**
```python
import math
resultado = cosseno(0)  # Retorna 1.0
print(f"Cosseno: {resultado}")
```

### tangente(x)
Retorna a tangente de `x` (em radianos).

**Exemplo:**
```python
import math
resultado = tangente(0)  # Retorna 0.0
print(f"Tangente: {resultado}")
```

---

## Funções Estatísticas

Todas as funções estatísticas recebem uma lista de números (`list`).

### media(lista)
Retorna a média aritmética da lista.

**Exemplo:**
```python
lista = [1, 2, 3, 4, 5]
resultado = media(lista)  # Retorna 3
print(f"Média: {resultado}")
```

### mediana(lista)
Retorna a mediana da lista.

**Exemplo:**
```python
lista = [1, 3, 3, 6, 7, 8, 9]
resultado = mediana(lista)  # Retorna 6
print(f"Mediana: {resultado}")
```

### moda(lista)
Retorna a moda da lista.

**Exemplo:**
```python
lista = [1, 2, 2, 3, 4]
resultado = moda(lista)  # Retorna 2
print(f"Moda: {resultado}")
```

### variancia(lista)
Retorna a variância da lista.

**Exemplo:**
```python
lista = [1, 2, 3, 4, 5]
resultado = variancia(lista)  # Retorna 2.5
print(f"Variância: {resultado}")
```

---

## Uso na Interface Gráfica

- Para funções básicas e científicas, utilize os botões correspondentes e insira os valores conforme solicitado.
- Para funções estatísticas, insira a função seguida de uma lista de números entre parênteses, separados por vírgula. Exemplo:  
  `mean(1,2,3,4,5)`  
  A calculadora interpretará e calculará o resultado.

---

Se precisar de mais detalhes ou exemplos, estou à disposição para ajudar!

# Manual de Uso da Calculadora Científica

Este manual descreve a sintaxe e o uso das funções disponíveis na calculadora, incluindo funções básicas, científicas e estatísticas.

---

## Uso na Interface Gráfica

Para utilizar as funções na interface gráfica da calculadora, siga as orientações abaixo:

- Insira os números e operadores diretamente no campo de entrada, utilizando os botões disponíveis ou digitando pelo teclado.
- Para funções básicas e científicas, utilize os botões correspondentes para inserir a função e os valores.
- Para funções estatísticas, insira a função seguida de uma lista de números entre parênteses, separados por vírgula. Exemplo:  
  `mean(1,2,3,4,5)`  
  A calculadora interpretará essa expressão e calculará o resultado.
- Use o botão `=` para calcular o resultado da expressão inserida.
- Use o botão `C` para limpar o campo de entrada.

---

## Funções Básicas

### adicionar(a, b)
Retorna a soma de `a` e `b`.

**Exemplo na interface:**
```
3 + 5 =
```
Resultado: 8

### subtrair(a, b)
Retorna a subtração de `b` de `a`.

**Exemplo na interface:**
```
10 - 4 =
```
Resultado: 6

### multiplicar(a, b)
Retorna a multiplicação de `a` por `b`.

**Exemplo na interface:**
```
6 * 7 =
```
Resultado: 42

### dividir(a, b)
Retorna a divisão de `a` por `b`. Lança erro se `b` for zero.

**Exemplo na interface:**
```
20 / 4 =
```
Resultado: 5.0

---

## Funções Científicas

### potencia(base, expoente)
Use o operador `^` para potência.

**Exemplo na interface:**
```
2 ^ 3 =
```
Resultado: 8

### raiz(n, grau=2)
Use o símbolo `√` para raiz quadrada. Para raiz de grau diferente, insira o grau após a raiz.

**Exemplo na interface:**
```
√ 9 =
```
Resultado: 3.0

```
√ 27 3 =
```
Resultado: 3.0 (raiz cúbica)

### logaritmo(n, base=math.e)
Use `log` seguido do número para logaritmo natural ou com base 10.

**Exemplo na interface:**
```
log 10 =
```
Resultado: 1.0 (log base 10)

---

## Funções Trigonométricas

Use `sin`, `cos`, `tan` seguidos do ângulo em graus.

**Exemplo na interface:**
```
sin 90 =
```
Resultado: 1.0

---

## Funções Estatísticas

Insira a função seguida da lista de números entre parênteses, separados por vírgula.

### media (mean)

**Exemplo na interface:**
```
mean(1,2,3,4,5) =
```
Resultado: 3

### mediana (median)

**Exemplo na interface:**
```
median(1,3,3,6,7,8,9) =
```
Resultado: 6

### moda (mode)

**Exemplo na interface:**
```
mode(1,2,2,3,4) =
```
Resultado: 2

### variancia (variance)

**Exemplo na interface:**
```
variance(1,2,3,4,5) =
```
Resultado: 2.5

---

Se precisar de mais detalhes ou exemplos, estou à disposição para ajudar!

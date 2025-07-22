"""
Calculadora Científica em Python - Entrega 3
Inclui funções básicas, científicas e estatísticas
Projeto didático para aprendizado de programação e engenharia de software
"""

import math
import statistics

def adicionar(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de b de a."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de a por b."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de a por b. Lança erro se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(base, expoente):
    """Retorna base elevado ao expoente."""
    return math.pow(base, expoente)

def raiz(n, grau=2):
    """Retorna a raiz de grau 'grau' do número n."""
    if n < 0 and grau % 2 == 0:
        raise ValueError("Raiz par de número negativo não é permitida.")
    return n ** (1 / grau)

def logaritmo(n, base=math.e):
    """Retorna o logaritmo de n na base especificada."""
    if n <= 0:
        raise ValueError("Logaritmo de número não positivo não é definido.")
    if base <= 0 or base == 1:
        raise ValueError("Base do logaritmo deve ser positiva e diferente de 1.")
    return math.log(n, base)

def seno(x):
    """Retorna o seno de x (x em radianos)."""
    return math.sin(x)

def cosseno(x):
    """Retorna o cosseno de x (x em radianos)."""
    return math.cos(x)

def tangente(x):
    """Retorna a tangente de x (x em radianos)."""
    return math.tan(x)

# Funções estatísticas

def media(lista):
    """Retorna a média aritmética da lista de números."""
    return statistics.mean(lista)

def mediana(lista):
    """Retorna a mediana da lista de números."""
    return statistics.median(lista)

def moda(lista):
    """Retorna a moda da lista de números."""
    return statistics.mode(lista)

def variancia(lista):
    """Retorna a variância da lista de números."""
    return statistics.variance(lista)

def main():
    print("Calculadora Científica - Entrega 3")
    # Interface será atualizada posteriormente
    pass

if __name__ == "__main__":
    main()
